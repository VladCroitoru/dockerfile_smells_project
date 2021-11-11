FROM alpine:edge
MAINTAINER Jesus Macias <jmacias@solidgear.es>

# CREDITS
# https://github.com/smebberson/docker-alpine
# https://github.com/just-containers/base-alpine
# https://github.com/bytepark/alpine-nginx-php7

# s6 overlay
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk --update upgrade && apk add curl

RUN curl -L -s https://github.com/just-containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz \
  | tar xvzf - -C / 

# Install packages
RUN apk add php7 php7-fpm openssl php7-xml php7-xsl php7-pdo php7-pdo_mysql php7-mcrypt php7-curl php7-json php7-fpm php7-phar php7-openssl php7-mysqli php7-ctype php7-opcache php7-mbstring php7-session php7-pdo_sqlite php7-sqlite3 php7-pcntl php7-ldap php7-soap php7-gd php7-zip php7-zlib php7-xmlreader nginx mysql mysql-client bash git openssh rsync pwgen netcat-openbsd

#Generate Host ssh Keys
RUN mkdir -p ~root/.ssh && chmod 700 ~root/.ssh/ && \
    echo -e "Port 22\n" >> /etc/ssh/sshd_config && \
    cp -a /etc/ssh /etc/ssh.cache

# Update root password
# CHANGE IT # to something like root:ASdSAdfÑ3
RUN echo "root:root" | chpasswd

# Enable ssh for root
RUN printf "\\nPermitRootLogin yes" >> /etc/ssh/sshd_config
# Enable this option to prevent SSH drop connections
RUN printf "\\nClientAliveInterval 15\\nClientAliveCountMax 8" >> /etc/ssh/sshd_config

# Exposed ENV
ENV MYSQL_PASS="root"

# Configure MySQL
COPY config/my.cnf /etc/mysql/my.cnf

# Configure nginx
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/log/nginx

# Configure PHP-FPM
COPY config/fpm-pool.conf /etc/php7/php-fpm.d/zzz_custom.conf
COPY config/php.ini /etc/php7/conf.d/zzz_custom.ini
RUN mkdir -p /var/log/php-fpm
RUN touch /var/log/php-fpm/fpm-error.log

# Small fixes
RUN ln -s /etc/php7 /etc/php && \
    ln -s /usr/bin/php7 /usr/bin/php && \
    ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \
    ln -s /usr/lib/php7 /usr/lib/php

# Install composer global bin
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# Create nginx document pat
RUN mkdir -p /var/www/html

# Clean packages cache
RUN rm -rf /var/cache/apk/*

# root filesystem (S6 config files)
COPY rootfs /

EXPOSE 80 22

# S6 init script
ENTRYPOINT [ "/init" ]
