FROM php:7.1.5-apache

RUN apt-get update && \
    apt-get install unzip && \
    apt-get clean

RUN curl -L -O https://github.com/Studio-42/elFinder/archive/2.1.25.zip && \
    unzip *.zip && \
    rm -f *.zip

RUN mv elFinder-* elFinder && \
    chown -R www-data:www-data elFinder && \
    mv elFinder/php/connector.minimal.php-dist elFinder/php/connector.minimal.php && \
    rm -rf elFinder/files && \
    ln -s /data ./elFinder/files && \
    mv elFinder/* . && \
    rm -rf elFinder && \
    mv elfinder.html index.html

RUN mkdir /config && \
    rm php/connector.minimal.php && \
    ln -s /config/connector.php php/connector.minimal.php 

COPY connector.php /config/connector.php

VOLUME /data
