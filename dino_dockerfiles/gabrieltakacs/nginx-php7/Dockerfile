FROM gabrieltakacs/ubuntu-xenial:1.0.0
MAINTAINER Gabriel Takács <gtakacs@gtakacs.sk>

# Install nginx, supservisor, PHP 7
RUN apt-get update && \
    apt-get -y install \
    nginx \
    supervisor \
    php7.0 \
    php7.0-fpm \
    php7.0-xml \
    php7.0-pgsql \
    php7.0-mysqli \
    php7.0-mcrypt \
    php7.0-opcache \
    php7.0-gd \
    php7.0-curl \
    php7.0-json \
    php7.0-phar \
    php7.0-ctype \
    php7.0-mbstring \
    php7.0-zip \
    php7.0-dev \
    php-xdebug \
    php7.0-dom \
    php7.0-posix \
    memcached \
    imagemagick \
    postfix

# Install NPM & NPM modules (gulp, bower)
RUN apt-get -y install nodejs-legacy nodejs npm
RUN npm install -g \
    gulp \
    bower

# Install composer
ENV COMPOSER_HOME=/composer
RUN mkdir /composer \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/bin/composer

# php7-fpm configuration
RUN adduser --shell /sbin/nologin --disabled-login www-data www-data
COPY php7/php-fpm.conf /etc/php7/php-fpm.conf
COPY php7/www.conf /etc/php7/php-fpm.d/www.conf
RUN mkdir /run/php/

RUN mkdir /var/run/sshd
RUN chmod 0755 /var/run/sshd

# Copy Supervisor config file
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Add nginx configuration files
COPY nginx/nginx.conf /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/vhosts

# Copy and add files first (to make dockerhub autobuild working: https://forums.docker.com/t/automated-docker-build-fails/22831/14)
COPY run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 80 443
CMD ["/run.sh"]
