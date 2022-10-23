FROM python:3.10.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends tk-dev && rm -r /var/lib/apt/lists/*
RUN apt update -y && apt install -y build-essential libpq-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP run_single_app.py

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN flask db upgrade

COPY . .