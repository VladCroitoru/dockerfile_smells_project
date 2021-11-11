FROM php:7.3-apache-buster

EXPOSE 80

LABEL description="FirebirdWebAdmin 3.4.0 webbased interface to a firebird sql server"
LABEL maintainer="marian.aldenhoevel@marian-aldenhoevel.de"

ARG DEBIAN_FRONTEND=noninteractive
ARG APP_VERSION=3.4.1

WORKDIR /var/www/html

RUN \
	# rm /etc/apache2/mods-available/php5.load \
	apt-get update \
	&& apt-get install -y --no-install-recommends firebird-dev firebird3.0-utils \
	&& docker-php-ext-install interbase \
	&& docker-php-ext-enable interbase \
	&& ln -s /usr/bin/isql-fb /usr/bin/isql \
	&& curl https://codeload.github.com/mariuz/firebirdwebadmin/tar.gz/${APP_VERSION} | tar zxv --strip-components=1 \
	&& apt-get purge -y firebird-dev \
	&& apt-get autoremove -y --purge \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*
	
# Stuff we want for debugging
#RUN \
#	apt-get update \
#	&& apt-get install -y --no-install-recommends iputils-ping telnet nano file net-tools curl procps	

ADD . ./
