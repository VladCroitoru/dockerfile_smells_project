FROM python:3.6-alpine3.6

MAINTAINER parisswing@gmail.com

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN pip install awscli
RUN apk update 
RUN apk add docker

COPY pull.sh /usr/local/

ENTRYPOINT ["/usr/local/pull.sh"]

