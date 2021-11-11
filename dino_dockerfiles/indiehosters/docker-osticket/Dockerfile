FROM php:5.6-fpm

RUN mkdir -p /usr/src/osticket
WORKDIR /usr/src/osticket

# environment for osticket
ENV OSTICKET_VERSION 1.9.14
ENV HOME /var/www/html

# requirements
RUN apt-get update && apt-get -y install \
  libc-client-dev \
  libjpeg-dev \
  libkrb5-dev \
  libldap2-dev \
  libpng12-dev \
  libpq-dev \
  libxml2-dev \
  ssmtp \
  zip \
 && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
 && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
 && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
 && docker-php-ext-install gd gettext imap json mbstring ldap mysqli xml

RUN set -ex \
 && pecl install APCu-4.0.10 \
 && docker-php-ext-enable apcu

# Download & install OSTicket
RUN curl -fsSL -o osTicket.zip http://osticket.com/sites/default/files/download/osTicket-v${OSTICKET_VERSION}.zip && \
    unzip osTicket.zip && \
    rm osTicket.zip && \
    chown -R www-data:www-data ./upload/ && \
    chmod -R a+rX ./upload/ ./scripts/ && \
    chmod -R u+rw ./upload/ ./scripts/ && \
    chfn -f 'OsTicket Admin' www-data && \
    curl -fsSL -o upload/include/i18n/fr.phar http://osticket.com/sites/default/files/download/lang/fr.phar && \
    curl -fsSL -o upload/include/plugins/auth-ldap.phar http://osticket.com/sites/default/files/download/plugin/auth-ldap.phar

COPY conf.ini /usr/local/etc/php/conf.d/osticket.ini
COPY docker-entrypoint.sh /entrypoint.sh

VOLUME /var/www/html
WORKDIR /var/www/html
ENTRYPOINT ["/entrypoint.sh"]
CMD ["php-fpm"]
