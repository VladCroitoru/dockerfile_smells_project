FROM python:3.7.7-alpine

COPY . /app
COPY requirements.txt /

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["./gunicorn_starter.sh"]
