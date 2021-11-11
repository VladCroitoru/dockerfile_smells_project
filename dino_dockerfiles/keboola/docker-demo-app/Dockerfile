FROM php:7.1-cli

WORKDIR /code

RUN apt-get update && apt-get install -y \
        git \
        unzip \
   --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN curl -sS https://getcomposer.org/installer | php \
  && mv /code/composer.phar /usr/local/bin/composer

COPY . /code/
COPY ./docker/php/php.ini /usr/local/etc/php/php.ini

RUN composer install

CMD php /code/run.php --data=/data
