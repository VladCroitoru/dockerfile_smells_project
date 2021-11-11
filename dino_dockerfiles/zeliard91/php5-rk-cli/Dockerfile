FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y dist-upgrade

RUN echo "deb http://ppa.launchpad.net/ondrej/php5/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C && \
    apt-get update

RUN apt-get update && apt-get -y install curl git php5-cli php5-gd \
    php5-mcrypt php5-mongo php5-curl php5-mysql php5-sqlite

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

ENTRYPOINT ["/usr/bin/php"]
