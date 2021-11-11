FROM ubuntu:trusty
MAINTAINER Viktor Tusa <tusavik@gmail.com>

ADD ./ /app
RUN apt-get update && apt-get install -y python-pip python-dev python-openssl && pip install -r /app/requirements.txt

EXPOSE 5000

WORKDIR /app

CMD python app.py

