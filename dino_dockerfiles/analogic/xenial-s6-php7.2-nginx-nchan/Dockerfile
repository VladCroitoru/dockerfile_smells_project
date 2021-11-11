FROM ubuntu:xenial
MAINTAINER sh@analogic.cz

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
ADD https://nchan.slact.net/download/nginx-nchan-latest.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
    echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" | tee -a /etc/apt/sources.list && \
    echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" | tee -a /etc/apt/sources.list && \
    gpg --keyserver pool.sks-keyservers.net --recv E5267A6C && \
    gpg --export --armor E5267A6C | apt-key add - && \

    tar xzf /tmp/nginx-nchan-latest.tar.gz -C / && \

    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends php7.2-fpm php7.2-cli php7.2-json && \

    sed 's/\# server_tokens off;/server_tokens off;/' -i /etc/nginx/nginx.conf && echo "expose_php = off" >> /etc/php/7.2/fpm/php.ini && \
    sed 's/listen = \/run\/php\/php7.2-fpm\.sock/listen = \/var\/run\/php-fpm.sock/' -i /etc/php/7.2/fpm/pool.d/www.conf && \
    sed 's/pid = \/run\/php\/php7.2-fpm\.pid/pid = \/var\/run\/php-fpm.pid/' -i /etc/php/7.2/fpm/php-fpm.conf && \
    rm -Rf /tmp/*

EXPOSE 80

ENTRYPOINT ["/init"]
ADD rootfs /
