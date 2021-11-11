
FROM phusion/baseimage
MAINTAINER gabriel schubiner <gabriel.schubiner@gmail.com>

# Installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    apache2 \
    libapache2-mod-php5 \
    build-essential \
    php5 \
    php5-dev \
    php5-mysqlnd \
    php5-imap \
    php5-cli \
    php-pear \
    php-apc \
    php5-gd \
    php5-memcached \
    python-pip \
    mysql-client \
    ssmtp \
    memcached

# Cron
ADD ./assets/openatrium.cron.sh /etc/cron.hourly/openatrium
RUN chmod +x /etc/cron.hourly/openatrium

# Apache Cfg
RUN rm -f /etc/apache2/sites-enabled/*
ADD assets/apache.openatrium.conf /etc/apache2/sites-available/
RUN ln -s /etc/apache2/sites-available/apache.openatrium.conf /etc/apache2/sites-enabled/openatrium.conf
RUN a2enmod rewrite

# PHP Config
ENV PHP_MEMORY_LIMIT 1024M
ENV PHP_MAX_EXECUTION_TIME 900
ENV PHP_SESSION_SAVE_CACHE memcached
ENV PHP_SENDMAIL_PATH /usr/sbin/ssmtp -t
RUN sed -i \
    -e 's/^;session.save_path/session.save_path/g' \
    -e "s!^;sendmail_path =.*\$!sendmail_path = $PHP_SENDMAIL_PATH!g" \
    /etc/php5/apache2/php.ini
ADD ./assets/update_php_vars.sh /usr/bin/
RUN chmod +x /usr/bin/update_php_vars.sh 
RUN update_php_vars.sh
RUN php5enmod imap
RUN pecl install -Z uploadprogress && \
    echo 'extension=uploadprogress.so' >/etc/php5/mods-available/uploadprogress.ini && \
    php5enmod uploadprogress

# Default ENV vars
## Apache
RUN echo "www-data" >/etc/container_environment/APACHE_RUN_GROUP && \
    echo "www-data" >/etc/container_environment/APACHE_RUN_USER && \
    echo "/var/run/apache2/apache2.pid" >/etc/container_environment/APACHE_PID_FILE && \
    echo "/var/run/apache2" >/etc/container_environment/APACHE_RUN_DIR && \
    echo "/var/lock/apache2" >/etc/container_environment/APACHE_LOCK_DIR && \
    echo "/var/log/apache2" >/etc/container_environment/APACHE_LOG_DIR


## MEMCACHED
ENV MEMCACHED_MEM 1024

## INIT
ENV NO_FILE_PERMISSION_RESTORE false

## MIGRATE SITES
ENV MIGRATE_SITES_TO false

## Site Installation 
ENV ACCOUNT_NAME admin
ENV ACCOUNT_PASS insecurepass
ENV ACCOUNT_MAIL admin@example.com
ENV SITE_NAME Open Atrium
ENV SITE_MAIL admin@example.com
ENV INSTALL_SITE true

## DB
ENV AUTO_DB_SETTINGS true

## sSMTP
ENV SSMTP_ROOT example.address@gmail.com
ENV SSMTP_MAILHUB smtp.gmail.com:587
ENV SSMTP_HOSTNAME example.address@gmail.com
ENV SSMTP_USE_STARTTLS YES
ENV SSMTP_AUTH_USER example.address
ENV SSMTP_AUTH_PASS emailpassword
ENV SSMTP_FROMLINE_OVERRIDE YES
ENV SSMTP_AUTH_METHOD LOGIN

ADD ./assets/update_ssmtp.sh /usr/bin/update_ssmtp.sh
RUN rm -f /etc/ssmtp/ssmtp.conf
ADD ./assets/ssmtp.conf /etc/ssmtp/ssmtp.conf
RUN chmod +x /usr/bin/update_ssmtp.sh && update_ssmtp.sh

# Drush install
RUN pear channel-discover pear.drush.org

RUN pear install drush/drush

# Open Atrium
RUN rm -f /var/www/html/*
RUN curl http://ftp.drupal.org/files/projects/openatrium-7.x-2.33-core.tar.gz | tar xz -C /var/www/html --strip-components=1 

# Services
RUN mkdir /etc/service/memcached /etc/service/apache
ADD ./assets/services/memcached.sh /etc/service/memcached/run
ADD ./assets/services/apache.sh /etc/service/apache/run
ADD ./assets/services/apache-log-forwarder.sh /etc/service/apache-log-forwarder/run
RUN chmod -R +x /etc/service/

# Init script
ADD ./assets/init.sh /etc/my_init.d/10_init.sh
RUN chmod -R +x /etc/my_init.d/

# Ports
EXPOSE 22 80 443

# Volumes
VOLUME /data
VOLUME /var/www/html/sites

CMD ["/sbin/my_init"]

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
