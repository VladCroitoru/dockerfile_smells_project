# Need to hard code the version until this is resolved https://github.com/renovatebot/renovate/issues/5626
FROM php:8.0-apache-buster@sha256:65c8c4d468f13afb058445b5338e394d245ac2b9e30dcc6cab0becbeba3aa0bf
ENV DEBIAN_FRONTEND=noninteractive
ARG USER_ID=2000
ARG APP_DIR=/app
ARG USER_HOME=/home/user
ARG TZ=UTC
ARG CA_HOSTS_LIST
ARG YII_ENV
# Support for composer API token for Github and Gitlab
ARG GITHUB_API_TOKEN
ARG GITLAB_API_HOST
ARG GITLAB_API_TOKEN
# System - Application path
ENV APP_DIR=${APP_DIR}
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# System - Update embded package
# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get -y install --no-install-recommends \
            g++ \
            git \
            curl \
            gnupg2 \
            imagemagick \
            libcurl3-dev \
            libicu-dev \
            libfreetype6-dev \
            libjpeg-dev \
            libjpeg62-turbo-dev \
            libmagickwand-dev \
            libpq-dev \
            libpng-dev \
            libxml2-dev \
            libzip-dev \
            zlib1g-dev \
            openssh-client \
            nano \
            unzip \
            libcurl4-openssl-dev \
            libssl-dev \
            netcat \
            runit \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# System - Set default timezone
ENV TZ=${TZ}
# System - Define HOME directory
ENV USER_HOME=${USER_HOME}
RUN mkdir -p ${USER_HOME} \
    && chgrp -R 0 ${USER_HOME} \
    && chmod -R g=u ${USER_HOME}
# System - Set path
ENV PATH=/app:/app/vendor/bin:/root/.composer/vendor/bin:$PATH
# System - Set terminal type
ENV TERM=linux
# System - Install Yii framework bash autocompletion
ADD https://raw.githubusercontent.com/yiisoft/yii2/master/contrib/completion/bash/yii /etc/bash_completion.d/yii
RUN chmod a+rx /etc/bash_completion.d/yii
# Php - configure if php-fpm
ENV PHPFPM_PM_MAX_CHILDREN=10
ENV PHPFPM_PM_START_SERVERS=5
ENV PHPFPM_PM_MIN_SPARE_SERVERS=2
ENV PHPFPM_PM_MAX_SPARE_SERVERS=5
# hadolint ignore=DL3008,SC1089,SC2016
RUN if [ -d /usr/local/etc/php-fpm.d ]; then \
        sed -i -e 's#\(listen *= *\).*$#\1/var/run/php-fpm/fpm.sock#g' \
            -e 's#^\(user *= *\).*$#\1${APACHE_RUN_USER}#g' \
            -e 's#^\(group *= *\).*$#\1${APACHE_RUN_GROUP}#g' \
            -e 's#^\(pm.max_children *= *\).*$#\1${PHPFPM_PM_MAX_CHILDREN}#g' \
            -e 's#^\(pm.start_servers *= *\).*$#\1${PHPFPM_PM_START_SERVERS}#g' \
            -e 's#^\(pm.min_spare_servers *= *\).*$#\1${PHPFPM_PM_MIN_SPARE_SERVERS}#g' \
            -e 's#^\(pm.max_spare_servers *= *\).*$#\1${PHPFPM_PM_MAX_SPARE_SERVERS}#g' \
            /usr/local/etc/php-fpm.d/*.conf ; \
    fi
# All - Add configuration files
COPY image-files/ /
# Apache - configure if apache image
ENV APACHE_REMOTE_IP_HEADER=X-Forwarded-For
ENV APACHE_REMOTE_IP_TRUSTED_PROXY="10.0.0.0/8 172.16.0.0/12 192.168.0.0/16"
ENV APACHE_REMOTE_IP_INTERNAL_PROXY="10.0.0.0/8 172.16.0.0/12 192.168.0.0/16"
# Apache - Avoid warning at startup
ENV APACHE_SERVER_NAME=__default__
# Apache - Syslog Log
ENV APACHE_SYSLOG_PORT=514
ENV APACHE_SYSLOG_PROGNAME=httpd
RUN if which apache2 > /dev/null 2>&1; then \
        sed -i -e 's#^export \([^=]\+\)=\(.*\)$#export \1=${\1:=\2}#' /etc/apache2/envvars \
        # Apache - Enable mod rewrite and headers
        && a2enmod headers rewrite \
        # Apache - Disable useless configuration
        && a2disconf serve-cgi-bin \
        # Apache - remoteip module
        && a2enmod remoteip \
        && sed -i 's/%h/%a/g' /etc/apache2/apache2.conf \
        && a2enconf remoteip \
        # Apache - Hide version
        && sed -i 's/^ServerTokens OS$/ServerTokens Prod/g' /etc/apache2/conf-available/security.conf \
        && a2enconf servername \
        # Apache - Logging
        && sed -i -e 's/vhost_combined/combined/g' -e 's/other_vhosts_access/access/g' /etc/apache2/conf-available/other-vhosts-access-log.conf \
        # Apache- Prepare to be run as non root user
        && mkdir -p /var/lock/apache2 /var/run/apache2 \
        && chgrp -R 0 /var/lock/apache2 /var/log/apache2 /var/run/apache2 \
        && chmod -R g=u /var/lock/apache2 /var/log/apache2 /var/run/apache2 \
        && rm -f /var/log/apache2/*.log \
        && ln -s /proc/self/fd/2 /var/log/apache2/error.log \
        && ln -s /proc/self/fd/1 /var/log/apache2/access.log \
        && sed -i -e 's/80/8080/g' -e 's/443/8443/g' /etc/apache2/ports.conf; \
    fi
EXPOSE 8080 8443
# Php
RUN mkdir -p /var/run/php-fpm \
    && chgrp -R 0 /run /etc/service /var/run/php-fpm \
    && chmod -R g=u /etc/passwd /run /etc/service
# Cron - use supercronic (https://github.com/aptible/supercronic)
ENV SUPERCRONIC_VERSION=0.1.12
ENV SUPERCRONIC_SHA1SUM=048b95b48b708983effb2e5c935a1ef8483d9e3e
ADD https://github.com/aptible/supercronic/releases/download/v${SUPERCRONIC_VERSION}/supercronic-linux-amd64 /usr/local/bin/supercronic
RUN echo "${SUPERCRONIC_SHA1SUM}" "/usr/local/bin/supercronic" | sha1sum -c - \
    && chmod a+rx "/usr/local/bin/supercronic"
# Php - Set default php.ini config variables (can be override at runtime)
ENV PHP_CGI_FIX_PATHINFO=0
ENV PHP_UPLOAD_MAX_FILESIZE=2m
ENV PHP_POST_MAX_SIZE=8m
ENV PHP_MAX_EXECUTION_TIME=30
ENV PHP_MEMORY_LIMIT=64m
ENV PHP_REALPATH_CACHE_SIZE=256k
ENV PHP_REALPATH_CACHE_TTL=3600
ENV PHP_DEFAULT_SOCKET_TIMEOUT=60
# Php - Opcache extension configuration
ENV PHP_OPCACHE_ENABLE=1
ENV PHP_OPCACHE_ENABLE_CLI=1
ENV PHP_OPCACHE_MEMORY=64m
ENV PHP_OPCACHE_VALIDATE_TIMESTAMP=0
ENV PHP_OPCACHE_REVALIDATE_FREQ=600
# Php - update pecl protocols
RUN pecl channel-update pecl.php.net
# Php - Install extensions required for Yii 2.0 Framework
# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends libonig5 libonig-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-configure bcmath \
    && docker-php-ext-install \
        soap \
        zip \
        curl \
        bcmath \
        exif \
        gd \
        iconv \
        intl \
        mbstring \
        opcache \
        pdo_mysql \
        pdo_pgsql \
    && apt-get remove -y libonig-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # Php - Install image magick (see http://stackoverflow.com/a/8154466/291573 for usage of `printf`)
    # need to wait for https://github.com/Imagick/imagick/issues/358
    && if [ "${PHP_VERSION%%.*}" -lt 7 ]; then \
        printf "\n" | pecl install imagick; \
        docker-php-ext-enable imagick; \
    fi \
    # Php - Mongodb with SSL
    && apt-get update \
    && apt-get install -y --no-install-recommends libssl1.1 libssl-dev \
    && pecl uninstall mongodb \
    && pecl install mongodb \
    && apt-get remove -y libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Composer - Install composer
ENV COMPOSER_ALLOW_SUPERUSER=1
# hadolint ignore=DL3008
RUN curl -sS https://getcomposer.org/installer | php -- \
        --filename=composer.phar \
        --install-dir=/usr/local/bin \
    && chmod a+rx "/usr/local/bin/composer.phar" \
    # Php - Cache & Session support
    # Php - Redis
    && pecl install redis \
    && docker-php-ext-enable redis \
    # Php - Yaml
    && apt-get update \
    && apt-get install -y --no-install-recommends libyaml-dev libyaml-0-2 \
    && pecl install yaml \
    && docker-php-ext-enable yaml \
    && apt-get remove -y libyaml-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # Php - GMP
    && apt-get update \
    && apt-get install -y --no-install-recommends libgmp-dev libgmpxx4ldbl \
    && ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \
    && docker-php-ext-install gmp \
    && apt-get remove -y libgmp-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # Php - Gearman
    && apt-get update \
    && apt-get install -y --no-install-recommends git unzip libgearman-dev libgearman8 \
    && pecl install gearman \
    && apt-get remove -y libgearman-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # Php - pcntl
    && docker-php-ext-install pcntl
# Php - Xdebug
ENV PHP_ENABLE_XDEBUG=0
ENV PHP_XDEBUG_MODE=debug
RUN pecl install xdebug \
    # Php - Sockets
    && docker-php-ext-install sockets \
    # Php - Igbinary
    && pecl install igbinary \
    && docker-php-ext-enable igbinary \
    && echo "session.serialize_handler=igbinary" >> /usr/local/etc/php/conf.d/docker-php-ext-igbinary.ini \
    && pecl install apcu \
    && docker-php-ext-enable apcu \
    && echo "apc.serializer=igbinary" >> /usr/local/etc/php/conf.d/docker-php-ext-igbinary.ini \
    && echo "apc.enable_cli=1" >> /usr/local/etc/php/conf.d/docker-php-ext-apcu.ini
# Pinpoint - Php module configuration
ENV PINPOINT_COLLECTOR_AGENT_VERSION 0.4.5
ENV PINPOINT_PHP_COLLETOR_AGENT_HOST tcp:pinpoint-collector-agent:8080
ENV PINPOINT_PHP_SEND_SPAN_TIMEOUT_MS 100
ENV PINPOINT_PHP_TRACE_LIMIT -1
# Pinpoint - Install pinpoint php module
# hadolint ignore=DL3003,DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends cmake \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/naver/pinpoint-c-agent.git /pinpoint-c-agent/ \
    && cd /pinpoint-c-agent \
    && git checkout v${PINPOINT_COLLECTOR_AGENT_VERSION} \
    && phpize \
    && ./configure \
    && make \
    && make test TESTS=src/PHP/tests/ \
    && make install \
    && rm -rf /pinpoint-c-agent \
    # Php - Disable extension should be enable by user if needed
    && chmod g=u /usr/local/etc/php/conf.d/ \
    && chown root:root -R /usr/local/etc/php/conf.d \
    && rm -f /usr/local/etc/php/conf.d/docker-php-ext-exif.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-gd.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-gearman.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-imagick.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-pcntl.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-pdo_mysql.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-pdo_pgsql.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-soap.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-sockets.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
            /usr/local/etc/php/conf.d/docker-php-ext-zip.ini \
    # System - Clean apt
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir -p ${APP_DIR} \
    && chmod a+rx /docker-bin/*.sh \
    && /docker-bin/docker-build.sh
WORKDIR ${APP_DIR}
USER ${USER_ID}
ENTRYPOINT ["/docker-bin/docker-entrypoint.sh"]
