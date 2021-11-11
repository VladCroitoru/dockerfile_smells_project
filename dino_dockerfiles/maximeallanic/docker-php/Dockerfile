FROM nimmis/alpine-micro:latest

RUN apk update
RUN apk add \
    nginx \
    curl \
    php7-common=~7.1 \
    php7-xml \
    php7-intl \
    php7-pgsql \
    php7-mbstring \
    php7-json \
    php7-phar \
    php7-apcu \
    php7-dom \
    php7-openssl \
    php7-fpm \
    php7-xmlwriter \
    php7-tokenizer \
    php7-common \
    php7-calendar \
    php7-pdo \
    php7-fileinfo \
    php7-pdo_pgsql \
    php7-ctype \
    php7-session \
    php7-iconv \
    php7-posix \
    php7-simplexml \
    php7-xdebug \
    php7-apcu \
    php7-curl \
    php7-zip \
    php7-pcntl \
    bind-tools \
    apache-ant \
    openjdk8 \
    git \
    libc6-compat \
    gcompat


# Install composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Define custom config for apache
#RUN sed -i '/LoadModule rewrite_module/s/^#//g' /etc/apache2/httpd.conf
#RUN sed -i '/\/web\/html/s//\/web\/html\/web/g' /etc/apache2/httpd.conf
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/service/nginx
COPY conf/nginx/run /etc/service/nginx/run
RUN chmod 777 /etc/service/nginx/run

# Define custom config for php
RUN echo -e "\napc.enabled=1\n \
            apc.shm_size=64M\n \
            apc.enable_cli=1" >> /etc/php7/conf.d/apcu.ini
RUN echo -e '\nshort_open_tag = Off\n \
            log_errors = On\n \
            max_input_time=-1\n \
            max_execution_time=0\n \
            memory_limit=-1\n \
            error_reporting = E_ALL\n \
            display_errors = On\n \
            error_log = /proc/self/fd/2\n \
            realpath_cache_size = 4M\n \
            realpath_cache_ttl = 7200' >> /etc/php7/php.ini

RUN echo -e '[blackfire]\n\
    extension=blackfire.so\n\
    blackfire.agent_socket = unix:///var/run/blackfire/agent.sock\n\
    blackfire.agent_timeout = 0.25\n\
    blackfire.log_level = 4\n\
    blackfire.log_file = /tmp/blackfire.log\n\
    blackfire.server_id = BLACKFIRE_SERVER_ID\n\
    blackfire.server_token = BLACKFIRE_SERVER_TOKEN' >> /etc/php7/conf.d/01_blackfire.ini.disabled

COPY conf/php-fpm/xdebug.ini /etc/php7/conf.d/xdebug.ini.disabled
COPY conf/php-fpm/*.conf /etc/php7/php-fpm.d/
RUN mkdir /etc/service/php-fpm
COPY conf/php-fpm/run /etc/service/php-fpm/run
RUN chmod 777 /etc/service/php-fpm/run

RUN wget https://packages.blackfire.io/binaries/blackfire-agent/1.27.0/blackfire-agent-linux_static_amd64 -O /usr/local/bin/blackfire-agent
RUN chmod 777 /usr/local/bin/blackfire-agent
COPY conf/black-fire/config.conf /etc/blackfire/agent
RUN mkdir /etc/service/black-fire
COPY conf/black-fire/run /etc/service/black-fire/run
RUN chmod 777 /etc/service/black-fire/run
RUN mkdir -p /usr/lib/php7/modules
RUN wget https://packages.blackfire.io/binaries/blackfire-php/1.26.3/blackfire-php-alpine_amd64-php-72.so -O /usr/lib/php7/modules/blackfire.so
RUN chmod 755 /usr/lib/php7/modules/blackfire.so
RUN mkdir /var/run/blackfire/


COPY conf/profile /root/.profile
RUN chmod 777 /root/.profile

RUN mkdir -p /run/nginx
RUN mkdir -p /web/logs
RUN mkdir -p /web/run
RUN mkdir -p /dev/shm/cache
RUN chmod -R 777 /run
RUN chmod -R 777 /web
RUN chmod -R 777 /var/log

ENTRYPOINT ["/bin/sh", "-l", "-c"]

CMD ["/boot.sh"]

WORKDIR /web/html
