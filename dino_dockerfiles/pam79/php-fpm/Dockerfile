FROM php:7.4.1-fpm
LABEL maintainer="Paapa Abdullah Morgan <paapaabdullahm@gmail.com>"

# Install persistent build dependencies
RUN set -eux; apt update; apt install -y --no-install-recommends \
    aspell-en \
    curl \
    file \
    ghostscript \
    libc6 \
    libcurl4 \
    libgmp10 \
    libsqlite3-0 \
    libyaml-0-2 \
    libzstd1 \
    mariadb-client \
    pkg-config \
    re2c \
    ucf \
    wget \
    tidy \
    zip; \
    rm -rf /var/lib/apt/lists/*

# Install ephemeral build dependencies
RUN set -ex; savedAptMark="$(apt-mark showmanual)"; \
    apt update; apt install -y --no-install-recommends \
    libc-client-dev \
    libcurl4-openssl-dev \
    libfreetype6-dev \
    libgmp-dev \
    libicu-dev \
    libjpeg-dev \
    libkrb5-dev \
    libldap2-dev \
    libldb-dev \
    libmagickwand-dev \
    libmcrypt-dev \
    libmhash-dev \
    libonig-dev \
    libpng-dev \
    libpq-dev \
    libpspell-dev \
    libsqlite3-dev \
    libssl-dev \
    libtidy-dev \
    libwebp-dev \
    libxml2-dev \
    libxpm-dev \
    libxslt-dev \
    libyaml-dev \
    libzip-dev \
    libzstd-dev; \
    #
    # Configure php extensions
    PHP_OPENSSL=yes \
    docker-php-ext-configure imap --with-kerberos --with-imap-ssl; \
    docker-php-ext-configure gd --with-freetype --with-jpeg; \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu; \
    docker-php-ext-configure bcmath --enable-bcmath; \
    docker-php-ext-configure calendar --enable-calendar; \
    docker-php-ext-configure curl --with-curl; \
    docker-php-ext-configure ftp --enable-ftp; \
    docker-php-ext-configure gettext --with-gettext; \
    docker-php-ext-configure gmp --with-gmp; \
    docker-php-ext-configure intl --enable-intl; \
    docker-php-ext-configure pdo_mysql --with-pdo-mysql; \
    docker-php-ext-configure pdo_pgsql --with-pdo-pgsql; \
    docker-php-ext-configure pspell --with-pspell; \
    docker-php-ext-configure mbstring --enable-mbstring; \
    docker-php-ext-configure shmop --enable-shmop; \
    docker-php-ext-configure soap --enable-soap; \
    docker-php-ext-configure sockets --enable-sockets; \
    docker-php-ext-configure sysvmsg --enable-sysvmsg; \
    docker-php-ext-configure sysvsem --enable-sysvsem; \
    docker-php-ext-configure sysvshm --enable-sysvshm; \
    docker-php-ext-configure tidy --with-tidy; \
    docker-php-ext-configure xmlrpc --with-xmlrpc; \
    docker-php-ext-configure xsl --with-xsl; \
    #
    # Install php extensions
    docker-php-ext-install -j "$(nproc)" \
    bcmath \
    calendar \
    ctype \
    curl \
    exif \
    ftp \
    gd \
    gettext \
    gmp \
    imap \
    intl \
    ldap \
    mbstring \
    mysqli \
    opcache \
    pdo \
    pdo_mysql \
    pdo_pgsql \
    pdo_sqlite \
    pspell \
    shmop \
    soap \
    sockets \
    sysvmsg \
    sysvsem \
    sysvshm \
    tidy \
    xmlrpc \
    xsl \
    zip ; \
    #
    # Install and enable redis dependency via pecl
    yes | pecl install igbinary; docker-php-ext-enable igbinary; \
    #
    # Install and enable other php extensions via pecl
    yes | pecl install imagick-3.4.4 yaml-2.0.4 xdebug mongodb redis; \
    docker-php-ext-enable imagick yaml xdebug mongodb redis; \
    #
    # Reset apt-mark
    apt-mark auto '.*' > /dev/null; \
    apt-mark manual $savedAptMark; \
    ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
        | awk '/=>/ { print $3 }' \
        | sort -u \
        | xargs -r dpkg-query -S \
        | cut -d: -f1 \
        | sort -u \
        | xargs -rt apt-mark manual; \
    #
    # Remove all build dependencies
    apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    rm -rf /var/lib/apt/lists/*; pecl update-channels; rm -rf /tmp/pear ~/.pearrc; \
    #
    # Smoke test
    php -m

# Set recommended opcache php.ini settings
RUN { \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=4000'; \
    echo 'opcache.revalidate_freq=2'; \
    echo 'opcache.fast_shutdown=1'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini

# Configure-error-logging
RUN { \
    echo 'error_reporting = E_ERROR | E_WARNING | E_PARSE | E_CORE_ERROR | E_CORE_WARNING | E_COMPILE_ERROR | E_COMPILE_WARNING | E_RECOVERABLE_ERROR'; \
    echo 'display_errors = Off'; \
    echo 'display_startup_errors = Off'; \
    echo 'log_errors = On'; \
    echo 'error_log = /dev/stderr'; \
    echo 'log_errors_max_len = 1024'; \
    echo 'ignore_repeated_errors = On'; \
    echo 'ignore_repeated_source = Off'; \
    echo 'html_errors = Off'; \
} > /usr/local/etc/php/conf.d/error-logging.ini

# Set usermod
RUN usermod -u 1000 www-data;

VOLUME /var/www/html
EXPOSE 9000
CMD ["php-fpm"]
