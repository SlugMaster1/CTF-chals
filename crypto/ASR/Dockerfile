# Start with a lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the ASR directory into the container
COPY ASR /app/ASR

# Generate the flag and set it as an environment variable
ENV FLAG="FFCTF{D0nt_m1x_yOUr_k3y5!}"

# Install necessary dependencies
RUN pip install pycryptodome

# Expose the desired port
EXPOSE 8000

# Command to run the Python script on startup
CMD ["python3", "ASR/ASR.py"]
