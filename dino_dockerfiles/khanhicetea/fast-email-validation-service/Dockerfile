FROM php:7-alpine

RUN curl https://getcomposer.org/installer > composer-setup.php && php composer-setup.php && mv composer.phar /usr/local/bin/composer && rm composer-setup.php
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
WORKDIR /www
ADD . /www
RUN cp .env.example .env

RUN /usr/local/bin/composer install --no-dev --prefer-dist
CMD ["php", "/www/react", "server", "0.0.0.0:8000"]
