FROM python:3.9-slim

WORKDIR /app

RUN pip3 install gunicorn requests flask

COPY MANIFEST.in setup.py README.md gitlabui-runner.py /app/
COPY gitlabui /app/gitlabui

RUN python3 /app/setup.py install && rm -rf /app/*
