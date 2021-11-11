# Dockerfile based on https://github.com/skeal/docker-baikal

FROM nginx:latest
MAINTAINER  Dmitri Rubinstein

# Set Environement variables
ENV LC_ALL=C
ENV DEBIAN_FRONTEND=noninteractive

# Update package repository and install packages
RUN apt-get -y update && \
    apt-get -y install supervisor python php-common php-fpm php-zip \
               php-sqlite3 nano wget curl php-curl php-cli php-mysql \
               php-xml php-mbstring php-sabre-vobject && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/local/bin --filename=composer

# Copy Baikal sources
WORKDIR /usr/share/nginx/html/Baikal
COPY README.md CHANGELOG.md composer.json Makefile ./
COPY Core ./Core/
COPY Specific ./Specific/
COPY html ./html/


RUN cp -a ./Specific ./Specific_Initial && \
    chown -R www-data:www-data ./

RUN composer install

# Add configuration files. User can provides customs files using -v in the image startup command line.
COPY docker/supervisord.conf /etc/supervisor/supervisord.conf
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/php-fpm.conf /etc/php/7.0/fpm/php-fpm.conf
COPY docker/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# Expose HTTP port
EXPOSE      80

# Last but least, unleach the daemon!
ENTRYPOINT  ["/usr/local/bin/docker-entrypoint.sh"]
