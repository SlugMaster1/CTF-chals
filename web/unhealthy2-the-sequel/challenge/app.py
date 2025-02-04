from sys import argv
from subprocess import run
from flask import Flask, render_template, request, send_file
from firewall import validate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return send_file('./robots.txt')

@app.route('/health-check')
def health():
    return render_template('health.html')

@app.route('/health-check', methods=['POST'])
def check():
    ip = request.form['ip']
    if validate(ip):
        response = run(f'ping -c 1 {ip}',shell=True,capture_output=True).stdout
        return render_template('health.html', response=response.decode())
    return render_template('error.html')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(argv[1]))
