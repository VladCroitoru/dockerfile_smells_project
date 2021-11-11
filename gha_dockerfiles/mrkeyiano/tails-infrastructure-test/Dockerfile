FROM python:3.5-slim-buster

RUN apt-get update

WORKDIR ./app

ADD . .

ENV FLASK_APP=app.py

RUN pip install -r requirements.txt


EXPOSE 7777

CMD flask run --host=0.0.0.0 --port 7777
