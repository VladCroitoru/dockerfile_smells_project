#####################################################
# Dockerfile to customeize PHP for Laravel project
# Based on the official PHP-FPM 7.4
#####################################################

# Set the base image
FROM        php:7.4-fpm

# File Author / Maintainer
LABEL       maintainer=info@adiwit.co.th

# Environmental Variables
ARG         DEBIAN_FRONTEND=noninteractive

# Change System TimeZone to Asia/Bangkok
RUN         apt-get update --fix-missing \
    && apt-get upgrade -fy \
    && apt-get dist-upgrade -fy \
    && apt-get install --no-install-recommends --fix-missing -fy \
    locales \
    && printf "th_TH.UTF-8 UTF-8\nen_US UTF-8\nen_US.UTF-8 UTF-8\n" > /etc/locale.gen \
    && locale-gen \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/Asia/Bangkok /etc/localtime

# Update Repositories
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    apt-transport-https \
    apt-utils \
    autoconf \
    git \
    pkg-config \
    rsync \
    wget \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# BZ2
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    bzip2 \
    bzip2-doc \
    libbz2-dev \
    && docker-php-ext-install bz2 \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# GD
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    libfreetype6-dev \
    libjpeg-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    && docker-php-ext-configure gd \
    --with-jpeg=/usr/include \
    --with-freetype=/usr/include/freetype2 \
    && docker-php-ext-install gd \
    && docker-php-ext-enable gd  \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# GetText
RUN         docker-php-ext-install gettext \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# MCrypt
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    libmcrypt-dev \
    && pecl install --onlyreqdeps --force mcrypt \
    && docker-php-ext-enable mcrypt \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# Memcached
# RUN         apt-get update --fix-missing \
#     && apt-get install --no-install-recommends --fix-missing -fy \
#     libmemcached-dev \
#     zlib1g-dev \
#     && doNotUninstall=" \
#     libmemcached11 \
#     libmemcachedutil2 \
#     " \
#     && rm -r /var/lib/apt/lists/* \
#     && docker-php-source extract \
#     && git clone https://github.com/php-memcached-dev/php-memcached /usr/src/php/ext/memcached/ \
#     && docker-php-ext-install memcached \
#     && apt-mark manual $doNotUninstall \
#     && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $buildDeps \
#     && apt-get autoremove -fy \
#     && apt-get clean \
#     && apt-get autoclean -y \
#     && docker-php-source delete \
#     && rm -rf /var/lib/apt/lists/*

# MySQL
RUN         docker-php-ext-install mysqli \
    pdo pdo_mysql \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# PostgreSQL
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    libpq-dev \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install pdo pdo_pgsql pgsql \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# Redis
RUN         pecl channel-update pecl.php.net \
    && pecl install --onlyreqdeps --force redis \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable redis

# SQL Server
# ENV         ACCEPT_EULA=Y
# RUN         apt-get update --fix-missing \
#     && apt-get install --no-install-recommends --fix-missing -fy \
#     gnupg \
#     && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
#     && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql.list \
#     && apt-get update --fix-missing \
#     && apt-get install --no-install-recommends --fix-missing -fy \
#     unixodbc \
#     odbcinst1debian2 \
#     unixodbc-dev \
#     locales \
#     msodbcsql17 \
#     mssql-tools \
#     && printf "th_TH.UTF-8 UTF-8\nen_US UTF-8\nen_US.UTF-8 UTF-8\n" > /etc/locale.gen \
#     && locale-gen \
#     && pecl install sqlsrv \
#     && pecl install pdo_sqlsrv \
#     && docker-php-ext-enable \
#     sqlsrv.so \
#     pdo_sqlsrv.so \
#     && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
#     && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
#     && apt-get autoremove -fy \
#     && apt-get clean \
#     && apt-get autoclean -y \
#     && docker-php-source delete \
#     && rm -rf /var/lib/apt/lists/*

# Zip
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    libzip-dev \
    zip \
    unzip \
    && docker-php-ext-install zip \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# PDF
# RUN         apt-get update --fix-missing \
#     && apt-get install --no-install-recommends --fix-missing -fy \
#     libthai0 \
#     xfonts-thai \
#     pdftk \
#     libxrender1 \
#     libfontconfig1 \
#     libxtst6 \
#     libx11-dev \
#     libjpeg62 \
#     && wget https://github.com/h4cc/wkhtmltopdf-amd64/blob/master/bin/wkhtmltopdf-amd64?raw=true --no-verbose -O /usr/local/bin/wkhtmltopdf \
#     && chmod +x /usr/local/bin/wkhtmltopdf \
#     && rm -rf /var/lib/apt/lists/* \
#     && apt-get autoremove -fy \
#     && apt-get clean \
#     && apt-get autoclean -y

# IMAP
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    libc-client-dev \
    libkrb5-dev \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install imap \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# BCMATH
RUN         docker-php-ext-configure bcmath \
    && docker-php-ext-install bcmath \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# ActiveDirectory / LDAP
# RUN         apt-get update --fix-missing \
#     && apt-get install --no-install-recommends --fix-missing -fy \
#     libldap2-dev -y \
#     && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
#     && docker-php-ext-install ldap \
#     && apt-get autoremove -fy \
#     && apt-get clean \
#     && apt-get autoclean -y \
#     && docker-php-source delete \
#     && rm -rf /var/lib/apt/lists/*

# Graphviz
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    graphviz \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

# Calendar
RUN         docker-php-ext-configure calendar \
    && docker-php-ext-install calendar \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && docker-php-source delete \
    && rm -rf /var/lib/apt/lists/*

# Intl
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    libicu-dev \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

# EXIF
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    libicu-dev \
    && docker-php-ext-configure exif \
    && docker-php-ext-install exif \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

# IGBINARY
RUN         pecl install --onlyreqdeps --force igbinary \
    && docker-php-ext-enable igbinary

# XDEBUG
# Xdebug can cause Composer to take minutes even when running a command as simple as composer --version
# RUN         pecl install --onlyreqdeps --force xdebug \
#     && apt-get autoremove -fy \
#     && apt-get clean \
#     && apt-get autoclean -y \
#     && docker-php-source delete \
#     && rm -rf /var/lib/apt/lists/*

# SSH
RUN         apt-get update --fix-missing \
    && apt-get install --no-install-recommends --fix-missing -fy \
    openssh-client \
    && apt-get autoremove -fy \
    && apt-get clean \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

# Composer
RUN         wget https://getcomposer.org/installer -O - -q | php -- --no-ansi --install-dir=/usr/bin --filename=composer \
    && composer config --global repo.packagist composer https://packagist.org \
    # && composer global require laravel/installer \
    && composer global require phpunit/phpunit \
    && composer global require squizlabs/php_codesniffer \
    && composer global require beyondcode/laravel-self-diagnosis dev-master \
    && composer global require beyondcode/laravel-er-diagram-generator dev-master --ignore-platform-reqs \
    && export PATH="~/.composer/vendor/bin:$PATH" \
    && mkdir -p /root/.ssh \
    && echo "StrictHostKeyChecking no" > /root/.ssh/config

# Configurations
COPY        php.ini /usr/local/etc/php/php.ini
COPY        zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf