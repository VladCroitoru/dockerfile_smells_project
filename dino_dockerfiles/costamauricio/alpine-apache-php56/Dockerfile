FROM php:5-fpm-alpine

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/bin/composer

RUN apk add --update vim postgresql-dev freetype-dev libmcrypt-dev libjpeg-turbo-dev libpng-dev zlib-dev apache2-proxy

RUN docker-php-ext-install iconv mcrypt pdo pdo_pgsql pdo_mysql opcache zip mysql

RUN sed -i -r 's/(LoadModule.*mod_mpm_prefork.so)/#\1/' /etc/apache2/httpd.conf
RUN sed -i -r 's/#(LoadModule.*mod_mpm_event.so)/\1/' /etc/apache2/httpd.conf
RUN sed -i -r 's/#(LoadModule.*mod_rewrite.so)/\1/' /etc/apache2/httpd.conf

RUN echo "php_admin_value[date.timezone] = \"America/Sao_Paulo\"">>/usr/local/etc/php-fpm.d/www.conf
RUN echo "php_admin_value[display_errors] = On">>/usr/local/etc/php-fpm.d/www.conf
RUN echo "php_admin_value[error_reporting] = E_ALL & ~E_DEPRECATED">>/usr/local/etc/php-fpm.d/www.conf
RUN echo "LoadModule slotmem_shm_module modules/mod_slotmem_shm.so">/etc/apache2/conf.d/slotmem_shm.conf
COPY ./artifacts/www.conf /etc/apache2/conf.d/www.conf

EXPOSE 80

RUN mkdir /run/apache2

ENTRYPOINT httpd && php-fpm -F
