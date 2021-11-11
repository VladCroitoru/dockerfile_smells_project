FROM php:fpm

ENV NODE_PATH /usr/lib/node_modules
ENV BEHAT_PARAMS='{"extensions" : {"Behat\\MinkExtension" : {"base_url" : "http://test"}}}'
ENV TERM="xterm"
ENV COMPOSER_ALLOW_SUPERUSER=1

MAINTAINER Jeremy Jumeau <jumeau.jeremy@gmail.com>

# PHP extensions
RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        git \
        libicu-dev \
        libldap2-dev \
        libmagickwand-dev \
        libmcrypt-dev \
        libssl-dev \
        zlib1g-dev \
    && pecl install mongodb \
    && pecl install imagick-beta \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install \
        intl \
        ldap \
        mbstring \
        mcrypt \
        opcache \
        sockets \
        zip \
    && docker-php-ext-enable \
        mongodb \
        imagick \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Composer
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');" \
    && mkdir -p /var/.composer \
    && composer global --no-interaction --working-dir=/var/.composer require symfony/var-dumper

# Wkhtmltopdf
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libxrender-dev \
        xz-utils \
    && curl -LO https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && cp wkhtmltox/bin/wkhtmltopdf /usr/local/bin/ \
    && cp wkhtmltox/bin/wkhtmltoimage /usr/local/bin/ \
    && rm -R wkhtmltox* \
    && apt-get remove -y xz-utils libxrender-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Node
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get update \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends yarn \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Gulp / Zombie.js
RUN yarn global add gulp zombie
