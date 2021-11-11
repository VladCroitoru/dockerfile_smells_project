FROM ubuntu:14.04

MAINTAINER Luca Mattivi <luca@smartdomotik.com>

ENV PROJECT_PATH=/var/www \
    PROJECT_URL=uala.it \
    DEBIAN_FRONTEND=noninteractive \
    APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_LOG_DIR=/var/log/apache2 \
    APACHE_LOCK_DIR=/var/lock/apache2 \
    APACHE_PID_FILE=/var/run/apache2/apache2.pid \
    PHP_MODS_CONF=/etc/php/5.6/mods-available \
    PHP_INI=/etc/php/5.6/apache2/php.ini \
    PHP_INI_CONFD=/etc/php/5.6/apache2/conf.d \
    TERM=xterm

RUN apt-get update && apt-get upgrade -y --force-yes

# Use PHP5.6 instead of PHP5.5 (need to manually add repo key)
RUN apt-get update -q && apt-get upgrade -yqq && \
    apt-get install -yqq software-properties-common && \
    add-apt-repository ppa:ondrej/php && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

# Utilities, Apache, PHP, and supplementary programs
RUN apt-get update && apt-get install -yqq --force-yes \
    npm \
    git \
    htop \
    nano \
    wget \
    zip \
    unzip \
    apache2 \
    libapache2-mod-php5.6 \
    curl \
    php5.6 \
    php5.6-dom \
    php5.6-mbstring \
    php5.6-mysql \
    php5.6-intl \
    php5.6-mcrypt \
    php5.6-redis \
    php5.6-soap \
    php5.6-cgi \
    php5.6-curl \
    php5.6-imagick \
    gettext

RUN ln -s "$(which nodejs)" /usr/bin/node

# Apache mods
RUN a2enmod rewrite expires headers

# Custom PHP.ini
COPY custom-php.ini $PHP_INI_CONFD/custom-php.ini

# Apache2 conf
RUN echo "ServerName localhost" | sudo tee /etc/apache2/conf-available/fqdn.conf && \
    a2enconf fqdn

# Set the timezone.
RUN sudo echo "Europe/Paris" > /etc/timezone && \
    sudo dpkg-reconfigure -f noninteractive tzdata

# Port to expose
EXPOSE 80

# VirtualHost
COPY apache-vhost.conf /etc/apache2/sites-available/000-default.conf


# move composer before copy project, This should improve docker cache.
WORKDIR $PROJECT_PATH

COPY artisan $PROJECT_PATH/artisan
COPY composer.json $PROJECT_PATH/composer.json
COPY composer.lock $PROJECT_PATH/composer.lock
COPY package.json $PROJECT_PATH/package.json
COPY vendor $PROJECT_PATH/vendor


# must copy project before composer for artisan
#COPY . $PROJECT_PATH
#WORKDIR $PROJECT_PATH


RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    composer install --no-interaction --prefer-dist --optimize-autoloader --no-scripts --no-dev --ignore-platform-reqs
    #composer install --no-interaction --optimize-autoloader

# Copy site into place
COPY . $PROJECT_PATH

RUN php artisan clear-compiled
RUN php artisan optimize

# Folder permissions & Add permissions for temp data of mpdf library
RUN chown -R $APACHE_RUN_USER:$APACHE_RUN_GROUP config/ && \
    chown -R $APACHE_RUN_USER:$APACHE_RUN_GROUP public/ && \
    chown -R $APACHE_RUN_USER:root logs/ && \
    chown -R $APACHE_RUN_USER:root storage/ && \
    chown -R $APACHE_RUN_USER:root bootstrap/ && \
    chown -R $APACHE_RUN_USER:$APACHE_RUN_GROUP vendor/ && \
    chmod +x $PROJECT_PATH/generate_env.sh && \
    chmod +x start.sh

# Remove pre-existent apache pid and start apache
CMD rm -f $APACHE_PID_FILE && /usr/sbin/apache2ctl -D FOREGROUND