FROM composer/composer:latest

MAINTAINER Toby <t.post@hotmail.com>

WORKDIR /

ADD ./entrypoint.sh /entrypoint.sh

VOLUME /builds

ENTRYPOINT ["/entrypoint.sh"]

# docker run --rm --tty -v $(pwd)/builds:/builds toby1991/laravel-release:latest
