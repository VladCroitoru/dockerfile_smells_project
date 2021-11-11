FROM nimmis/apache

MAINTAINER peavers <peavers@gmail.com>

# disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN apt-get update && \
    apt-get install -y  \
    git \
    sudo \
    php \
    libapache2-mod-php \
    php-fpm \
    php-cli \
    php-mysqlnd \
    php-pgsql \
    php-sqlite3 \
    php-redis \
    php-apcu \
    php-intl \
    php-imagick \
    php-mcrypt \
    php-json \
    php-gd \
    php-curl \
    php-mbstring \
    php-xml \
    php-tidy

# Configure packages
RUN phpenmod mcrypt

# Settings
RUN echo "ServerName localhost" > /etc/apache2/conf-available/fqdn.conf && \
    echo "memory_limit=512M" > /etc/php/7.0/apache2/conf.d/memory-limit.ini && \
	echo "date.timezone = Pacific/Auckland" > /etc/php/7.0/apache2/conf.d/timezone.ini && \
	sed -i -e 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf && \
	a2enmod rewrite expires remoteip cgid && \
	usermod -u 1000 www-data && \
	usermod -G staff www-data

# Install Composer
RUN cd /tmp && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer

# Setup permissions for www-data
RUN chgrp www-data /var/www/ && \
    chgrp www-data -R /var/www/ && \
    chmod g+rwxs -R /var/www/

# Cleanup
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 80
