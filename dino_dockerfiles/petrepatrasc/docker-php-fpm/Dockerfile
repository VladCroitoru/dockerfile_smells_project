FROM petrepatrasc/docker-ubuntu
MAINTAINER Petre Pătrașc <petre@dreamlabs.ro>
ENV REFRESHED_AT 2016-01-29 21:41:00

ENV PPA_PACKAGE=php5 \
    PPA_NAME=php \
    PHP_IGNORE_ENVIRONMENT_SETTINGS=false

# Conf settings
ENV PHP_CONF_FILE=/etc/php5/fpm/conf.d/20-system.ini \
    PHP_CONF_FILE_CLI=/etc/php5/cli/conf.d/20-system.ini \
    PHP_CONF_TIMEZONE=UTC \
    PHP_CONF_MAX_EXECUTION_TIME=30 \
    PHP_CONF_UPLOAD_LIMIT=40M \
    PHP_CONF_PHAR_READONLY=off \
    PHP_CONF_MEMORY_LIMIT=512M \
    PHP_CONF_DISPLAY_ERRORS=off \
    PHP_CONF_ERROR_REPORTING=0

# Pool settings
ENV PHP_POOL_FILE=/etc/php5/fpm/pool.d/20-system.pool.conf \
    PHP_POOL_USER=www-data \
    PHP_POOL_GROUP=www-data \
    PHP_POOL_LISTEN_HOST=127.0.0.1 \
    PHP_POOL_LISTEN_PORT=9000 \
    PHP_POOL_PM_CONTROL=dynamic \
    PHP_POOL_PM_MAX_CHILDREN=20 \
    PHP_POOL_PM_START_SERVERS=2 \
    PHP_POOL_PM_MIN_SPARE_SERVERS=1 \
    PHP_POOL_PM_MAX_SPARE_SERVERS=3 \
    PHP_POOL_CATCH_WORKERS_OUTPUT=yes

# Install PHP
RUN add-apt-repository ppa:ondrej/${PPA_NAME} && \
    apt-get update -qq && \
    apt-get install -qq -y \
        ${PPA_PACKAGE}-fpm \
        ${PPA_PACKAGE}-curl \
        ${PPA_PACKAGE}-cli \
        ${PPA_PACKAGE}-json \
        ${PPA_PACKAGE}-intl \
        ${PPA_PACKAGE}-imap \
        ${PPA_PACKAGE}-mcrypt \
        ${PPA_PACKAGE}-memcached \
        ${PPA_PACKAGE}-mysql \
        ${PPA_PACKAGE}-ldap \
        supervisor \
        netcat

# Install Composer
RUN cd /tmp && \
    php -r "readfile('https://getcomposer.org/installer');" | php && \
    mv composer.phar /usr/local/bin/composer

# Supervisor
ADD supervisor /etc/supervisor/

# Add PHP5-FPM Configuration Files
ADD php5-fpm /etc/php5/

# Make sure to run PHP as not daemonized
RUN sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php5/fpm/php-fpm.conf && \
		rm -f /etc/php5/fpm/pool.d/www.conf

ADD commands /root/commands
WORKDIR /etc/php5
EXPOSE 9000
CMD ["/root/commands/init.sh"]
