FROM php:7.1-cli

# Environmental Variables
ENV COMPOSER_HOME /root/composer
ENV COMPOSER_VERSION master

RUN set -xe \
    && apt-get update \
    && apt-get install -y zip zlib1g-dev git \
    && docker-php-ext-install \
        zip bcmath \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer global require hirak/prestissimo \
    && composer global require wikimedia/composer-merge-plugin

COPY . /usr/src/myapp
WORKDIR /usr/src/myapp

EXPOSE 8888

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["composer install -vvv && php -S 0.0.0.0:8888"]
