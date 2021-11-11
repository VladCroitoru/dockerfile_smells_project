FROM ubuntu:xenial
MAINTAINER sh@analogic.cz

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends nginx-light php7.0-fpm php7.0-cli php7.0-json

RUN sed 's/\# server_tokens off;/server_tokens off;/' -i /etc/nginx/nginx.conf && echo "expose_php = off" >> /etc/php/7.0/fpm/php.ini
RUN sed 's/listen = \/run\/php\/php7.0-fpm\.sock/listen = \/var\/run\/php-fpm.sock/' -i /etc/php/7.0/fpm/pool.d/www.conf && \
    sed 's/pid = \/run\/php\/php7.0-fpm\.pid/pid = \/var\/run\/php-fpm.pid/' -i /etc/php/7.0/fpm/php-fpm.conf

EXPOSE 80

ADD rootfs /
