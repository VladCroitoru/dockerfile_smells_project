FROM php:7-apache
MAINTAINER Phy <dockerfile@phy25.com>

ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars

RUN { \
        echo; \
        echo 'ServerName howto.info.bit.edu.cn'; \
        echo '<IfModule mpm_prefork_module>'; \
        echo 'StartServers                   5'; \
        echo 'MinSpareServers                5'; \
        echo 'MaxSpareServers               10'; \
        echo 'MaxClients                   150'; \
        echo 'MaxRequestsPerChild          100'; \
        echo '</IfModule>'; \
    } | tee -a "$APACHE_CONFDIR/conf-available/docker-php.conf" \
    && ln -s $APACHE_CONFDIR/mods-available/rewrite.load $APACHE_CONFDIR/mods-enabled/rewrite.load

ADD index.html /var/www/html/index.html

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd
# ADD php.ini /usr/local/etc/php/

ENTRYPOINT ["docker-php-entrypoint"]

EXPOSE 80
VOLUME ["/var/www/html"]
CMD ["apache2-foreground"]