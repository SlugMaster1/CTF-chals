import jwt
import bcrypt
from os import urandom
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET'] = urandom(16).hex()
app.config['FLAG'] = open('flag.txt').read()

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    jwt_algorithm = db.Column(db.String(10), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

def init_db():
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            test_user = User(username='admin')
            test_user.set_password(urandom(16).hex())
            db.session.add(test_user)
            db.session.commit()

def create_access_token(user, algorithm='HS256', admin=False):
    try:
        token = jwt.encode({"user": user, "admin": admin}, app.config['JWT_SECRET'], algorithm=algorithm)
    except:
        return None
    return token

def decode_access_token(token):
    try:
        user_data = jwt.decode(token, options={"verify_signature": False})
        user = user_data['user']
        algorithm = User.query.filter_by(username=user).first().jwt_algorithm
        if algorithm == 'HS256':
            user_data = jwt.decode(token, app.config['JWT_SECRET'], algorithms=[algorithm])
        elif algorithm == 'none':
            user_data = jwt.decode(token, options={'verify_signature': False}, algorithms=[algorithm])
        else:
            user_data = jwt.decode(token, algorithms=[algorithm])
    except:
        return None
    return user_data
    

@app.route('/')
def home():
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        rows = User.query.filter_by(username=username)
        count = rows.count()
        user = rows.first()
        
        if count == 1 and user.check_password(password):
            algorithm = User.query.filter_by(username=user.username).first().jwt_algorithm
            access_token = create_access_token(username,algorithm=algorithm,admin=username=='admin')
            if access_token is None:
                return render_template('login.html', error="There was an unexpected error with your login, please try again")
            response = redirect(url_for('profile'))
            response.set_cookie('access_token', access_token)
            return response

        return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).count()
        if not user:
            try:
                db.session.execute(text(f'INSERT INTO User (username, password_hash, jwt_algorithm) VALUES ("{username}", "{bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")}", "HS256")'))
                db.session.commit()
            except:
                return render_template('register.html', error="Database error")
            response = redirect(url_for('login_page'))
            return response

        return render_template('register.html', error="User already exists")

    return render_template('register.html')

@app.route('/profile')
def profile():
    if 'access_token' in request.cookies:
        user_jwt = request.cookies['access_token']
        user_data = decode_access_token(user_jwt)
        if user_data is None:
            return render_template('profile.html', error="Error validating token")
        if 'user' in user_data and 'admin' in user_data and user_data['admin']:
            return render_template('profile.html', username=user_data['user'], flag=app.config['FLAG'])
        elif 'user' in user_data:
            return render_template('profile.html', username=user_data['user'])
    return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    response = redirect(url_for('login_page'))
    response.set_cookie('access_token', '', expires=0)
    return response

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')
