FROM php:7-alpine

RUN apk add --no-cache bzip2-dev \
    && docker-php-ext-install bz2

RUN curl -L http://static.phpmd.org/php/latest/phpmd.phar \
    -o /usr/local/bin/phpmd \
    && chmod +x /usr/local/bin/phpmd

RUN mkdir -p /workspace
COPY ./ruleset.xml /
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
WORKDIR /workspace

ENTRYPOINT ["/entrypoint.sh"]
CMD ["--help"]
