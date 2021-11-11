FROM analogic/trusty
MAINTAINER sh@analogic.cz

ADD https://nchan.slact.net/download/nginx-nchan-latest.tar.gz /tmp/
RUN tar xzf /tmp/nginx-nchan-latest.tar.gz -C /

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends php5-fpm php5-cli php5-json

RUN sed 's/\# server_tokens off;/server_tokens off;/' -i /etc/nginx/nginx.conf && echo "expose_php = off" >> /etc/php5/fpm/php.ini

EXPOSE 80

ADD rootfs /
