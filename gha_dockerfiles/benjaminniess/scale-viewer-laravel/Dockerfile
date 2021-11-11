####
#### IMAGE
####
FROM php:7.4.2-cli-buster

ARG WP_ENV

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
      curl \
      less \
      libcurl4-openssl-dev \
      libpng-dev \
      libzip-dev \
      postfix \
      rsyslog \
      vim \
      zip \
      zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*


RUN curl --silent https://getcomposer.org/composer-stable.phar -o /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer

# Install vardumper
RUN mkdir -p /opt/composer/
RUN cd /opt/composer && composer require symfony/var-dumper

RUN mv $PHP_INI_DIR/php.ini-development $PHP_INI_DIR/php.ini
RUN sed -i 's/;extension=pdo_mysql/extension=pdo_mysql/' $PHP_INI_DIR/php.ini

RUN echo "auto_prepend_file = /opt/composer/vendor/autoload.php" > /usr/local/etc/php/conf.d/autoload.ini
RUN echo "sendmail_path = /usr/sbin/sendmail -t -i" > /usr/local/etc/php/conf.d/postfix.ini

RUN ln -s /var/www/html /app

RUN docker-php-ext-install pdo pdo_mysql gd curl mysqli zip

# POSTFIX
RUN echo "relayhost = mail" > /etc/postfix/main.cf
RUN echo "compatibility_level = 2" >> /etc/postfix/main.cf

RUN ln -s /dev/stdout /var/log/mail.log
RUN ln -s /dev/stderr /var/log/mail.err

WORKDIR /app
CMD service rsyslog start && service postfix start && cd /app && php artisan serve --port=80 --host=0.0.0.0
EXPOSE 80

