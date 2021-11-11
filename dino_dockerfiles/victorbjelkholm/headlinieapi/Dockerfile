FROM dockerfile/ubuntu

# Container stuff

RUN apt-get update
RUN apt-get install --yes php5 php5-dev nginx php5-fpm

# Installing composer

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Application stuff

RUN mkdir -p /headlinie/
RUN mkdir /composer
WORKDIR /headlinie/www
ADD www/composer.json /headlinie/www/composer.json
RUN composer install -vvv --optimize-autoloader --no-dev
ADD . /headlinie/
WORKDIR /

# Configuration stuff

RUN rm /etc/nginx/sites-enabled/default
ADD configs/site_headlinie_api /etc/nginx/sites-available/headlinie_api
ADD configs/nginx.conf /etc/nginx/nginx.conf
RUN ln -s /etc/nginx/sites-available/headlinie_api /etc/nginx/sites-enabled/headlinie_api

# Running stuff

EXPOSE 8000
CMD sh /headlinie/scripts/run-app.sh -n -f
