FROM php:5.6.25-apache

ENV TIMEZONE="America/Los_Angeles"

RUN mkdir -p /opt/ebot/demos /opt/ebot/logs && a2enmod rewrite && \
    docker-php-ext-install pdo_mysql && \
    echo 'date.timezone = "${TIMEZONE}"' >> /usr/local/etc/php/conf.d/php.ini && \
    apt-get update && apt-get -y install zip netcat && \
    apt-get clean && \
    rm -rf /var/www/html/* && \
    curl -L https://github.com/TheShockTop/eBot-CSGO-Web/archive/master.zip >> /tmp/master.zip && \
    unzip -d /var/www/html /tmp/master.zip && \
    rm -rf /tmp/* && \
    mv /var/www/html/eBot-CSGO-Web-master/* /var/www/html/ &&\
    rm -rf /var/www/html/eBot-CSGO-Web-master /var/www/html/web/installation && \
    cp /var/www/html/config/app_user.yml.default /var/www/html/config/app_user.yml && \    
    chown www-data:www-data -R /var/www /opt/ebot

RUN sed -i 's@#RewriteBase /@RewriteBase /@g' /var/www/html/web/.htaccess

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

COPY entrypoint.sh /sbin/entrypoint.sh

Run chmod +x /sbin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/sbin/entrypoint.sh"]
