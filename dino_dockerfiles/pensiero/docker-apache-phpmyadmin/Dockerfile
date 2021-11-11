FROM ubuntu:16.04

MAINTAINER Oscar Fanelli <oscar.fanelli@gmail.com>

ENV PROJECT_PATH=/var/www \
    DEBIAN_FRONTEND=noninteractive \
    APACHE_PID_FILE=/var/run/apache2/apache2.pid \
    PHP_MODS_CONF=/etc/php/7.0/mods-available \
    PHP_INI=/etc/php/7.0/apache2/php.ini \
    MYSQL_ROOT_PASSWORD=pornfood \
    TERM=xterm

RUN (echo 'phpmyadmin phpmyadmin/dbconfig-install boolean true' | debconf-set-selections)
RUN (echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' | debconf-set-selections)

RUN apt-get update -q && apt-get upgrade -yqq

# Utilities, Apache, PHP, and supplementary programs
RUN apt-get update -q && apt-get install -yqq --force-yes \
    mysql-client \
    apache2 \
    libapache2-mod-php \
    php \
    php-mysql \
    phpmyadmin

# PHP.ini file: enable <? ?> tags and quieten logging
RUN sed -i "s/short_open_tag = .*/short_open_tag = On/" $PHP_INI && \
    sed -i "s/memory_limit = .*/memory_limit = 512M/" $PHP_INI && \
    sed -i "s/display_errors = .*/display_errors = Off/" $PHP_INI && \
    sed -i "s/display_startup_errors = .*/display_startup_errors = Off/" $PHP_INI && \
    sed -i "s/post_max_size = .*/post_max_size = 1G/" $PHP_INI && \
    sed -i "s/upload_max_filesize = .*/upload_max_filesize = 1G/" $PHP_INI && \
    sed -i "s/max_file_uploads = .*/max_file_uploads = 100/" $PHP_INI && \
    sed -i "s/error_reporting = .*$/error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT/" $PHP_INI

# Apache2 conf
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf
RUN a2enconf fqdn

# Cleanup
RUN apt-get autoremove -yqq

# Port to expose
EXPOSE 80

CMD rm -f $APACHE_PID_FILE && /usr/sbin/apache2ctl -D FOREGROUND