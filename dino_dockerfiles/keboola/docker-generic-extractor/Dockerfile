# VERSION 1.6.15
FROM php:7.0
RUN apt-get update -q && apt-get install unzip git -y
RUN cd \
  && curl -sS https://getcomposer.org/installer | php \
  && ln -s /root/composer.phar /usr/local/bin/composer

MAINTAINER Ondrej Vana <ondrej.vana@keboola.com>

WORKDIR /home

# Initialize
COPY php.ini /usr/local/etc/php/
RUN git clone https://github.com/keboola/generic-extractor.git ./
RUN git checkout tags/0.7.1
RUN composer install --no-interaction --no-dev

ENTRYPOINT php ./run.php --data=/data
