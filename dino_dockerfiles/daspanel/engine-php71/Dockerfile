FROM golang:1.9-alpine3.6 as builder-caddy
LABEL maintainer="ulrich.schreiner@gmail.com"

ENV CADDY_VERSION v0.10.10

# Inject files in container file system
COPY caddy-build /caddy-build

RUN apk --no-cache update \
    && apk --no-cache --update add git bash \
    && cd /caddy-build \
    && env OS=linux ARCH=amd64 ./build_caddy.sh \
    && ls -la /caddy-build/caddy

FROM daspanel/engine-base-dev:dev
MAINTAINER Abner G Jacobsen - http://daspanel.com <admin@daspanel.com>

# Thanks:
#   https://github.com/openbridge/ob_php-fpm

# Copy bynaries build before
COPY --from=builder-caddy /caddy-build/caddy /usr/sbin/caddy

# Parse Daspanel common arguments for the build command.
ARG VERSION
ARG VCS_URL
ARG VCS_REF
ARG BUILD_DATE
ARG S6_OVERLAY_VERSION=v1.19.1.1
ARG DASPANEL_IMG_NAME=engine-php71
ARG DASPANEL_OS_VERSION=alpine3.6

# Parse Container specific arguments for the build command.
ARG GOTTY_URL="https://github.com/yudai/gotty/releases/download/v2.0.0-alpha.3/gotty_2.0.0-alpha.3_linux_amd64.tar.gz"
ARG WP_CLI_VERSION="1.4.1"
ARG WPCLI_URL="https://github.com/wp-cli/wp-cli/releases/download/v${WP_CLI_VERSION}/wp-cli-${WP_CLI_VERSION}.phar"

# PHP minimal modules to install - run's Worpress, Grav and others
ARG PHP_MINIMAL="php7-fpm php7 php7-common php7-pear php7-phar php7-posix \
    php7-mbstring php7-ctype php7-iconv php7-bcmath php7-bz2 php7-calendar \
    php7-gettext php7-pspell php7-recode php7-gmp php7-fileinfo php7-session \
    php7-zip php7-zlib php7-intl php7-mcrypt \ 
    php7-json php7-dom php7-soap php7-xsl php7-xml \
    php7-tokenizer php7-xmlwriter php7-simplexml php7-xmlreader \
    php7-curl php7-openssl php7-sockets php7-imap php7-ftp \
    php7-mysqlnd php7-mysqli \
    php7-pdo php7-pdo_mysql php7-pdo_pgsql php7-pdo_sqlite \
    php7-exif php7-gd \
    php7-apcu php7-opcache php7-pcntl \
    php7-redis@testing php7-memcached"

ARG PECL_MINIMAL="yaml-2.0.0"

ARG PHP_MODULES="php7-pgsql php7-sqlite3 php7-memcached php7-mailparse \
    php7-enchant \
    php7-tidy \
    php7-ldap \
    php7-zmq \
    php7-amqp \
    php7-mailparse \
    php7-pdo_dblib"
    
ARG PHP_MODULES_EXTRA="ffmpeg php7-imagick"

ARG PHP_XDEBUG="php7-xdebug"
ARG PHP_PHPDBG="php7-phpdbg"

ARG PHP_MODULES_BANNED="php7-sysvsem php7-sysvshm php7-xmlrpc php7-shmop \
    php7-snmp php7-sysvmsg php7-odbc php7-pdo_odbc php7-ldap php7-apache2 \
    php7-cgi php7-dba php7-embed php7-litespeed php7-doc"

# Set default env variables
ENV \
    # Stop container initialization if error occurs in cont-init.d, fix-attrs.d script's
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    # Timezone
    TZ="UTC" \
    # DASPANEL defaults
    DASPANEL_WAIT_FOR_API="YES"

# A little bit of metadata management.
# See http://label-schema.org/  
LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$VERSION \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name="daspanel/engine-php71" \
      org.label-schema.description="This service provides HTTP php 7.1 engine server to Daspanel sites."

ENV TERM=xterm-256color
ENV VAR_PREFIX=/var/run
ENV LOG_PREFIX=/var/log/php-fpm7
ENV TEMP_PREFIX=/tmp
ENV CACHE_PREFIX=/var/cache

# Solves: https://github.com/wp-cli/wp-cli/issues/4246#issuecomment-325774849
# less: unrecognized option: r
# BusyBox v1.26.2 (2017-06-11 06:38:32 GMT) multi-call binary.
ENV PAGER='more' 

# Inject files in container file system
COPY rootfs /

RUN set -x \

    # Initial OS bootstrap - required
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/00_base \

    # Install Daspanel base - common layer for all container's independent of the OS and init system
    && wget -O /tmp/opt-daspanel.zip "https://github.com/daspanel/rootfs-base/releases/download/0.1.0/opt-daspanel.zip" \
    && unzip -o -d / /tmp/opt-daspanel.zip \

    # Install Daspanel bootstrap for Alpine Linux with S6 Overlay Init system
    && wget -O /tmp/alpine-s6.zip "https://github.com/daspanel/rootfs-base/releases/download/0.1.0/alpine-s6.zip" \
    && unzip -o -d / /tmp/alpine-s6.zip \

    # Bootstrap the system (TBD)

    # Install s6 overlay init system
    && wget https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz --no-check-certificate -O /tmp/s6-overlay.tar.gz \
    && tar xvfz /tmp/s6-overlay.tar.gz -C / \
    && rm -f /tmp/s6-overlay.tar.gz \

    # ensure www-data user exists
    && addgroup -g 82 -S www-data \
    && adduser -u 82 -D -S -h /home/www-data -s /sbin/nologin -G www-data www-data \

    # Install specific OS packages needed by this image
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/99_install_pkgs "git" \

    # Activate additional repositories
    && echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories \
    && echo '@community http://nl.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories \

    # Install build environment packages
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/00_buildenv \

    # Install PHP and modules avaiable on the default repositories of this Linux distro
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/99_install_pkgs "${PHP_MINIMAL}" \
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/99_install_pkgs "${PHP_MODULES}" \
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/99_install_pkgs "${PHP_MODULES_EXTRA}" \
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/99_install_pkgs "${PHP_PHPDBG}" \
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/99_install_pkgs "${PHP_XDEBUG}" \

    # Install PHP Composer
    && curl -sS https://getcomposer.org/installer -o /tmp/composer-install \
    && php /tmp/composer-install --install-dir=/usr/local/bin --filename=composer \
    && rm /tmp/composer-install \

    # Install PHPUnit
    && curl -sSL https://phar.phpunit.de/phpunit-6.2.phar -o /usr/local/bin/phpunit \
    && chmod +x /usr/local/bin/phpunit \

    # PECL fix
    # Bug Fix: 
    # https://serverfault.com/questions/589877/pecl-command-produces-long-list-of-errors
    # https://bugs.alpinelinux.org/issues/5378
    # Patch pecl command
    && sed -i -e 's/\(PHP -C\) -n/\1/g' /usr/bin/pecl \
    && mkdir -p /tmp/pear/cache \

    # Cleanup after phpizing
    #&& rm -rf /usr/include/php7 /usr/lib/php7/build \

    # Remove build environment packages
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/09_cleanbuildenv \

    # Install wp-cli
    && curl --progress-bar --show-error --fail --location \
        --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o /usr/local/bin/wp \
        "${WPCLI_URL}" \
    && chmod 0755 /usr/local/bin/wp \

    # Install gotty
    && curl --silent --show-error --fail --location \
        --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o /tmp/gotty.tar.gz \
        "${GOTTY_URL}" \
    && tar -C /usr/sbin -xvzf /tmp/gotty.tar.gz \
    && chmod 0755 /usr/sbin/gotty \
    && mkdir /lib64 \
    && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \

    # Install Caddy
    && chmod 0755 /usr/sbin/caddy \
    && setcap "cap_net_bind_service=+ep" /usr/sbin/caddy \

    # Cleanup
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/*

# Let's S6 control the init system
ENTRYPOINT ["/init"]
CMD []

# Expose ports for the service
EXPOSE 443

