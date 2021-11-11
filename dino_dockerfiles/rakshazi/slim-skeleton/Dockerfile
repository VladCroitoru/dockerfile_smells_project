FROM alpine:latest
MAINTAINER Nikita Chernyi <developer.nikus@gmail.com>

RUN apk --no-cache add nginx s6 php7 php7-fpm php7-json php7-ctype php7-mbstring php7-curl curl git \
    php7-session php7-ldap php7-pdo_mysql php7-phar php7-openssl php7-zlib php7-zip php7-xml php7-simplexml && \
    curl -o /usr/local/bin/composer https://getcomposer.org/composer.phar && \
    rm -rf /var/cache/apk/* /tmp/*

COPY . /var/www
COPY ./docker/nginx.conf /etc/nginx/nginx.conf
COPY ./docker/php-fpm.conf /etc/php7/php-fpm.d/www.conf
COPY ./docker/run.sh /usr/local/bin/run.sh
COPY ./docker/migrate.sh /usr/local/bin/migrate
COPY ./docker/phinx.sh /usr/local/bin/phinx
COPY ./docker/s6.d /etc/s6.d

RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*

VOLUME /var/www

EXPOSE 8080

CMD ["run.sh"]

