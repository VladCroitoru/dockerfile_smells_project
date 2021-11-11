FROM php:5.6-apache
MAINTAINER Jesús Urrutia <jesus.urrutia@gmail.com>
# Install Git
RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y nodejs npm
# Install bower
RUN npm -g install bower
# Install composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer
EXPOSE 80
COPY config/php.ini /usr/local/etc/php/
COPY entrypoint.sh /var/www/
WORKDIR /var/www/
CMD ["bash", "/var/www/entrypoint.sh"]