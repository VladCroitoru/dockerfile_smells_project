FROM wordpress:php7.1

MAINTAINER Christian Chung <christian.m.chung@gmail.com>

# Install the packages I usually need
RUN apt-get update && apt-get install -y \
		less \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng12-dev \
		libmemcached-dev \
		git \
    vim \
	&& docker-php-ext-install -j$(nproc) iconv mcrypt \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd \
	&& docker-php-ext-install mysqli \
	&& docker-php-ext-install pdo_mysql \
	&& docker-php-ext-install zip \
	&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install Memcached
RUN git clone https://github.com/php-memcached-dev/php-memcached /usr/src/php/ext/memcached \
	&& cd /usr/src/php/ext/memcached && git checkout -b php7 origin/php7 \
	&& docker-php-ext-configure memcached \
	&& docker-php-ext-install memcached

# Enable error reporting.
# https://github.com/docker-library/php/issues/153
RUN { \
      echo 'error_reporting=E_ALL'; \
      echo 'log_errors=On'; \
    } > /usr/local/etc/php/conf.d/errors.ini

# Install wp-cli
RUN curl -O "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar" \
    && chmod +x wp-cli.phar \
    && mv wp-cli.phar /usr/local/bin/wp-cli

# Setup a config file
RUN mkdir -p /etc/wp-cli
RUN { \
      echo 'path: /var/www/html'; \
    } > /etc/wp-cli/config.yml

# Setup an alias for running wp-cli commands that will run commands as the appropriate user
RUN { \
      echo '#!/usr/bin/env sh'; \
      echo 'runuser -l www-data -s /bin/sh -c "WP_CLI_CONFIG_PATH=/etc/wp-cli/config.yml /usr/local/bin/wp-cli $*"'; \
    } > /usr/local/bin/wp \
    && chmod +x /usr/local/bin/wp

# Donwload and install composer
RUN curl -sSL "https://getcomposer.org/installer" | php \
    && mv composer.phar /usr/local/bin/composer

RUN pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && rm -rf /tmp/pear/

RUN { \
      echo ''; \
      echo 'xdebug.remote_enable=1'; \
      echo 'xdebug.remote_port="9000"'; \
    } >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

RUN curl -sSL -o /usr/local/bin/phpunit "https://phar.phpunit.de/phpunit.phar" \
    && chmod +x /usr/local/bin/phpunit

RUN { \
      echo '#!/usr/bin/env sh'; \
      echo 'runuser -l www-data -s /bin/sh -c "cd $PHPUNIT_TEST_DIR; /usr/local/bin/phpunit $*"'; \
    } > /usr/local/bin/tests \
    && chmod +x /usr/local/bin/tests

# This is WordPress gets installed at first, courtesy of parent image
WORKDIR /usr/src/wordpress

# Add configs for memcached and batcache 
ADD bin/wp-config.sh /usr/local/bin/wp-config.sh

# Make it executable
RUN chmod +x /usr/local/bin/wp-config.sh

# Inject our stuff into wp-config
RUN /usr/local/bin/wp-config.sh

# Put our application code onto the server
ADD wp-content /usr/src/wordpress/wp-content

# Reset working directory so upstream entrypoints work
WORKDIR /var/www/html