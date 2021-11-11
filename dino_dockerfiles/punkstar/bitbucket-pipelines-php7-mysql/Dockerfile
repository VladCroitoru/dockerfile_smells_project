FROM debian:jessie

# With inspiration from https://github.com/smartapps-fr/bitbucket-pipelines-php-mysql

MAINTAINER Nick Jones <nick@nicksays.co.uk>

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL en_US.UTF-8
ENV LANGUAGE en_US:en

# Base
RUN \
 apt-get update && \
 apt-get -y --no-install-recommends install locales apt-utils curl ca-certificates && \
 echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
 locale-gen en_US.UTF-8 && \
 /usr/sbin/update-locale LANG=en_US.UTF-8 && \
 update-ca-certificates && \
 apt-get autoclean && apt-get clean && apt-get autoremove

# Add the PHP 7 repo
RUN \
  echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list && \
  echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list && \
  curl https://www.dotdeb.org/dotdeb.gpg | apt-key add -

# Install MySQL
RUN \
  apt-get update && \
  echo "mysql-server mysql-server/root_password password root" | debconf-set-selections && \
  echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections && \
  apt-get install -y mysql-server mysql-client && \
  apt-get autoclean && apt-get clean && apt-get autoremove

# Install PHP
RUN \
  apt-get update && \
  apt-get install -y git zip && \
  apt-get install -y php7.0-mysqlnd php7.0-cli php7.0-sqlite php7.0-mbstring php7.0-mcrypt php7.0-curl php7.0-intl php7.0-gd php7.0-xdebug php7.0-zip php7.0-xml && \
  apt-get autoclean && apt-get clean && apt-get autoremove

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/bin

# Install PHPUnit
RUN curl https://phar.phpunit.de/phpunit.phar > phpunit.phar && chmod +x phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit
