# Use official Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create instance directory
RUN mkdir -p instance

# Initialize database
RUN python -c "from app import app, db; app.app_context().push(); db.create_all()"
RUN python init_db.py

# Expose the port
EXPOSE {{challenge.port}}

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port={{challenge.port}}"]
