FROM azul/zulu-openjdk-alpine:8
MAINTAINER Saul Hernandez <me@sauldhernandez.com>

RUN wget https://download.docker.com/linux/static/stable/x86_64/docker-17.03.0-ce.tgz -O /docker.tgz && \
    cd / && \
    tar -xvzf /docker.tgz && \
    mv /docker/* /usr/local/bin && \
    rm /docker.tgz

RUN wget https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -O /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose
    
