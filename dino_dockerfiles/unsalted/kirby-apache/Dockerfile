FROM php:7.0-apache

ENV COMPOSER_HOME $HOME/.composer

RUN mkdir -p $COMPOSER_HOME/vendor/bin

# Allow modrewrite
RUN a2enmod rewrite

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        git \
        less \
        nano \
        vim \
        unzip \
        libzip-dev \
        && docker-php-ext-install zip


# download and check composer (may need to update hash in future)
RUN curl -sSL https://getcomposer.org/installer | \
    php -- --install-dir=$COMPOSER_HOME/vendor/bin --filename=composer

# add composer vendors to path
ENV PATH vendor/bin:$COMPOSER_HOME/vendor/bin:$PATH

# install kirby-cli
RUN composer global require getkirby/cli

WORKDIR /var/www/html/

VOLUME ["/var/www/html/"]

EXPOSE 80


