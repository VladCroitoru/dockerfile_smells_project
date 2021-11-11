FROM analogic/trusty
MAINTAINER sh@analogic.cz

ADD https://nchan.slact.net/download/nginx-nchan-latest.tar.gz /tmp/

RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    gpg --keyserver pool.sks-keyservers.net --recv E5267A6C && \
    gpg --export --armor E5267A6C | apt-key add - && \

    tar xzf /tmp/nginx-nchan-latest.tar.gz -C / && \

    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends php7.1-fpm php7.1-cli php7.1-json && \

    sed 's/\# server_tokens off;/server_tokens off;/' -i /etc/nginx/nginx.conf && echo "expose_php = off" >> /etc/php/7.1/fpm/php.ini && \
    sed 's/listen = \/run\/php\/php7.1-fpm\.sock/listen = \/var\/run\/php-fpm.sock/' -i /etc/php/7.1/fpm/pool.d/www.conf && \
    sed 's/pid = \/run\/php\/php7.1-fpm\.pid/pid = \/var\/run\/php-fpm.pid/' -i /etc/php/7.1/fpm/php-fpm.conf

EXPOSE 80

ADD rootfs /
