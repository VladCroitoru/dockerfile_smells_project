# Dockerfile for Ubuntu 18.04 nginx

# Pull base image.
FROM ubuntu:18.04

# Maintainer
MAINTAINER John McCracken <john.mccracken@qanw.co.uk>

# Install Packages
RUN DEBIAN_FRONTEND=noninteractive apt update -y && apt-get install software-properties-common -y && add-apt-repository ppa:ondrej/php -y && apt update -y && DEBIAN_FRONTEND=noninteractive apt install -y vim nginx nodejs npm \
    supervisor php7.3-fpm php7.3-mbstring php7.3-zip php-xdebug php-memcached php-imagick libssh2-1 libssl1.0.0 php-curl php-ssh2 php7.3-mysql php7.3-xml composer rsyslog zip unzip && apt clean && service php7.3-fpm start && usermod -u 1000 www-data

COPY ./conf/nginx.conf /etc/nginx/sites-enabled/default
COPY ./conf/php-custom.ini /etc/php/7.3/fpm/conf.d/99-custom.ini
COPY ./conf/php-fpm-pool.conf /etc/php/7.3/fpm/pool.d/www.conf
COPY ./webroot /var/www/html

EXPOSE 443 80

#Supervisor
COPY ./conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

