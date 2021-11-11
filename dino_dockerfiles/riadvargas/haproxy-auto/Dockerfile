FROM alpine
MAINTAINER Riad Vargas de Oliveira me@riadvargas.com.br

RUN apk update \
    && apk add haproxy ca-certificates curl openssl rsyslog bash

ENV DOCKER_GEN_VERSION 0.7.3
RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
    && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
    && rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

WORKDIR /app/
ENV DOCKER_HOST unix:///tmp/docker.sock

ADD files/haproxy.cfg   /etc/haproxy/haproxy.cfg
ADD files/rsyslog.conf  /etc/rsyslog.conf
ADD files/run.sh        /app/run.sh
ADD files/reload.sh     /usr/bin/reload-haproxy
ADD files/haproxy.tpl   /app/haproxy.tpl

RUN chmod +x /app/run.sh
RUN chmod +x /usr/bin/reload-haproxy
ENTRYPOINT ["/app/run.sh"]
