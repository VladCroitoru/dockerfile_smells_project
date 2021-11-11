FROM romeoz/docker-nginx-php
MAINTAINER romeOz <serggalka@gmail.com>

RUN rm -rf /etc/nginx/sites-enabled/*

ADD ./sites-enabled/ /etc/nginx/sites-enabled/
ADD ./src/ /var/www/rock-sanitize/

WORKDIR /var/www/rock-sanitize/

RUN composer install --prefer-dist --no-dev \
    && chown www-data:www-data /var/www/rock-sanitize -R

EXPOSE 80

CMD ["/usr/bin/supervisord"]