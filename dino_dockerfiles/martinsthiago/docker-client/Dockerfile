FROM ubuntu:16.04
MAINTAINER 'Martins <rogue.thiago@gmail.com>'

RUN apt-get update &&\
    apt-get install -y curl ssh git python

RUN curl "https://get.docker.com/builds/`uname -s`/`uname -m`/docker-latest.tgz" > docker.tgz &&\
    tar -xvzf docker.tgz &&\
    mv docker/* /usr/bin &&\
    rm -rf docke* &&\
    curl -L "https://raw.githubusercontent.com/MartinsThiago/rdocker/master/rdocker.sh" > /usr/local/bin/rdocker &&\
    chmod +x /usr/local/bin/rdocker &&\
    curl  -L "https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m`" > /usr/local/bin/docker-compose &&\
    chmod +x /usr/local/bin/docker-compose
