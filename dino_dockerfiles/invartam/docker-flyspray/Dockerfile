FROM invartam/docker-alpine-php-fpm-advanced

WORKDIR /
RUN apk update && apk add ca-certificates openssl && update-ca-certificates && \
    docker-php-ext-install exif && \
    wget https://github.com/Flyspray/flyspray/archive/master.zip -O /master.zip && \
    unzip master.zip && \
    mv flyspray-master/* /app/ && \
    rm -rf /flyspray-master /master.zip && \
    cd /app && \
    wget https://getcomposer.org/composer.phar && \
    php composer.phar install && \
    rm -f composer.phar && \
    touch flyspray.conf.php && \
    chown -R www-data:www-data /app
