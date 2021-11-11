FROM node:latest

MAINTAINER Alexander Martin <alex@suitupalex.com>

ENV HOME /root

RUN apt-get update -qq && \
    apt-get install -y -qq php5 php5-cli php5-cgi

RUN wget http://getcomposer.org/composer.phar && \
    chmod 777 composer.phar && \
    mv composer.phar /usr/local/bin/composer
