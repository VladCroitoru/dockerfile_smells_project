FROM meoooh/ubuntu14.04
MAINTAINER Jaap van Arragon <j.vanarragon@lukkien.com>

RUN \
    apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y locales wget gcc ruby-dev make libpcre3 libpcre3-dev zlib1g zlib1g-dev openssl libssl-dev && \
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
    gem install fpm && \
    apt-get autoremove
