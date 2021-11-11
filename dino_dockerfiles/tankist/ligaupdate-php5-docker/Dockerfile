FROM php:5-apache

RUN set -xe && a2enmod rewrite && service apache2 restart

RUN set -xe && \
    commonDeps=" \
        libmcrypt-dev \
        libxml2-dev \
        zlib1g-dev \
    " && \
    apt-get update && \
    apt-get install -y libmcrypt4 --no-install-recommends && \
    apt-get install -y $commonDeps --no-install-recommends && \
    docker-php-ext-install pdo_mysql mysqli mcrypt opcache soap zip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $commonDeps

RUN set -xe && imagickDeps=" \
        libgd-dev \
        libmagickwand-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
    " && \
    apt-get update && \
    apt-get install -y libgd3 libmagickwand-6.q16-2 imagemagick --no-install-recommends && \
    apt-get install -y $imagickDeps --no-install-recommends && \
    NPROC=$(getconf _NPROCESSORS_ONLN) && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j${NPROC} gd && \
    pecl install imagick && \
    docker-php-ext-enable imagick && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $imagickDeps

RUN set -xe && \
    mongoDeps=" \
            libcurl4-openssl-dev \
            pkg-config \
            libssl-dev \
        " && \
    apt-get update && \
    apt-get install -y $mongoDeps libcurl3 --no-install-recommends && \
    pecl install mongodb && \
    docker-php-ext-enable mongodb && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $mongoDeps && \
    ldconfig

RUN set -xe && \
    zmqDeps="git curl wget build-essential uuid-dev libsodium-dev pkg-config" && \
    apt-get update && \
    apt-get install -y $zmqDeps && \
    cd /tmp &&  wget http://download.zeromq.org/zeromq-4.1.2.tar.gz && tar -xvf zeromq-4.1.2.tar.gz && cd zeromq-4.1.2 && ./configure && make && make install && ldconfig -v && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $zmqDeps

RUN set -xe && \
    chown www-data:www-data /var/www/html -R
