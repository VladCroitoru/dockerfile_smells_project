FROM registry.shanemcc.net/public/docker-apache-php-base:latest
MAINTAINER Shane Mc Cormack <dataforce@dataforce.org.uk>

COPY . /dnsfrontend

RUN \
  rm -Rfv /var/www/html && \
  chown -Rfv www-data: /dnsfrontend/ /var/www/ && \
  ln -s /dnsfrontend/public /var/www/html && \
  cd /dnsfrontend/ && \
  su www-data --shell=/bin/bash -c "cd /dnsfrontend; /usr/bin/composer install"


EXPOSE 80
