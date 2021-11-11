FROM nextcloud:stable

LABEL maintainer="github.com/Develbold"

# Project-specific ini settings
COPY ./php-ini-overrides.ini /usr/local/etc/php/conf.d/

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y nano
RUN apt-get install -y imagemagick
