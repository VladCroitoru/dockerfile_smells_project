FROM ubuntu:14.04
MAINTAINER James Hill <jhill@amelco.co.uk>

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN rm /etc/nginx/nginx.conf
COPY docker/nginx.conf /etc/nginx/

EXPOSE 80
EXPOSE 443