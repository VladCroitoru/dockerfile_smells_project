FROM gabrieltakacs/alpine:latest
MAINTAINER Gabriel Takács <gtakacs@gtakacs.sk>

# Copy and add files first (to make dockerhub autobuild working: https://forums.docker.com/t/automated-docker-build-fails/22831/14)
COPY run.sh /run.sh

# Install Apache2, supervisor, PHP 5.6
RUN apk --no-cache --update add \
    apache2 \
    supervisor \
    php5 \
    php5-xml \
    php5-pgsql \
    php5-mysql \
    php5-mysqli \
    php5-pdo_mysql \
    php5-mcrypt \
    php5-opcache \
    php5-gd \
    php5-curl \
    php5-json \
    php5-phar \
    php5-openssl \
    php5-ctype \
    php5-zip \
    php5-dev \
    php5-iconv \
    php5-soap \
    php5-zlib \
    php5-dom \
    php5-apache2 \
    php5-bcmath \
    php5-posix \
    php5-memcache \
    php5-memcached \
    php5-imagick \
    memcached \
    imagemagick \
    postfix

# Install NPM & NPM modules (gulp, bower)
RUN apk --no-cache --update add \
    nodejs
RUN npm install  -g \
    gulp \
    bower

# php5-fpm configuration
COPY php5/php.ini /etc/php5/php.ini

# Install composer
ENV COMPOSER_HOME=/composer
RUN mkdir /composer \
    && curl -sS https://getcomposer.org/download/1.2.1/composer.phar > composer.phar

RUN mkdir -p /opt/composer \
    && mv composer.phar /usr/local/bin/composer \
    && chmod 777 /usr/local/bin/composer

# Configure xdebug
#RUN echo 'zend_extension="/usr/lib/php7/modules/xdebug.so"' >> /etc/php7/php.ini \
#    && echo "xdebug.remote_enable=on" >> /etc/php7/php.ini \
#    && echo "xdebug.remote_autostart=off" >> /etc/php7/php.ini \
#    && echo "xdebug.remote_connect_back=0" >> /etc/php7/php.ini \
#    && echo "xdebug.remote_port=9001" >> /etc/php7/php.ini \
#    && echo "xdebug.remote_handler=dbgp" >> /etc/php7/php.ini \
#    && echo "xdebug.remote_host=192.168.65.1" >> /etc/php7/php.ini
#     (Only for MAC users) Fill IP address from:
    # cat /Users/gtakacs/Library/Containers/com.docker.docker/Data/database/com.docker.driver.amd64-linux/slirp/host
    # Source topic on Docker forums: https://forums.docker.com/t/ip-address-for-xdebug/10460/22

# Copy Supervisor config file
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN adduser -s /sbin/nologin -D -G www-data www-data
RUN mkdir /run/apache2
RUN chown -R www-data:www-data /run/apache2/

# Copy Apache2 config
COPY apache2/httpd.conf /etc/apache2/httpd.conf

# Make run file executable
RUN chmod a+x /run.sh

RUN chmod a+rw /var/log/apache2

#RUN apk --no-cache --update add icu icu-libs icu-dev
#RUN docker-php-ext-install intl

EXPOSE 80 443 25
CMD ["/run.sh"]
WORKDIR /var/www/web
