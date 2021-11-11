FROM python:3.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .