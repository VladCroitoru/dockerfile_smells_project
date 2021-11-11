FROM php:{{PHP_VERSION}}-cli-alpine
MAINTAINER JH <hello@wearejh.com>

RUN apk --update add \
    curl \
    git \
    knock \
    openssh \
    mysql-client \
    patch \
    rsync \
    libpng \
    libpng-dev \
    freetype-dev \
    jpeg \
    jpeg-dev \
    g++ \
    icu \
    icu-dev \
    libmcrypt-dev \
    libxslt-dev \
    libstdc++ \
    libgcc \
    libzip-dev \
    ruby \
    ruby-json \
    ruby-bundler \
    libsodium-dev \
    nodejs \
    npm \
    oniguruma-dev \
    yarn \
    procps \
    perl-utils \
    zlib

RUN [ $(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") -lt 74 ] \
    && docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ --with-freetype-dir=/usr/include/ \
    && docker-php-ext-configure zip --with-libzip=/usr/include/ \
    ; true

RUN [ $(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") -ge 74 ] \
    && docker-php-ext-configure gd --with-jpeg=/usr/include/ --with-freetype=/usr/include/ \
    && docker-php-ext-configure zip \
    ; true

RUN docker-php-ext-install \
    gd \
    intl \
    mbstring \
    pdo_mysql \
    xsl \
    zip \
    soap \
    bcmath \
    mysqli \
    opcache \
    pcntl \
    sockets

RUN [ $(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") -lt 72 ] \
    && docker-php-ext-install mcrypt \
    ; true

RUN [ $(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") -ge 72 ] \
    && docker-php-ext-install sodium \
    ; true

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
ENV PATH=/root/.composer/vendor/bin:$PATH

RUN composer selfupdate --{{COMPOSER_VERSION}}
RUN composer global require wearejh/m2-deploy-recipe:dev-master
RUN composer global config repositories.ci-tool vcs git@github.com:WeareJH/ci-tool.git

RUN [ $(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") -ge 72 ] \
    && composer global require wearejh/ci-tool:dev-master \
    ; true

RUN yarn global add m2-builder@4

RUN mkdir -p /root/build
WORKDIR /root/build

RUN mkdir $HOME/.ssh
COPY ./config/php.ini /usr/local/etc/php/conf.d/php-custom.ini
