FROM ubuntu:16.04

MAINTAINER Dao Anh Dung <dung13890@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install hugo
RUN apt-get update \
   && apt-get install -y wget

RUN wget https://github.com/gohugoio/hugo/releases/download/v0.31.1/hugo_0.31.1_Linux-64bit.deb

RUN dpkg -i hugo*.deb

RUN apt-get install -f

RUN usermod -u 1000 www-data

WORKDIR /var/www/app

EXPOSE 1313
