FROM ubuntu:14.04

RUN apt-get update && apt-get upgrade -y && apt-get -y install apache2 php5 php5-cli curl vim supervisor  mysql-client php5-mysql libapache2-mod-auth-mysql
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN cd /var/www/html && composer require slim/slim "^3.0" && composer require palanik/corsslim  "dev-slim3" && composer require mikehaertl/phpwkhtmltopdf

RUN rm -rf /var/www/html/index.html

RUN a2enmod rewrite

ADD slim/.htaccess /var/www/html/.htaccess
ADD slim/index.php /var/www/html/api/index.php
ADD slim/slim-apache.conf /etc/apache2/sites-available/000-default.conf

ADD supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

VOLUME /var/www/html/api

EXPOSE 80
CMD ["/usr/bin/supervisord"]
