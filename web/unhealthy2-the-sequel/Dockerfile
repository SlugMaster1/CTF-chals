# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN pip install flask
COPY ./challenge /app
COPY ./flag.txt /flag.txt

USER www-data
EXPOSE {{challenge.port}}

CMD ["python", "app.py", "{{challenge.port}}"]
