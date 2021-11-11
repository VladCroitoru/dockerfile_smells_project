FROM php:7.2-cli

COPY . /app

WORKDIR /app

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
  php composer-setup.php && rm composer-setup.php

RUN apt-get update && apt-get install -y git unzip

RUN php composer.phar install

CMD [ "./vendor/bin/phpunit" ]
