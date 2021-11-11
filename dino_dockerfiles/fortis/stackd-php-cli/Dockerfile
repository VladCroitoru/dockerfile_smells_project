FROM alpine:edge
MAINTAINER Alan Bondarchuk <imacoda@gmail.com>

# Install packages
RUN echo 'http://alpine.gliderlabs.com/alpine/edge/main' > /etc/apk/repositories && \
    echo 'http://alpine.gliderlabs.com/alpine/edge/community' >> /etc/apk/repositories && \
    echo 'http://alpine.gliderlabs.com/alpine/edge/testing' >> /etc/apk/repositories && \

    apk add --update \
        unzip \
        php7 \
        php7-pcntl \
        php7-json \
        php7-ctype \
        php7-session \
        php7-dom \
        php7-xml \
        php7-mcrypt \
        php7-phar \
        php7-iconv \
        php7-openssl \
        php7-zip \
        php7-zlib \
        php7-curl \
        php7-pdo \
        php7-pdo_mysql \
        php7-mysqli \
        && \

    # Create symlinks for backward compatibility
    ln -sf /usr/bin/php7 /usr/bin/php && \

    # Cleanup
    apk del --purge \
        *-dev \
        build-base \
        autoconf \
        libtool \
        openssl \
        && \

    rm -rf \
        /usr/include/php \
        /usr/lib/php/build \
        /var/cache/apk/* \
        /tmp/*

WORKDIR /var/www/html
VOLUME /var/www/html

# Command
CMD ["php", "-a"]
