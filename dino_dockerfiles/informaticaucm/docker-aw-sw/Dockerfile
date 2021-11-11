# School of Computer Engineering at Complutense University
#
# LAMP stack for student projects

FROM php:7.3-apache-buster
LABEL maintainer="Ivan Martinez-Ortiz <imartinez@fdi.ucm.es>"

# Optimize recurrent builds by using a helper container runing apt-cache
ARG USE_APT_CACHE
ENV USE_APT_CACHE ${USE_APT_CACHE}
RUN ([ ! -z $USE_APT_CACHE ] && echo 'Acquire::http { Proxy "http://172.17.0.1:3142"; };' >> /etc/apt/apt.conf.d/01proxy \
    && echo 'Acquire::HTTPS::Proxy "false";' >> /etc/apt/apt.conf.d/01proxy) || true

#
# Configure locale es_ES.UTF-8
#
RUN set -ex; \
    apt-get update; apt-get install -y \
        locales \
    ; \
# installation cleanup
    rm -rf /var/lib/apt/lists/*; \
    localedef -i es_ES -c -f UTF-8 -A /usr/share/locale/locale.alias es_ES.UTF-8

ENV LANG es_ES.utf8

RUN set -eux; \
    \
    savedAptMark="$(apt-mark showmanual)"; \
    \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        libc-client-dev \
        libfreetype6-dev \
        libmcrypt-dev \
        libpng-dev \
        libjpeg-dev \
        libwebp-dev \
        libxpm-dev \
        zlib1g-dev \
        libtidy-dev \
        libbz2-dev \
        libzip-dev \
        libyaml-dev \
# pecl_http raphf
        libcurl4-openssl-dev \
        libevent-dev \
        libbrotli-dev \
        libicu-dev \
    ; \
    \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/  --with-png-dir=/usr --with-jpeg-dir=/usr --with-webp-dir=/usr --with-xpm-dir=/usr; \
    docker-php-ext-install -j$(nproc) gd; \
    docker-php-ext-install -j$(nproc) mysqli pdo pdo_mysql opcache bz2 zip tidy; \
    pecl install apcu-5.1.18; \
    pecl install xdebug-2.9.4; \
    pecl install yaml-2.0.4; \
# https://mdref.m6w6.name/http
# https://github.com/m6w6/ext-http/
    pecl install raphf-2.0.1; \
    pecl install propro-2.1.0; \
    docker-php-ext-enable apcu xdebug yaml raphf propro; \
    pecl install pecl_http-3.2.3; \
    docker-php-ext-enable http; \
    \
    apt-mark auto '.*' > /dev/null; \
    apt-mark manual $savedAptMark; \
    ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
        | awk '/=>/ { print $3 }' \
        | sort -u \
        | xargs -r dpkg-query -S \
        | cut -d: -f1 \
        | sort -u \
        | xargs -rt apt-mark manual; \
    \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \
    php --version


# Configure PHP sessions storage
RUN set -eux; \
    mkdir -p /var/lib/php/sessions; \
    chown root:www-data /var/lib/php/sessions; \
    chmod 770 /var/lib/php/sessions; \
    { \
        echo 'session.save_path="/var/lib/php/sessions"'; \
    } > "$PHP_INI_DIR/conf.d/sessions.ini"

# Configure PHP error logging to /dev/stdout
RUN set -eux; \
    mkdir -p /var/log/php; \
    chown root:www-data /var/log/php; \
    chmod 770 /var/log/php; \
    { \
# https://www.php.net/manual/en/errorfunc.constants.php
# https://github.com/docker-library/wordpress/issues/420#issuecomment-517839670
		echo 'error_reporting = E_ERROR | E_WARNING | E_PARSE | E_CORE_ERROR | E_CORE_WARNING | E_COMPILE_ERROR | E_COMPILE_WARNING | E_RECOVERABLE_ERROR'; \
		echo 'display_errors = Off'; \
		echo 'display_startup_errors = Off'; \
		echo 'log_errors = On'; \
		echo 'error_log = /var/log/php/errors.log'; \
		echo 'log_errors_max_len = 1024'; \
		echo 'ignore_repeated_errors = On'; \
		echo 'ignore_repeated_source = Off'; \
		echo 'html_errors = Off'; \
    } > "$PHP_INI_DIR/conf.d/error-log.ini"

RUN set -eux; \
    { \
        echo 'upload_max_filesize = 10M'; \
        echo 'post_max_size = 10M'; \
    } > "$PHP_INI_DIR/conf.d/upload.ini"

RUN set -ex; \
    . "$APACHE_ENVVARS"; \
# Reduce throughput to keep resource consumption low    
    sed -r -i -e 's/^\s+StartServers.*/StartServers\t\t1/g' "$APACHE_CONFDIR/mods-enabled/mpm_prefork.conf"; \
    sed -r -i -e 's/^\s+MinSpareServers.*/MinSpareServers\t\t1/g' "$APACHE_CONFDIR/mods-enabled/mpm_prefork.conf"; \
    sed -r -i -e 's/^\s+MaxSpareServers.*/MaxSpareServers\t\t5/g' "$APACHE_CONFDIR/mods-enabled/mpm_prefork.conf"; \
    sed -r -i -e 's/^\s+MaxRequestWorkers.*/MaxRequestWorkers\t50/g' "$APACHE_CONFDIR/mods-enabled/mpm_prefork.conf"; \
# Enable URL rewriting
    a2enmod rewrite; \
# Configure apache behind a reverse proxy
    a2enmod remoteip; \
# Configure apache logs to use the client IP provided by the reverse proxy
    sed -r -i -e 's/%h/%a/g' "$APACHE_CONFDIR/apache2.conf";

# Configure apache behind a reverse proxy (simplified to allow private IPv4 addresses as an internal proxy)
RUN set -ex; \
    . "$APACHE_ENVVARS"; \
    { \
        echo 'RemoteIPHeader X-RealIp'; \
        echo 'RemoteIPInternalProxy 10.0.0.0/8'; \
        echo 'RemoteIPInternalProxy 172.16.0.0/12'; \
        echo 'RemoteIPInternalProxy 192.168.0.0/16'; \
        echo 'RemoteIPInternalProxy 127.0.0.0/8'; \
    } | tee "$APACHE_CONFDIR/conf-available/remoteip.conf"; \
    a2enconf remoteip

# Restore Apache2 logs to files
RUN set -ex; \
    . "$APACHE_ENVVARS"; \
    rm -fr "$APACHE_LOG_DIR/error.log"; \
    rm -fr "$APACHE_LOG_DIR/access.log"; \
    rm -fr "$APACHE_LOG_DIR/other_vhosts_access.log"; \
    touch "$APACHE_LOG_DIR/error.log"; \
    touch "$APACHE_LOG_DIR/access.log"; \
    touch "$APACHE_LOG_DIR/other_vhosts_access.log"; \
    chown -R --no-dereference "$APACHE_RUN_USER:$APACHE_RUN_GROUP" "$APACHE_LOG_DIR"

#
# install s6-overlay
#
ENV S6_OVERLAY_VERSION 1.22.1.0

RUN set -ex; \
    \
    fetchDeps=' \
        ca-certificates \
        curl \
        gnupg \
    '; \
    apt-get update; apt-get -y --no-install-recommends install $fetchDeps; \
# fetch s6-overlay archive and signature
    curl -fsSL -o /tmp/s6.tgz \
        https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz; \
    curl -fsSL -o /tmp/s6.sig \
        https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz.sig; \
# gpg verification    
    export GNUPGHOME="$(mktemp -d)"; \
    curl -sSL https://keybase.io/justcontainers/key.asc | gpg --import; \
    gpg --batch --verify /tmp/s6.sig /tmp/s6.tgz; \
# extract s6-overlay archive
    tar -xzf /tmp/s6.tgz -C /; \
# installation cleanup
    apt-get purge -y --auto-remove $fetchDeps; \
    rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*


#
# Install and configure OpenSSH
#
RUN set -ex; \
    apt-get update; apt-get install -y --no-install-recommends \
        openssh-server \
    ; \
# Configure SSH
    sed -r -i -e 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config; \
    sed -r -i -e 's/#PidFile.*/PidFile \/var\/run\/sshd\/pid/' /etc/ssh/sshd_config; \
# SSH login fix. Otherwise user is kicked off after login
    sed 's/session\s*required\s*pam_loginuid.so/session optional pam_loginuid.so/g' -i /etc/pam.d/sshd; \
    mkdir /var/run/sshd && chmod 0755 /var/run/sshd; \
# installation cleanup
    rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN set -xe; \
    \
    apt-get update; apt-get -y --no-install-recommends install \
        less \
        vim \
        nano \
        openssl \
        tmux \
        zip \
        unzip \
    ; \
    rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Extra cleanup
RUN set -xe;\
    rm -rf /var/log/dpkg.log; \
    rm -rf /var/log/alternatives.log


RUN set -xe;\
    mkdir -p /templates/folders; \
    mkdir -p /templates/files; \
    for dir in \
        /root \
        /etc/apache2 \
        /etc/ssh \
        /usr/local/etc/php \
        /run \
        /var/log \
        /var/www \
    ; do \
        tar -cf - ${dir} 2> /dev/null | ( tar -C /templates/folders -xpf - > /dev/null 2>&1); \
        echo "${dir}" >> /templates/folders-to-restore; \
    done; \
    for file in \
        /etc/shadow \
    ; do \
        tar -cf - ${file} 2> /dev/null | ( tar -C /templates/files -xpf - > /dev/null 2>&1); \
        echo "${file}" >> /templates/files-to-restore; \
    done; \
# Remove server keys
    find /templates/folders/etc/ssh -name 'ssh_host_*' -exec rm {} \;

COPY overlay /

EXPOSE 80/tcp 22/tcp

ENTRYPOINT ["/init"]