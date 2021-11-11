FROM php:7.1-alpine

LABEL maintainer="Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>"

ENV QUEUE_CONNECTION=sqs
ENV QUEUE_NAME=default

# Install some dependenties
RUN set -ex && \
    apk add --no-cache --virtual .build-deps \
    $PHPIZE_DEPS \
    freetype-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    zlib-dev

# Install pdo if you want to use database queue
RUN docker-php-ext-install pdo pdo_mysql pcntl posix gd zip

ENV PYTHON_VERSION=2.7.15-r2
ENV PY_PIP_VERSION=10.0.1-r0
ENV SUPERVISOR_VERSION=3.3.3

# Install supervisor
RUN apk update && apk add -u python=$PYTHON_VERSION py-pip=$PY_PIP_VERSION
RUN pip install supervisor==$SUPERVISOR_VERSION

ENV PHPREDIS_VERSION 4.0.1

# Install PHP Redis
RUN mkdir -p /usr/src/php/ext/redis \
    && curl -L https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar xvz -C /usr/src/php/ext/redis --strip 1 \
    && echo 'redis' >> /usr/src/php-available-exts \
    && docker-php-ext-install redis

RUN apk add --no-cache libssl1.0
RUN apk add --no-cache --virtual openssl-dev

RUN pecl install mongodb && \
    docker-php-ext-enable mongodb

ADD supervisord.conf /etc/supervisord.conf

# Copy scripts
COPY start.sh /usr/local/bin/start.sh

# Run supervisor
CMD ["/usr/local/bin/start.sh"]