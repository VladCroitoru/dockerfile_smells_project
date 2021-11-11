# Version: 0.0.1
FROM ubuntu:16.04
MAINTAINER Vlad STAN "stan.v.vlad@gmail.com"
RUN apt-get update && apt-get install -y nginx
RUN echo 'Hi, I am in your container built from GitHub Dockerfile!' >/var/www/html/index.html
EXPOSE 80

LABEL version=0.3 location=cluj.hub
