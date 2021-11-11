FROM python:3.6.8-slim

ENV TZ=Europe/Warsaw

ENV PYTHONUNBUFFERED=0

RUN apt-get update \
    && apt-get install -y cron

COPY ./cronpy /etc/cron.d/cronpy
RUN crontab /etc/cron.d/cronpy

RUN chmod 0644 /etc/cron.d/cronpy

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade -r requirements.txt

COPY ./src /app/src

RUN chmod 0744 /app/src/main.py

CMD ["cron", "-f"]
