FROM php:7.0.10-cli

RUN docker-php-ext-install pdo_mysql

RUN apt-get update && \
  apt-get install -y libzip-dev && \
  rm -rf /var/lib/apt/lists/* && \
  docker-php-ext-install zip

RUN curl -o composer-setup.php https://getcomposer.org/installer && php composer-setup.php && unlink composer-setup.php

RUN apt-get update && \
  apt-get install -y libldap2-dev && \
  rm -rf /var/lib/apt/lists/* && \
  docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
  docker-php-ext-install ldap

RUN apt-get update && \
  apt-get install -y libzmq-dev && \
  rm -rf /var/lib/apt/lists/* && \
  pecl install zmq-beta && \
  docker-php-ext-enable zmq
