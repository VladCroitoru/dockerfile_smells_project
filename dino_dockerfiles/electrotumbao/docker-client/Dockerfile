FROM ubuntu:16.04

ENV COMPOSE_VERSION 1.18.0

RUN apt-get update && \
    apt-get install -y curl ssh git python lsb-release software-properties-common apt-transport-https

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
RUN apt-get update && \
    apt-get install -y docker-ce


RUN curl -L "https://github.com/dvddarias/rdocker/raw/master/rdocker.sh" > /usr/local/bin/rdocker &&\
    chmod +x /usr/local/bin/rdocker &&\
    curl  -L "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m`" > /usr/local/bin/docker-compose &&\
    chmod +x /usr/local/bin/docker-compose
