FROM ubuntu:xenial
MAINTAINER Sascha Wessel <swessel@gr4yweb.de>

# Install all Packages
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install \
    wget unzip curl git apache2 php7.0 libapache2-mod-php7.0 php7.0 php7.0-cli php7.0-gd php7.0-json php7.0-ldap php7.0-mbstring php7.0-mysql php7.0-xml php7.0-xsl php7.0-zip php7.0-soap 

# Enable apache mods.
RUN a2enmod php7.0
RUN a2enmod rewrite

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.0/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.0/apache2/php.ini

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Expose HTTP
EXPOSE 80

# Expose HTTPS
EXPOSE 443

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Change into directory and remove /var/www/html
RUN cd /var/www; rm -r /var/www/html

# Download and Unzip ProcessWire
RUN wget https://github.com/processwire/processwire/archive/master.zip -O processwire.zip; unzip processwire.zip -d /var/www; rm processwire.zip; mv /var/www/processwire-master /var/www/html
# Change into
WORKDIR /var/www/html
VOLUME /var/www/html

RUN chown -R www-data:www-data /var/www && find /var/www -type d -exec chmod 750 {} \; && find /var/www -type f -exec chmod 640 {} \;

# Install Dependencies
RUN /usr/bin/composer install

# Uncomment RewriteBase
RUN sed -i 's|# RewriteBase /~user/|RewriteBase /|1' /var/www/html/htaccess.txt

# Move .htaccess into place
RUN mv /var/www/html/htaccess.txt /var/www/html/.htaccess

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD /usr/sbin/apache2ctl -D FOREGROUND
