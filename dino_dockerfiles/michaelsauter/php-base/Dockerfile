FROM ubuntu
MAINTAINER Michael Sauter, mail@michaelsauter.net

ENV REFRESHED_AT 2014-02-19
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y curl
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y php5-mysql php5-cli

# Composer
RUN curl -sS https://getcomposer.org/installer | php
RUN chmod +x composer.phar && mv composer.phar /usr/local/bin/composer

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
