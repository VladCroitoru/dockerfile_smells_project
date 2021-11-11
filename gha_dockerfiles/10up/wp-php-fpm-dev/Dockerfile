ARG PHP_VERSION=7.1

# Set a BASE_IMAGE CI var to specify a different base image
ARG BASE_IMAGE=10up/wp-php-fpm
FROM ${BASE_IMAGE}:${PHP_VERSION}-ubuntu

ARG PHP_VERSION=7.1

USER root
RUN \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get update && \
  apt-get install -y \
    php${PHP_VERSION}-xdebug \
    mariadb-client \
    netcat \
    wget \
    git \
    strace \
    telnet \
    rsync \
    vim \
    sudo \
    iproute2 \
    subversion \
    unzip && apt clean all

WORKDIR /
COPY scripts/composer-installer.sh /composer-installer.sh
RUN sh /composer-installer.sh && mv /composer.phar /usr/local/bin/composer && chmod +x /usr/local/bin/composer
RUN curl https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar -o /usr/local/bin/wp
RUN chmod +x /usr/local/bin/wp
RUN echo "ALL ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/enable-all

# entrypoint needs to manage the PHP config but will be running as www-data
# Get things setup and then re-own the files necessary to allow this
RUN  mkdir /etc/php-extensions-available; \
  mv /etc/php.d/15-xdebug.ini /etc/php-extensions-available; \
  chown www-data -R /etc/php*

COPY entrypoint-dev.sh /
COPY bash.sh /
RUN chmod +x /entrypoint-dev.sh && \
    chmod +x /bash.sh

RUN echo "opcache.validate_timestamps=1" >> /etc/php/${PHP_VERSION}/mods-available/docker-opcache.ini

RUN cp -a /etc/skel /home/www-data && chown 33:33 -R /home/www-data && usermod -d /home/www-data www-data
USER www-data
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash && \
  source ~/.profile && \
  nvm install --lts
WORKDIR /var/www/html

ENTRYPOINT ["/entrypoint-dev.sh"]
