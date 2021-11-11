FROM registry.gitlab.com/rust_musl_docker/image:stable-latest AS build
ENV PARSER_VERSION c2fe8ec
WORKDIR /root/build
RUN git clone https://github.com/demostf/parser
WORKDIR /root/build/parser
RUN git checkout $PARSER_VERSION
RUN cargo build --release --target=x86_64-unknown-linux-musl

FROM icewind1991/php-alpine-apcu

COPY --from=build /root/build/parser/target/x86_64-unknown-linux-musl/release/parse_demo /app/parse_demo
COPY composer.json composer.lock /app/

RUN apk add --no-cache git \
    && wget https://getcomposer.org/composer.phar \
    && php composer.phar --working-dir=/app install --no-dev --no-interaction --ignore-platform-reqs \
    && rm composer.phar \
    && apk del git

COPY src /app/src

ENV PARSER_PATH /app/parse_demo

RUN echo "clear_env = no" >> /usr/local/etc/php/php-fpm.conf \
    && echo "post_max_size = 150M" >> /usr/local/etc/php/php.ini \
    && echo "upload_max_filesize = 150M" >> /usr/local/etc/php/php.ini
