FROM ubuntu:14.04

MAINTAINER Michaelsun Baluyos

# Install packages
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -yq  --no-install-recommends install \
        apache2 \
        libapache2-mod-php5 \
        php5-curl \
        php5-gd \
        php5-mysql \
        php5-xmlrpc \
        php-apc \
        php5-mcrypt \
        php5-cli \
        mysql-server \
        mysql-common \
        mysql-client \
        wget \
        curl \
        pwgen \
        vim \
        git

# Install composer
RUN curl -sS https://getcomposer.org/installer --insecure | php -- --install-dir=/usr/local/bin --filename=composer

# Install phpmyadmin using composer
RUN composer create-project phpmyadmin/phpmyadmin --repository-url=https://www.phpmyadmin.net/packages.json --no-dev /var/www/phpmyadmin
# Mysql has no password, so do string replace to allow no password for phpmyadmin. Note not safe.
RUN grep -rl "\$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = false" /var/www/phpmyadmin | \
    xargs sed -i "s/\$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = false/\$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = true/g"

# Install phpunit
RUN composer global require "phpunit/phpunit=4.1.*"
RUN composer global require "phpunit/php-invoker=~1.1."
RUN ln -s  ~/.composer/vendor/phpunit/phpunit/phpunit   /usr/bin/

# Enable xdebug after composer
RUN apt-get -yq --no-install-recommends install php5-xdebug
ADD xdebug_settings.ini /etc/php5/mods-available/
RUN php5enmod xdebug_settings
RUN php5enmod mcrypt

# config to enable .htaccess
RUN service apache2 stop
RUN service mysql stop
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Enviornment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

#Get Magento files
RUN wget https://github.com/OpenMage/magento-mirror/archive/1.9.2.4.tar.gz --no-check-certificate -P /tmp
RUN tar -zxvf /tmp/1.9.2.4.tar.gz -C /tmp
RUN cp -al /tmp/magento-mirror-1.9.2.4/* /var/www/html -f
RUN rm -rf /tmp/magento-mirror-1.9.2.4 /tmp/1.9.2.4.tar.gz
RUN chmod -R o+w /var/www/html/media /var/www/html/var /var/www/html/app/etc

# Add volumes for MySQL 
VOLUME ["/etc/mysql", "/var/lib/mysql"]

EXPOSE 80 3306 22
