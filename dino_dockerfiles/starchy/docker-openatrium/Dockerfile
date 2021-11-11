FROM starchy/baseimage-docker
MAINTAINER starchy grant <starchy@gmail.com>

# Installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    apache2 \
    libapache2-mod-php \
    build-essential \
    php \
    php-dev \
    php-mysqlnd \
    php-imap \
    php-cli \
    php-pear \
    php-apcu \
    php-gd \
    php-memcached \
    python-pip \
    mysql-client \
    ssmtp \
    memcached \
    drush \
    git

# Cron
ADD ./assets/openatrium.cron.sh /etc/cron.hourly/openatrium
RUN chmod +x /etc/cron.hourly/openatrium

# Apache Cfg
ADD assets/apache.security.conf /etc/apache2/conf.d/
RUN rm -f /etc/apache2/sites-enabled/*
ADD assets/apache.openatrium.conf /etc/apache2/sites-available/
RUN ln -s /etc/apache2/sites-available/apache.openatrium.conf /etc/apache2/sites-enabled/openatrium.conf
RUN a2enmod rewrite

# Symlink for drush
RUN mkdir /usr/local/drush
RUN ln -s /usr/bin/drush /usr/local/drush/drush

# PHP Config
ENV PHP_MEMORY_LIMIT 1024M
ENV PHP_MAX_EXECUTION_TIME 900
ENV PHP_SESSION_SAVE_CACHE memcached
ENV PHP_SENDMAIL_PATH /usr/sbin/ssmtp -t
RUN sed -i \
    -e 's/^;session.save_path/session.save_path/g' \
    -e "s!^;sendmail_path =.*\$!sendmail_path = $PHP_SENDMAIL_PATH!g" \
    /etc/php/7.0/apache2/php.ini
ADD ./assets/update_php_vars.sh /usr/bin/
RUN chmod +x /usr/bin/update_php_vars.sh 
RUN update_php_vars.sh
RUN phpenmod imap

# build uploadprogress from git for php7 compatibility
RUN cd /root \
    && git clone https://github.com/Jan-E/uploadprogress.git \
    && cd uploadprogress \
    && phpize \
    && ./configure \
    && make \
    && make install \
    && echo 'extension=uploadprogress.so' >/etc/php/7.0/mods-available/uploadprogress.ini \
    && phpenmod uploadprogress \
    && cd \
    && rm -rf /root/uploadprogress


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
RUN chmod +x /usr/bin/update_ssmtp.sh 
RUN /usr/bin/update_ssmtp.sh

# Open Atrium
ENV OATRIUM_DOWNLOAD_URL https://ftp.drupal.org/files/projects/openatrium-7.x-2.644-core.tar.gz
ENV OATRIUM_DOWNLOAD_SHA256 8373f6f186445705974f3fe00929d409f246d9f1ab6e101bfd22df03231fade6
RUN rm -f /var/www/html/*
RUN curl -fsS "$OATRIUM_DOWNLOAD_URL" -o oatrium.tar.gz \
  && echo "$OATRIUM_DOWNLOAD_SHA256 oatrium.tar.gz" | sha256sum -c - \
  && tar -C /var/www/html -xzf oatrium.tar.gz --strip-components=1 \
  && rm -f oatrium.tar.gz

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
EXPOSE 80 443

# Volumes
VOLUME /data
VOLUME /var/www/html/sites

CMD ["/sbin/my_init"]

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
