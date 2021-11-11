FROM alpine:edge
MAINTAINER Tim Stallmann <tim@savaslabs.com>
# original MAINTAINER Dmytro Shavaryn <shavarynd@gmail.com>

# Install PHP7 with needed exstentions and composer.
RUN apk add --update \
    php7-dom \
    php7-curl \
    php7-json \
    php7-phar \
    php7-openssl \
    php7-mbstring \
    php7-ctype \
    php7-pdo_mysql \
    php7-session \
    curl \
    && rm -fr /var/cache/apk/* \
    && ln -s /usr/bin/php7 /usr/bin/php \
    && curl -sS https://getcomposer.org/installer | php -- --filename=composer \
    --install-dir=/usr/bin --version=1.0.0 \

WORKDIR /srv
# Add files and folders to container.
ADD ["composer.json", "entrypoint.sh", "./"]
# Install and initialize Behat.
RUN composer install \
    && bin/behat --init

ENTRYPOINT ["./entrypoint.sh"]
CMD ["--format=pretty", "--out=std"]
