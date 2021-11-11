FROM php:7.1

LABEL maintainer="christian@wreden.eu"

WORKDIR "/analyser"

ADD http://get.sensiolabs.org/security-checker.phar /usr/local/bin/security-checker

RUN chmod +x /usr/local/bin/security-checker