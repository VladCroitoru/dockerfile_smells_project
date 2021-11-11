FROM nginx:1.19.10-alpine
MAINTAINER Damien Garros <dgarros@gmail.com>

RUN apk update
RUN apk add wget
RUN wget --no-check-certificate https://github.com/jwilder/docker-gen/releases/download/0.7.1/docker-gen-alpine-linux-amd64-0.7.1.tar.gz
RUN tar xvzf docker-gen-alpine-linux-amd64-0.7.1.tar.gz

WORKDIR /

COPY entrypoint.sh entrypoint.sh
COPY nginx.conf.tpl /etc/nginx/nginx.conf.tpl

RUN chmod 777 /entrypoint.sh

ENV DOCKER_HOST unix:///tmp/docker.sock

EXPOSE 6000/udp

CMD /entrypoint.sh
