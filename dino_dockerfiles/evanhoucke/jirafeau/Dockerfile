FROM php:7-apache

RUN apt-get update && apt-get install -y unzip wget

RUN cd /var/www/ && wget https://gitlab.com/mojo42/Jirafeau/repository/archive.zip && unzip archive.zip
RUN rm -rf /var/www/html && mv /var/www/Jirafeau* /var/www/html 
ADD config.local.php /var/www/html/lib/config.local.php

RUN chown www-data:www-data /var/www/html/lib/config.local.php && chmod u+w /var/www/html/lib/config.local.php
RUN mkdir /data/ && chown -R www-data:www-data /data/ && chmod -R u+w /data/

ADD crontab /etc/cron.d/jirafeau-cron
RUN chmod 0644 /etc/cron.d/jirafeau-cron 

EXPOSE 80

VOLUME /data

