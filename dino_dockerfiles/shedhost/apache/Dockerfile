FROM php:apache
RUN a2enmod rewrite vhost_alias
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    pkg-config \
    git-core \
    autoconf \
    libjpeg62-turbo-dev \
    libpng-dev \
    libcurl4-openssl-dev \
    libpq-dev \
    libmemcached-dev \
    libmemcached11 \
    libsqlite3-dev \
    libmagickwand-dev \
    imagemagick \
    subversion \
    python \
    g++ \
    curl \
    vim \
    wget \
    netcat \
    chrpath \
    sendmail
RUN docker-php-ext-install \
    iconv \
    opcache \
    curl \
    gd \
    mysqli \
    pdo \
    pdo_pgsql \
    pdo_mysql \
    pdo_sqlite \
    pgsql \
    zip

COPY scripts/ /

# install memcached
RUN bash /install-php-memcached.sh && rm /install-php-memcached.sh

# install imagick
RUN bash /install-php-imagick.sh && rm /install-php-imagick.sh

# install xdebug
RUN bash /install-php-xdebug.sh && rm /install-php-xdebug.sh

# configure sendmail
RUN bash /configure-sendmail.sh && rm /configure-sendmail.sh

# install composer
WORKDIR /tmp
RUN wget https://getcomposer.org/composer.phar
RUN mv composer.phar /bin/composer
RUN chmod 700 /bin/composer

# cleanup
RUN apt-get clean
RUN apt-get autoremove -y
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/src/*

# create base document root
RUN mkdir -p /var/shed/public
COPY /public/ /var/shed/public/

# install adminer
RUN bash /install-adminer.sh && rm /install-adminer.sh

# install webgrind
RUN bash /install-webgrind.sh && rm /install-webgrind.sh

# copy in configuration files
COPY /000-default.conf /etc/apache2/sites-enabled/000-default.conf

# copy in PHP config
COPY /php.ini /usr/local/etc/php/php.ini


# Use custom entrypoint to allow for setting apache's UID and GID
COPY docker-php-entrypoint /usr/local/bin/
ENTRYPOINT ["docker-php-entrypoint"]
CMD ["apache2-foreground"]
