FROM ubuntu:16.04

MAINTAINER andmetoo <hello@notme.pw>

# Use baseimage-docker's init system.
#CMD ["/sbin/my_init"]

# Set correct environment variables
ENV HOME /root

# MYSQL ROOT PASSWORD
ARG MYSQL_ROOT_PASS=root    

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    locales \
    software-properties-common \
    python-software-properties \
    build-essential \
    curl \
    git \
    unzip \
    mcrypt \
    wget \
    openssl \
    autoconf \
    openssh-client \
    g++ \
    make \
    libssl-dev \
    libcurl4-openssl-dev \
    libsasl2-dev \
    libcurl3 \
    --no-install-recommends && rm -r /var/lib/apt/lists/* \
    && apt-get --purge autoremove -y

# Ensure UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
RUN locale-gen en_US.UTF-8

# OpenSSL
RUN mkdir -p /usr/local/openssl/include/openssl/ && \
    ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \
    mkdir -p /usr/local/openssl/lib/ && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/

RUN mkdir /root/.ssh/

RUN chmod 700 /root/.ssh/

# NODE JS
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install nodejs -qq && \
    npm install -g gulp-cli 

# MYSQL
# /usr/bin/mysqld_safe
RUN bash -c 'debconf-set-selections <<< "mysql-server-5.7 mysql-server/root_password password $MYSQL_ROOT_PASS"' && \
		bash -c 'debconf-set-selections <<< "mysql-server-5.7 mysql-server/root_password_again password $MYSQL_ROOT_PASS"' && \
		DEBIAN_FRONTEND=noninteractive apt-get update && \
		DEBIAN_FRONTEND=noninteractive apt-get install -qqy mysql-server-5.7	

RUN rm -rf /etc/mysql/mysql.conf.d/disable_strict_mode.cnf && \
    touch /etc/mysql/mysql.conf.d/disable_strict_mode.cnf && \
    echo "[mysqld] \n sql_mode=IGNORE_SPACE,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION" >> /etc/mysql/mysql.conf.d/disable_strict_mode.cnf

# PHP Extensions
RUN add-apt-repository -y ppa:ondrej/php && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y -qq php-pear \
      php7.0-dev \
      php7.0-cli \
      php7.0-fpm \
      php7.0-apcu \
      php7.0-bcmath \
      php7.0-bz2 \
      php7.0-calendar \
      php7.0-common \
      php7.0-ctype \
      php7.0-curl \
      php7.0-dba \
      php7.0-dom \
      php7.0-embed \
      php7.0-enchant \
      php7.0-exif \
      php7.0-fpm \
      php7.0-ftp \
      php7.0-gd \
      php7.0-gettext \
      php7.0-gmp \
      php7.0-iconv \
      php7.0-imagick \
      php7.0-imap \
      php7.0-intl \
      php7.0-json \
      php7.0-ldap \
      php7.0-libsodium \
      php7.0-mbstring \
      php7.0-mcrypt \
      php7.0-memcached \
      php7.0-mongodb \
      php7.0-mysqli \
      php7.0-mysqlnd \
      php7.0-odbc \
      php7.0-opcache \
#      php7.0-openssl \
      php7.0-pdo \
      php7.0-pgsql \
      php7.0-phar \
      php7.0-phpdbg \
      php7.0-posix \
      php7.0-pspell \
      php7.0-redis \
      php7.0-shmop \
      php7.0-snmp \
      php7.0-soap \
      php7.0-sockets \
      php7.0-sqlite3 \
      php7.0-sysvmsg \
      php7.0-sysvsem \
      php7.0-sysvshm \
      php7.0-tidy \
      php7.0-tokenizer \
      php7.0-wddx \
      php7.0-xdebug \
      php7.0-xml \
      php7.0-xmlreader \
      php7.0-xmlrpc \
      php7.0-xmlwriter \
      php7.0-xsl \
      php7.0-zip 

# Time Zone
RUN echo "date.timezone = UTC" > /etc/php/7.0/cli/conf.d/date_timezone.ini && \
    echo "date.timezone = UTC" > /etc/php/7.0/fpm/conf.d/date_timezone.ini

VOLUME /root/composer

# Environmental Variables
ENV COMPOSER_HOME /root/composer

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Goto temporary directory.
WORKDIR /tmp

# Codecept Support
RUN wget http://codeception.com/codecept.phar && \
    chmod +x codecept.phar && \
    mv codecept.phar /usr/local/bin/codecept

# Deployer
RUN wget http://deployer.org/deployer.phar -o deployer.phar && \
    mv deployer.phar /usr/local/bin/dep && \
    chmod +x /usr/local/bin/dep

RUN apt-get clean -y && \
        apt-get autoremove -y && \
		rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
