FROM python:3.10-slim

RUN apt-get update && apt-get install -y time && \
    pip install numpy pandas pillow

WORKDIR /app

COPY ../requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

