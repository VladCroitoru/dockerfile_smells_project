# Dockerfile for private webserver
#
# VERSION 1.0

FROM ubuntu

MAINTAINER toyama satoshi <toyamarinyon@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y curl git-core nginx

EXPOSE 80

CMD ["service","nginx","start"]
