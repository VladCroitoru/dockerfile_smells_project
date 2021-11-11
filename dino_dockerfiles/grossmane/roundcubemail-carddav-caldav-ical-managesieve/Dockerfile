FROM alunduil/roundcube:1.2.3

#ENV http_proxy http://proxy:8080
#ENV https_proxy http://proxy:8080

COPY config.inc.php /var/www/config/config.inc.php
COPY plugins/carddav /var/www/plugins/carddav
COPY plugins/calendar /var/www/plugins/calendar
COPY plugins/libcalendaring /var/www/plugins/libcalendaring
COPY plugins/managesieve  /var/www/plugins/managesieve
COPY plugins/password/config.inc.php  /var/www/plugins/password/config.inc.php

COPY vendor /var/www/vendor

RUN apt-get update
RUN apt-get -y install curl sudo php5-curl php5-mcrypt git vim
COPY composer-installer /root/installer
RUN cat /root/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN cd /var/www/plugins/calendar/lib/ && \
#    composer remove fkooman/oauth-client sabre/dav sabre/vobject 
    rm -rf vendor && \
    composer install
#    composer require sabre/vobject 2.1.x-dev && \
#    composer require sabre/dav 1.8.12 && \
#    composer require sabre/http 2.0.0 && \
#    composer require fkooman/oauth-client

#ENV http_proxy=""
#ENV https_proxy=""
