FROM php:7.1-fpm

ENV ACCEPT_EULA=Y
ENV DEBIAN_FRONTED=noninteractive
ENV ORACLE_HOME=/opt/oracle/instantclient_12_2/
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2/

# Get repository and install wget and vim
RUN apt-get update && apt-get install -y \
    wget \
    vim \
    git \
    unzip \
    curl \
    apt-utils \
    gnupg \
    software-properties-common \
    apt-transport-https

# Microsoft SQL Server Prerequisites
RUN wget -qO - https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && wget -qO - https://packages.microsoft.com/config/debian/9/prod.list \
        > /etc/apt/sources.list.d/mssql-release.list

# NodeJS & Yarn
RUN echo "--> Installing Yarn and NodeJS" && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    curl -sL https://deb.nodesource.com/setup_9.x | bash - && \
    apt-get install --no-install-recommends -y nodejs yarn

# Install Oracle Instantclient
RUN mkdir /opt/oracle \
    && cd /opt/oracle \
    && wget https://github.com/bumpx/oracle-instantclient/raw/master/instantclient-basic-linux.x64-12.2.0.1.0.zip \
    && wget https://github.com/bumpx/oracle-instantclient/raw/master/instantclient-sdk-linux.x64-12.2.0.1.0.zip  \
    && unzip /opt/oracle/instantclient-basic-linux.x64-12.2.0.1.0.zip -d /opt/oracle \
    && unzip /opt/oracle/instantclient-sdk-linux.x64-12.2.0.1.0.zip  -d /opt/oracle \
    && ln -s /opt/oracle/instantclient_12_2/libclntsh.so.12.1 /opt/oracle/instantclient_12_2/libclntsh.so \
    && ln -s /opt/oracle/instantclient_12_2/libclntshcore.so.12.1 /opt/oracle/instantclient_12_2/libclntshcore.so \
    && ln -s /opt/oracle/instantclient_12_2/libocci.so.12.1 /opt/oracle/instantclient_12_2/libocci.so \
    && rm -rf /opt/oracle/*.zip

# Install PHP extensions deps
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng-dev \
    zlib1g-dev \
    libicu-dev \
    g++ \
    unixodbc-dev \
    msodbcsql17 \
    mssql-tools \
    libxml2-dev \
    libaio-dev \
    libmemcached-dev \
    freetds-dev \
    libssl-dev \
    openssl \
    supervisor

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- \
        --install-dir=/usr/local/bin \
        --filename=composer

# Install PHP extensions
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && echo 'instantclient,/opt/oracle/instantclient_12_2' | pecl install oci8 \
    && docker-php-ext-configure pdo_oci --with-pdo-oci=instantclient,/opt/oracle/instantclient_12_2,12.2
RUN pecl install sqlsrv \
    && pecl install pdo_sqlsrv \
    && pecl install redis \
    && pecl install memcached \
    && pecl install apcu \
    && pecl install apcu_bc-1.0.3

RUN docker-php-ext-install \
            iconv \
            mbstring \
            intl \
            mcrypt \
            gd \
            pdo_oci \
            soap \
            sockets \
            zip \
            pcntl \
            ftp \
            mysqli \
            pdo \
            pdo_mysql \
    && docker-php-ext-enable \
            oci8 \
            sqlsrv \
            pdo_sqlsrv \
            pdo_mysql \
            redis \
            memcached \
            opcache \
            apcu --ini-name 10-docker-php-ext-apcu.ini \
            apc --ini-name 20-docker-php-ext-apc.ini

# FreeTDS
COPY ./freetds/freetds.conf /etc/freetds/freetds.conf
COPY ./freetds/locales.conf /etc/freetds/locales.conf

# Clean repository
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Permissions
RUN chown -R www-data:www-data /var/www

# Added mssql-tools bin
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

EXPOSE 9000
