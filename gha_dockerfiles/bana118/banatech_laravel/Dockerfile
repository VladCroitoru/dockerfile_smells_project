FROM php:7.4-fpm

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

COPY deploy/www.conf /usr/local/etc/php-fpm.d/zzz-www.conf
COPY deploy/php.ini /usr/local/etc/php/php.ini

#Author
LABEL maintainer="banatech.net"

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    procps \
    nano \
    vim-nox \
    nginx \
    supervisor \
    nodejs \
    npm \
    certbot \
    sqlite3 && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

# update node npm
RUN npm install n -g
RUN n stable
RUN apt purge -y nodejs npm
ENV PATH $PATH:/usr/local/bin/node

# install packages, but it doesn't work so do it manually in docker

# install laravel and etc
# RUN cd /root/banatech_laravel && composer install --optimize-autoloader --no-dev

# install npm packages
# RUN cd /root/banatech_laravel && npm install

# clear laravel caches
# This app doesn't seem to delete the route cache...
# RUN cd /root/banatech_laravel && php artisan config:cache
# RUN cd /root/banatech_laravel && php artisan config:cache && php artisan route:cache

# generate app key
# RUN cd /root/banatech_laravel && php artisan key:generate

# migrate
# RUN cd /root/banatech_laravel && php artisan migrate

# compile css and js
# RUN cd /root/banatech_laravel && npm run prod


# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY deploy/supervisor-app.conf /etc/supervisor/conf.d/

# create socket file for php-fpm
RUN mkdir /var/run/php-fpm
RUN touch /var/run/php-fpm/php-fpm.sock
RUN chmod 777 /var/run/php-fpm/php-fpm.sock

# run nginx
EXPOSE 80
EXPOSE 443
CMD ["supervisord", "-n"]
