FROM ubuntu:14.04
ADD . /code

RUN apt-get update && apt-get install -y curl php5
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
RUN mv /usr/bin/composer.phar /usr/bin/composer
RUN composer 
RUN cd /code && composer require silex/silex v1.2.4
RUN ls /code

EXPOSE 8080

CMD php -S 0.0.0.0:8080 -t /code/web
