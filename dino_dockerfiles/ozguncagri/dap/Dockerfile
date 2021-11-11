FROM ubuntu:latest

# Install Apache 2, PHP 7 and some modules for development
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install \
    unzip \
    apache2 \
    php7.4 \
    libapache2-mod-php7.4 \
    curl \
    php7.4-mysql \
    php7.4-pgsql \
    php7.4-sqlite3 \
    php7.4-mbstring \
    php7.4-curl \
    php7.4-bz2 \
    php7.4-gd \
    php7.4-bcmath \
    php7.4-xml \
    php7.4-zip \
    php-redis \
    php-mongodb \
    php-imagick


# Enable apache mods.
RUN a2enmod php7.4
RUN a2enmod rewrite
RUN a2enmod headers

# Suppress FQDN message
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Expose apache to world
EXPOSE 80

# Copy www folder to app folder
ADD www /var/www

# Update default apache site with our config
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf

# Start apache in the foreground (you can override it with /bin/bash)
CMD /usr/sbin/apache2ctl -D FOREGROUND