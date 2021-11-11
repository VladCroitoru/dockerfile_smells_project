FROM php:7.4.10-apache

RUN apt-get update && apt-get install -y libzip-dev libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev ca-certificates curl python python-pip cron\
&& pecl install mcrypt-1.0.3 redis xdebug \
&& docker-php-ext-enable mcrypt redis \
&& docker-php-ext-install -j$(nproc) iconv bcmath && docker-php-ext-configure gd --with-freetype --with-jpeg \
&& docker-php-ext-install -j$(nproc) gd mysqli pdo_mysql zip \
&& cp /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/ \
&& mv /var/www/html /var/www/public \
&& sed -i 's/\/var\/www\/html/\/var\/www\/public/' /etc/apache2/sites-available/default-ssl.conf \
&& sed -i 's/\/var\/www\/html/\/var\/www\/public/' /etc/apache2/sites-available/000-default.conf 

RUN mkdir /etc/supervisord \
&& mkdir /etc/supervisord/conf.d \
&& mkdir /var/log/supervisord \
&& pip install supervisor

RUN echo "* * * * * php /var/www/artisan schedule:run >> /dev/null 2>&1" | crontab

COPY supervisord.conf /etc/supervisord/

COPY laravel-worker.conf /etc/supervisord/conf.d/

COPY apached.conf /etc/supervisord/conf.d/

COPY crond.conf /etc/supervisord/conf.d/

WORKDIR /var/www

CMD ["/usr/local/bin/supervisord","-c","/etc/supervisord/supervisord.conf"]
