FROM php:7.0-fpm

ENV BOOKSTACK=BookStack \
    BOOKSTACK_VERSION=0.15.2

RUN apt-get update && apt-get install --no-install-recommends -y git zlib1g-dev libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev wget libldap2-dev libtidy-dev \
  && docker-php-ext-install pdo pdo_mysql mbstring zip tidy \
  && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
  && docker-php-ext-install ldap \
  && docker-php-ext-configure gd --with-freetype-dir=usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install gd \
  && cd /var/www && curl -sS https://getcomposer.org/installer | php \
  && cd /var/www  && mv /var/www/composer.phar /usr/local/bin/composer \
  && cd /var/www  && wget https://github.com/BookStackApp/BookStack/archive/v${BOOKSTACK_VERSION}.tar.gz -O ${BOOKSTACK}.tar.gz \
  && cd /var/www   && tar -xf ${BOOKSTACK}.tar.gz && mv BookStack-${BOOKSTACK_VERSION} ${BOOKSTACK} && rm ${BOOKSTACK}.tar.gz \
  && ls -lh /var/www/ \
  && cd /var/www/BookStack && composer install \
  && chown -R www-data:www-data /var/www/BookStack \
  && apt-get -y autoremove \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 9000

VOLUME /var/www/BookStack/public/

CMD ["php-fpm"]
