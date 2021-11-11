FROM trafex/alpine-nginx-php7:2.1.0 AS webserver

LABEL maintainer="matteo@matteogheza.it"
LABEL version="1.0"
LABEL description="Docker project for open source firefighter management software"

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./server /var/www/html
COPY --from=composer /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html
USER root
RUN apk add --no-cache bash sed php-pdo php-pdo_mysql php-pdo_sqlite php-pdo_pgsql git
RUN composer install --no-dev --optimize-autoloader --no-interaction --no-progress

#RUN echo "@reboot cd /var/www/html/install && php install.php config" > /etc/crontabs/root

USER nobody
EXPOSE 8080
