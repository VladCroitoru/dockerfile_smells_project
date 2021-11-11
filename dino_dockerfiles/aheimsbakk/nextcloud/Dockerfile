# Base it on old stable 
FROM alpine:3.6

# This is me
MAINTAINER Arnulf Heimsbakk <arnulf.heimsbakk@gmail.com>

# REDIS
ENV PHP_REDIS_VER 3.1.2  
ENV REDIS_ENABLED ""
ENV REDIS_SERVER redis
ENV REDIS_PORT 6379

# Trusted domains
ENV TRUSTED_DOMAINS ""

# Change owerwrite protocol to https if you use HTTPS proxy
ENV OVERWRITEPROTOCOL ""

# Set home
VOLUME /var/www/nextcloud

# Add entrypoint 
COPY docker-entrypoint.sh /
COPY fix-permissions.sh /

# Set workdir
WORKDIR /var/www/nextcloud

# Install packages
RUN apk update; apk add wget \ 
    # Reccomended packages from https://docs.nextcloud.com/server/9/admin_manual/installation/source_installation.html 
    bzip2 apache2 php7 php7-apache2 php7-gd php7-json php7-curl php7-intl \
    php7-mcrypt php7-imagick samba-client php7-xmlwriter php7-mbstring \ 
    php7-simplexml php7-fileinfo \
    # Install database drivers 
    php7-sqlite3 php7-pdo_sqlite php7-pdo_mysql php7-pgsql php7-pdo_pgsql \
    # Auth and storage 
    php7-ldap php7-imap php7-gmp \
    # For server performance 
    php7-apcu php7-memcached php7-redis php7-opcache \
    # Install ffmpeg
    ffmpeg \
    # Gnupg and bash
    gnupg bash \
    # Extra packages for occ command
    php7-posix php7-pdo php7-openssl php7-pcntl php7-zlib php7-ctype \ 
    php7-xml php7-xmlreader php7-dom php7-zip php7-iconv

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
        echo 'opcache.memory_consumption=128'; \
        echo 'opcache.interned_strings_buffer=8'; \
        echo 'opcache.max_accelerated_files=10000'; \
        echo 'opcache.revalidate_freq=1'; \
        echo 'opcache.fast_shutdown=1'; \
        echo 'opcache.save_comments=1'; \
        echo 'opcache.enable_cli=1'; \
    } >> /etc/php7/conf.d/00_opcache.ini

## Nextcloud apache config
RUN { \
        echo 'Alias / "/var/www/nextcloud/"'; \
        echo 'ServerName localhost'; \
        echo 'RemoteIPHeader X-Forwarded-For'; \
        echo '<Directory /var/www/nextcloud/>'; \
        echo '  Require all granted'; \
        echo '  Options +FollowSymlinks'; \
        echo '  AllowOverride All'; \
        echo ' <IfModule mod_dav.c>'; \
        echo '  Dav off'; \
        echo ' </IfModule>'; \
        echo ' SetEnv HOME /var/www/nextcloud'; \
        echo ' SetEnv HTTP_HOME /var/www/nextcloud'; \
        echo '</Directory>'; \
    } > /etc/apache2/conf.d/nextcloud.conf

# Fix apache2, and remove default apache vserver + increase php memory limit
RUN mkdir /run/apache2; \
    sed -i '/remoteip_module/s/#//' /etc/apache2/httpd.conf; \
    sed -i '/^DocumentRoot/d' /etc/apache2/httpd.conf; \
    sed -i '/<Directory ..var.www.*/,/<.Directory.*/d' /etc/apache2/httpd.conf; \
    sed -i '/^memory_limit/s/128/256/' /etc/php7/php.ini

# Redirect Apache2 logs
RUN ln -sf /dev/stdout /var/log/apache2/access.log
RUN ln -sf /dev/stderr /var/log/apache2/error.log

# Define Nexcloud version
ENV NEXTCLOUD_VERSION 12.0.4

# Download and verify Nextcloud, as in https://github.com/docker-library/owncloud/blob/master/9.0/apache/Dockerfile
RUN wget -O nextcloud.tar.bz2 \
        "https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2" \
    && wget -O nextcloud.tar.bz2.asc \
        "https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
# gpg key from https://nextcloud.com/nextcloud.asc
    && gpg --keyserver pool.sks-keyservers.net --recv-keys 28806A878AE423A28372792ED75899B9A724937A \
    && gpg --batch --verify nextcloud.tar.bz2.asc nextcloud.tar.bz2 \
    && rm -fr "$GNUPGHOME" nextcloud.tar.bz2.asc  \
    && mkdir /usr/src \
    && tar -xjf nextcloud.tar.bz2 -C /usr/src/ \
    && rm nextcloud.tar.bz2

## Run entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["httpd", "-DFOREGROUND"]

