FROM ubuntu:14.04
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get update
RUN apt-get install -y wget python python-dev python-pip
RUN pip install supervisor
RUN mkdir -p /var/log/supervisor

RUN wget https://github.com/jwilder/docker-gen/releases/download/0.3.6/docker-gen-linux-amd64-0.3.6.tar.gz
RUN tar xvzf docker-gen-linux-amd64-0.3.6.tar.gz -C /usr/local/bin

ENV DOCKER_HOST unix:///var/run/docker.sock
ENV NOTIFY cat /tmp/containers.json
ENV INTERVAL 10

ADD . /

CMD /usr/local/bin/supervisord -c /etc/supervisord.conf
