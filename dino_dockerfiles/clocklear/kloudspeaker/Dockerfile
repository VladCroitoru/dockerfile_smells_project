FROM php:5-apache

RUN apt-get update && apt-get install -y unzip wget php5-pgsql php5-mysql php5-dev php5-curl php5-ldap php5-sqlite sqlite3

RUN cd /var/www/ && wget -O kloudspeaker.zip http://www.kloudspeaker.com/download/latest.php && unzip kloudspeaker.zip -d /var/www/
RUN rm -rf /var/www/html && mv /var/www/kloudspeaker/ /var/www/html

RUN wget -O TextFile.zip http://dl.bintray.com/kloudspeaker/Kloudspeaker/viewer_TextFile_1.1.zip && unzip TextFile.zip -d /var/www/html/backend/plugin/FileViewerEditor/viewers && rm TextFile.zip

ADD configuration.php /var/www/html/backend/configuration.php
ADD php.ini /usr/local/etc/php/php.ini

RUN mkdir /data
RUN chmod -R 777 /data
RUN sed 's/Example Kloudspeaker Page/Kloudspeaker/g' /var/www/html/index.html > /var/www/html/index.html.tmp && mv /var/www/html/index.html.tmp /var/www/html/index.html

RUN a2enmod rewrite 

RUN echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php

VOLUME /data

EXPOSE 80
