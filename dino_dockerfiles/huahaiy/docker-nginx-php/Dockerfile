FROM huahaiy/debian

MAINTAINER Huahai Yang <hyang@juji-inc.com>

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y upgrade && \ 
    apt-get -y install nginx-extras curl git unzip php7.0-fpm php7.0-mysql php7.0-curl php7.0-gd php7.0-mbstring php7.0-cli php7.0-opcache php-uploadprogress php-pear php-memcached 

# Use nginx only
RUN apt-get -y --purge remove apache2* && \
    apt-get -y --purge autoremove && \ 
    apt-get clean && \ 
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

# install composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"


# php-fpm config
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/7.0/fpm/php.ini

# sites-enabled should be mounted to a host directory, which should contain at least one nginx site config file
# doc-root should be mounted to a host directory that contains the actual Web content
VOLUME ["/etc/nginx/sites-enabled", "/doc-root"]

# nginx should be configed to listen to at least one of these ports
EXPOSE 80 8080 8081

# run nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
