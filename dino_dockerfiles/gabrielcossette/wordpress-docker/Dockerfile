FROM wordpress:php7.2-fpm-alpine

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && chmod +x wp-cli.phar && mv wp-cli.phar /usr/bin/wp

RUN apk --no-cache add openssl msmtp

ENV PHPREDIS_VERSION 3.1.6

RUN docker-php-source extract \
  && curl -L -o /tmp/redis.tar.gz https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \
  && tar xfz /tmp/redis.tar.gz \
  && rm -r /tmp/redis.tar.gz \
  && mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \
  && docker-php-ext-install redis \
  && docker-php-source delete

ADD uploads.ini /usr/local/etc/php/conf.d/

ADD msmtprc /etc/msmtprc

ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
