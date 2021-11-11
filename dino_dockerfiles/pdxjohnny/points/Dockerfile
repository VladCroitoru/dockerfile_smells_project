FROM php:7.0-apache

ARG DEPS_DIR=deps
ARG SRC_DIR=/var/www/html
ARG LIB_DIR=/var/www/lib

COPY composer.json /var/www/

RUN docker-php-ext-install -j$(nproc) pdo_mysql && \
    cd /var/www && \
    apt-get update && \
    apt-get -y install git unzip && \
    curl -sS https://getcomposer.org/installer | php && \
    php composer.phar install && \
    apt-get -y purge git && \
    apt-get -y autoremove && \
    rm composer.phar

ADD https://code.jquery.com/jquery-2.2.3.min.js $SRC_DIR/$DEPS_DIR/jquery/jquery.min.js
ADD https://github.com/Semantic-Org/Semantic-UI-CSS/raw/master/dist.zip $SRC_DIR/$DEPS_DIR/semantic/s.zip

RUN cd $SRC_DIR/$DEPS_DIR/semantic && \
    unzip -o s.zip && \
    rm s.zip

COPY src $SRC_DIR/
COPY lib $LIB_DIR/
