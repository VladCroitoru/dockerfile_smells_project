FROM alpine:edge

LABEL maintainer "j.zelger@techdivision.com"

# copy all filesystem relevant files
COPY fs /tmp/

# install everything needed
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    # install packages
    apk -U --no-cache add \
        htop bash shadow vim wget ca-certificates openssl rsync curl git supervisor graphicsmagick postfix \
        openjdk8-jre mysql mysql-client nginx varnish redis xz tar nodejs \
        libpng libpng-dev libjpeg-turbo-dev libwebp-dev zlib-dev libxpm-dev \
        php7 php7-fpm php7-curl php7-dom php7-gd php7-iconv php7-mcrypt php7-pdo php7-pdo_mysql \
        php7-soap php7-ctype php7-json php7-openssl php7-zlib php7-intl php7-xsl php7-zip php7-bcmath \
        php7-mbstring php7-phar php7-session php7-mongodb php7-xdebug php7-mysqli php7-ldap \
        erlang erlang-mnesia erlang-public-key erlang-crypto erlang-ssl erlang-sasl erlang-asn1 erlang-inets \
        erlang-os-mon erlang-xmerl erlang-eldap erlang-syntax-tools && \

    # init mysql
    mysql_install_db --user=mysql 2> /dev/null && \
    # prepare filesystem and permissions
    mkdir -p /run/mysqld/ && \
    chown mysql /run/mysqld/ && \

    # install elasticsearch
    curl -Ls https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-2.4.2.tar.gz | tar -xz -C /usr/share && \
    # rename without version number
    mv /usr/share/elasticsearch-2.4.2 /usr/share/elasticsearch && \
    # prepare needed directories
    mkdir -p /usr/share/elasticsearch/data/elasticsearch/nodes /usr/share/elasticsearch/logs /usr/share/elasticsearch/config/scripts && \
    # install useful plugins
    /usr/share/elasticsearch/bin/plugin install analysis-phonetic && \
    /usr/share/elasticsearch/bin/plugin install analysis-icu && \

    # install rabbit mq
    curl -sSL https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-generic-unix-3.6.1.tar.xz | tar -xJ -C / --strip-components 1 && \
    rm -rf /share/**/rabbitmq*.xz && \
    mkdir -p /data/rabbitmq && \

    # install latest gulp-cli tools globally
    npm install -g --depth 0 gulpjs/gulp-cli && \

    # link php7 to php
    ln -s /usr/bin/php7 /usr/bin/php && \

    # install composer
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \

    # copy usr and etc files
    cp -r /tmp/usr / && \
    cp -r /tmp/etc / && \

    # init root user for mysql
    mysql_start && \
    mysql -e "DELETE FROM mysql.user; CREATE USER 'root'@'%'; GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION; DROP DATABASE IF EXISTS test; FLUSH PRIVILEGES;" && \
    mysql_stop && \

    # cleanup
    rm -rf /var/cache/apk/* /tmp/*

# define cmd
CMD ["/usr/bin/supervisord", "--nodaemon"]
