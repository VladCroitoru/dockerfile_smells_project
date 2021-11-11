FROM debian:jessie
LABEL maintainer="Marvil56 APACHE+PHP+GIT <tech@marvil56.com> | Miguel Leal - Alexandre Dias - Diogo Dias"

RUN apt-get update -q

RUN apt-get install -qy \
    sudo \
    software-properties-common \
    wget \
    gnupg2 \
    apt-utils \
    apt-transport-https \
    lsb-release \
    ca-certificates \
    make \
    gcc \
    wget \
    curl \
    nano \
    vim \
    git \
    tar \
    unzip \
    nginx \
    tzdata \
    supervisor \
    mysql-client \
    libcurl4-openssl-dev \
    pkg-config \
    libsasl2-dev

RUN export LANG="en_US.UTF-8" \
    export LC_ALL="en_US.UTF-8" \
    export LANGUAGE="en_US.UTF-8" \
    export DEBIAN_FRONTED="noninteractive" \
    export NODE_VERSION="8.9.4"

RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list
RUN apt-get update -q

RUN apt-get install --no-install-recommends -qy \
    php7.2 \
    php7.2-bcmath \
    php7.2-common \
    php7.2-curl \
    php7.2-dom \
    php7.2-fpm \
    php7.2-gd \
    php7.2-iconv \
    php7.2-intl \
    php7.2-json \
    php7.2-memcached \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-pdo \
    php7.2-phar \
    php7.2-sqlite \
    php7.2-xml \
    php7.2-zip \
    php7.2-dev \
    php7.2-xml \
    php-pear \
    curl \
    mariadb-client-10.0

RUN pecl install mongodb redis

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get install -y \
    nodejs \
    ruby-full \
    ruby-sass

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install yarn -y
RUN apt-get install -y nodejs
RUN npm install --global gulp-cli
RUN apt-get install -y git

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer global require drush/drush:8.1.15

RUN apt-get clean
