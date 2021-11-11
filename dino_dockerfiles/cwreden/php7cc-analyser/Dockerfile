FROM php:7.1

LABEL maintainer="christian@wreden.eu"

WORKDIR "/opt"

ENV version=1.1.8

ADD https://github.com/cwreden/php7cc-analyser/releases/download/$version/php7cc-analyser.phar /usr/local/bin/php7cc-analyser

RUN chmod +x /usr/local/bin/php7cc-analyser
