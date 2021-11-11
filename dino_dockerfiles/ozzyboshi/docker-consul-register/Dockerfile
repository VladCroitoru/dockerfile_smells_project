FROM ubuntu:14.04
MAINTAINER Alessio Garzi <gun101@email.it>

RUN apt-get update
RUN apt-get install -y wget python python-pip python-dev libssl-dev libffi-dev bash timelimit

RUN mkdir /app
WORKDIR /app

RUN wget https://github.com/jwilder/docker-gen/releases/download/0.5.0/docker-gen-linux-amd64-0.5.0.tar.gz
RUN tar xvzf docker-gen-linux-amd64-0.5.0.tar.gz -C /usr/local/bin

RUN pip install python-consul

ADD . /app

ENV DOCKER_HOST unix:///var/run/docker.sock

CMD docker-gen -interval 10 -watch -notify "timelimit -t 15 python /tmp/register.py" consul.tmpl /tmp/register.py
