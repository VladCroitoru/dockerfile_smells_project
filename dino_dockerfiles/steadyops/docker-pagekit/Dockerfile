FROM php:7.2.1-cli-alpine3.7

ENV PAGEKIT_VERSION=1.0.13

# install dependencies via apk
RUN apk update && apk add  wget unzip zlib-dev

# install php-zip
RUN docker-php-ext-install -j$(nproc) zip

RUN mkdir /var/www/ \
    && mkdir /var/www/html \
    && cd /var/www/html \
    && wget -q --show-progress https://github.com/pagekit/pagekit/releases/download/$PAGEKIT_VERSION/pagekit-$PAGEKIT_VERSION.zip \
    && unzip pagekit-$PAGEKIT_VERSION.zip


WORKDIR /var/www/html

CMD ["php", "-S", "0.0.0.0:10000"]

EXPOSE  10000
