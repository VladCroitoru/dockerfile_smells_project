FROM php:apache-buster

# app version, set with docker build --build-arg version=v0.0.2
ARG proxy_address

RUN  echo "deb [trusted=yes] http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/debian.org buster main" > /etc/apt/sources.list \
     && echo "deb [trusted=yes] http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/debian.org buster-updates main" >> /etc/apt/sources.list \
     && echo "deb [trusted=yes] http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/debian-security buster/updates main" >> /etc/apt/sources.list \
     && apt-get update

# 1. development packages
RUN apt-get install -y \
    git \
    pkg-config \
    libcurl4-openssl-dev \
    curl \
    wget \
    libicu-dev \
    libbz2-dev \
    libpng-dev \
    libjpeg-dev \
    libmcrypt-dev \
    libreadline-dev \
    libfreetype6-dev \
    libssl-dev \
    g++ \
    zip \
    zlib1g-dev \
    libzip-dev \
    unzip \
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install zip
ENV NODE_VERSION 15.6.0
ENV NVM_DIR /usr/local/nvm
ENV https_proxy $proxy_address
RUN mkdir -p $NVM_DIR && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash

# install node and npm
RUN . $NVM_DIR/nvm.sh \
     && nvm install $NODE_VERSION \
     && nvm alias default $NODE_VERSION \
     && nvm use default

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
RUN npm config set registry http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/api/npm/npm/

# 2. apache configs + document root
ENV APACHE_DOCUMENT_ROOT=/var/www/html/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf && \
    sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf && \
    sed -i 's/Require local/#Require local/g' /etc/apache2/mods-available/status.conf

# 3. mod_rewrite for URL rewrite and mod_headers for .htaccess extra headers like Access-Control-Allow-Origin-
RUN a2enmod rewrite headers

# 4. start with base php config, then add extensions. CA Bundle for https requests
RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini" && \
    sed -i 's/;curl.cainfo =/curl.cainfo=\/var\/www\/html\/trusted-ca-bundle.pem/g' $PHP_INI_DIR/php.ini && \
    docker-php-ext-install exif sockets

RUN useradd -G www-data,root -u 1000 -d /home/devuser devuser
ENV COMPOSER_HOME /home/devuser/.composer
RUN mkdir -p $COMPOSER_HOME
# 5. composer
ENV PATH ./vendor/bin:/composer/vendor/bin:$PATH
ENV COMPOSER_ALLOW_SUPERUSER 1
COPY installer .
RUN php installer --install-dir=/usr/local/bin/ --filename=composer --disable-tls

# so when we execute CLI commands, all the host file's ownership remains intact
# otherwise command from inside container will create root-owned files and directories
COPY config.json $COMPOSER_HOME
RUN chown -R devuser:devuser /home/devuser
RUN composer config --global home
COPY . /var/www/html/
RUN chown -R devuser /var/www/html/*

# Setup working directory
WORKDIR /var/www/html
# Install dependencies, run npm, patch apache start script to reload php config
RUN cd /var/www/html && \
    composer update && \
    composer install --optimize-autoloader --no-dev && \
    touch /var/www/html/.env && echo "APP_KEY=" > .env && php artisan key:generate && \
    php artisan route:cache && php artisan view:cache && php artisan config:cache && \
    composer dump-autoload
USER devuser
RUN npm config set registry http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/api/npm/npm/
RUN npm install  && \
    npm run production
USER root
RUN sed -i '/^exec.*/i php artisan config:cache' /usr/local/bin/apache2-foreground
