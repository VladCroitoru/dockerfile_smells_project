FROM php:7.1.8-fpm

ENV fpm_conf /usr/local/etc/php-fpm.d/www.conf

MAINTAINER rickshawhobo <rickshawhobo@gmail.com>

RUN apt-get update && apt-get install -y supervisor nginx

# Installs extra extensions and library depedencies
RUN apt-get install -y libsqlite3-dev libmcrypt-dev zlib1g-dev \
&& docker-php-ext-install pdo_mysql pdo_sqlite mysqli mcrypt json zip opcache

ADD supervisord.conf /etc/supervisord.conf
ADD entrypoint.sh /entrypoint.sh
ADD nginx.conf /etc/nginx/nginx.conf
ADD docker-vars.ini /usr/local/etc/php/conf.d/docker-vars.ini
ADD nginx-site.conf /etc/nginx/sites-available/default

RUN adduser --system nginx && addgroup --system nginx && adduser nginx nginx
RUN chmod 755 /entrypoint.sh

# config default fpm
RUN sed -i \
        -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" \
        -e "s/pm.max_children = 5/pm.max_children = 4/g" \
        -e "s/pm.start_servers = 2/pm.start_servers = 3/g" \
        -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" \
        -e "s/user = www-data/user = nginx/g" \
        -e "s/group = www-data/group = nginx/g" \
        -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" \
        -e "s/;pm.max_requests = 500/pm.max_requests = 200/g" \
        -e "s/;listen.mode = 0660/listen.mode = 0666/g" \
        -e "s/;listen.owner = www-data/listen.owner = nginx/g" \
        -e "s/;listen.group = www-data/listen.group = nginx/g" \
        -e "s/listen = 127.0.0.1:9000/listen = \/var\/run\/php-fpm.sock/g" \
        -e "s/^;clear_env = no$/clear_env = no/" \
        ${fpm_conf}

EXPOSE 443 80

# uncomment to install mongodb extension
# RUN apt-get install -y libssl-dev && pecl install mongodb
# echo "echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini
CMD ["/bin/bash", "/entrypoint.sh"]