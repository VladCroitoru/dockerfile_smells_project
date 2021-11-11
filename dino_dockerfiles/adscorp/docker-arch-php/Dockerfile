FROM jprjr/arch

MAINTAINER John Regan <john@jrjrtech.com>
MAINTAINER Zerph 

RUN pacman -Syy --noconfirm --quiet > /dev/null

RUN pacman -S --noconfirm --quiet --needed php-fpm php-gd \
    php-mcrypt php-ldap php-sqlite php-pgsql php-pear \
    php-xcache php-intl >/dev/null 2>/dev/null
    

RUN sed -i 's/;extension=gd.so/extension=gd.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=iconv.so/extension=iconv.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=mcrypt.so/extension=mcrypt.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=mysql.so/extension=mysql.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=sqlite3.so/extension=sqlite3.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=pgsql.so/extension=pgsql.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=ldap.so/extension=ldap.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=openssl.so/extension=openssl.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=pdo_pgsql.so/extension=pdo_pgsql.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=pdo_mysql.so/extension=pdo_mysql.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=pdo_sqlite.so/extension=pdo_sqlite.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=intl.so/extension=intl.so/g' /etc/php/php.ini
RUN sed -i 's/;extension=xcache.so/extension=xcache.so/g' /etc/php/conf.d/xcache.ini
RUN sed -i 's/;extension=phar.so/extension=phar.so/g' /etc/php/php.ini

RUN echo "<?php phpinfo(); ?>" > /srv/http/index.php

RUN paccache -rk0
RUN pacman -Scc --noconfirm

RUN touch /var/log/php-fpm.log
RUN chown -R http /var/log/php-fpm.log /run/php-fpm

EXPOSE 9000
VOLUME /srv/http
ENTRYPOINT ["php-fpm","-F"]
