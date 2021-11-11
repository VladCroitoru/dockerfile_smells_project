FROM alpine:3.14.2 as base

# HACK: Make iconv work on Alpine + PHP8
# https://github.com/docker-library/php/issues/240#issuecomment-762763705
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.13/community/ gnu-libiconv=1.15-r3 && \
    apk add --no-cache php8 php8-phar php8-iconv php8-openssl php8-tokenizer php8-dom php8-mbstring php8-xmlwriter \
    php8-xml

FROM base as builder

WORKDIR /workdir

RUN ln -s /usr/bin/php8 /usr/bin/php && \
    wget -O /usr/bin/composer https://getcomposer.org/download/2.1.9/composer.phar && \
    chmod +x /usr/bin/composer

COPY composer.json composer.json
COPY composer.lock composer.lock
RUN composer install --no-scripts
COPY src src
COPY tests tests

RUN composer test && composer check-formatting

RUN composer install --no-dev

FROM base
WORKDIR /workdir
COPY docs /docs
RUN adduser -u 2004 -D docker && \
    chown -R docker:docker . /docs
USER docker

COPY --from=builder /workdir/vendor vendor
COPY src src

ENTRYPOINT [ "php8", "-d", "memory_limit=-1" ]

CMD [ "src/index.php" ]
