FROM ubuntu:16.04

MAINTAINER Danil Kopylov <lobsterk@yandex.ru>

RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    apache2 \
    php libapache2-mod-php \
    ca-certificates \
    gettext \
    mc \
    libmcrypt-dev  \
    libicu-dev \
    libcurl4-openssl-dev \
    mysql-client \
    libldap2-dev \
    libfreetype6-dev \
    libfreetype6 \
    libpng12-dev

# exts
RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    php-mongodb \
    php-curl \
    php-intl \
    php-soap \
    php-xml \
    php-mcrypt \
    php-bcmath \
    php-mysql \
    php-mysqli \
    php-amqp \
    php-mbstring \
    php-ldap \
    php-zip \
    php-iconv \
    php-pdo \
    php-json \
    php-simplexml \
    php-xmlrpc \
    php-gmp \
    php-fileinfo \
    php-sockets \
    php-ldap \
    php-gd \
    php-xdebug

# Install mail server
COPY mailserver.sh /tmp/mailserver.sh
RUN /tmp/mailserver.sh

# set timezone Europe/Moscow
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

CMD ["/entrypoint.sh"]