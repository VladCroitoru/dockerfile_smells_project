FROM        cloudposse/apache
MAINTAINER  Erik Osterman "e@osterman.com"

USER root


# Install Apache with PHP 5.5
RUN apt-get update && \
    apt-get install -y libapache2-modsecurity \
                       libapache2-mod-php \
                       php-cli \
                       php \
                       php-mail \
                       php-json \
                       php-readline \
                       php-redis \
                       php-memcache \
                       php-apcu \
                       php-mcrypt \
                       php-curl \
                       php-gd \
                       php-pgsql \
                       php-mysql \
                       php-soap  && \
      apt-get clean && rm -rf /tmp/* /var/tmp/*

ADD rootfs /

RUN phpenmod security && \
    phpenmod short-open-tag && \
    phpenmod uploads && \
    phpenmod soap && \
    a2enmod mpm_prefork && \
    a2enmod security2




