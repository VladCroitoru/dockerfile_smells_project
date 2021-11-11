FROM ubuntu:xenial
MAINTAINER Pascal Martineau <pascal.animateur@gmail.com>

# Add official PHP ppa
COPY ondrej-php-xenial.list /etc/apt/sources.list.d/ondrej-php-xenial.list

# Install package dependencies
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \
    apt-get update && apt-get install -y \
        apache2 \
        build-essential \
        ca-certificates \
        curl \
        nano \
        php5.6 \
        php5.6-cli \
        php5.6-curl \
        php5.6-dev \
        php5.6-gd \
        php5.6-mbstring \
        php5.6-mcrypt \
        php5.6-mysql \
        php5.6-xml \
        php-pear \
        php-xdebug \
    --no-install-recommends && rm -r /var/lib/apt/lists/*

# Configure XDebug
COPY xdebug.ini /etc/php/5.6/mods-available/xdebug.ini
RUN mkdir /tmp/xdebug

# Enable Apache2 and PHP modules
RUN a2enmod actions rewrite headers && \
    pecl install uploadprogress && \
    echo "extension=uploadprogress.so" > /etc/php/5.6/mods-available/uploadprogress.ini && \
    phpenmod curl mcrypt uploadprogress xdebug

# Install WP-CLI
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

RUN rm /var/www/html/index.html

VOLUME /var/www/html
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
