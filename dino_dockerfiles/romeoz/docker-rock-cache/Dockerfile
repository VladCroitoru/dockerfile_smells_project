FROM romeoz/docker-nginx-php
MAINTAINER romeOz <serggalka@gmail.com>

RUN apt-get update \
    && apt-get install -y php5-memcached \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /etc/nginx/sites-enabled/*

ADD ./sites-enabled/ /etc/nginx/sites-enabled/
ADD ./src/ /var/www/rock-cache/

WORKDIR /var/www/rock-cache/

RUN composer install --prefer-dist --no-dev \
    && chown www-data:www-data /var/www/rock-cache -R

EXPOSE 80

CMD ["/usr/bin/supervisord"]