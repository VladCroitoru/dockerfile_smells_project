FROM petrepatrasc/docker-ubuntu
MAINTAINER Petre Pătrașc <petre@dreamlabs.ro>
ENV REFRESHED_AT 2015-10-12 21:41:00

ENV REPOSITORY_VERSION=5.6 \
    REPOSITORY_PACKAGE=php5

# Conf settings
ENV PHP_CONF_FILE=/etc/php5/fpm/conf.d/20-system.ini \
    PHP_CONF_FILE_CLI=/etc/php5/cli/conf.d/20-system.ini \
    PHP_CONF_TIMEZONE=Europe/UTC \
    PHP_CONF_MAX_EXECUTION_TIME=30 \
    PHP_CONF_UPLOAD_LIMIT=40M \
    PHP_CONF_PHAR_READONLY=off \
    PHP_CONF_MEMORY_LIMIT=512M \
    PHP_CONF_DISPLAY_ERRORS=on \
    PHP_CONF_ERROR_REPORTING=E_ALL \
    PHP_CONF_XDEBUG_MAX_NESTING_LEVEL=350 \
    PHP_CONF_XDEBUG_REMOTE_ENABLE=on \
    PHP_CONF_XDEBUG_REMOTE_HANDLER=dbgp \
    PHP_CONF_XDEBUG_REMOTE_CONNECT_BACK=on \
    PHP_CONF_XDEBUG_REMOTE_PORT=9005 \
    PHP_CONF_XDEBUG_IDEKEY=xdebug \
    PHP_CONF_XDEBUG_PROFILER_ENABLE_TRIGGER=1 \
    PHP_CONF_XDEBUG_PROFILER_OUTPUT_DIR=/var/xdebug/profile/ \
    PHP_CONF_XDEBUG_PROFILER_OUTPUT_NAME=profile.out.%t \
    PHP_CONF_XDEBUG_TRACE_ENABLE_TRIGGER=1 \
    PHP_CONF_XDEBUG_TRACE_OUTPUT_DIR=/var/xdebug/trace/ \
    PHP_CONF_XDEBUG_TRACE_OUTPUT_NAME=trace.out.%t

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
RUN add-apt-repository ppa:ondrej/${REPOSITORY_PACKAGE}-${REPOSITORY_VERSION} && \
    apt-get update -qq && \
    apt-get install -qq -y \
        ${REPOSITORY_PACKAGE}-fpm \
        ${REPOSITORY_PACKAGE}-curl \
        ${REPOSITORY_PACKAGE}-cli \
        ${REPOSITORY_PACKAGE}-json \
        ${REPOSITORY_PACKAGE}-intl \
        ${REPOSITORY_PACKAGE}-imap \
        ${REPOSITORY_PACKAGE}-mcrypt \
        ${REPOSITORY_PACKAGE}-xdebug \
        ${REPOSITORY_PACKAGE}-memcached \
        ${REPOSITORY_PACKAGE}-mysql \
        ${REPOSITORY_PACKAGE}-ldap \
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
