FROM php:7.1-fpm

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install zip \
    && pecl install xdebug-2.5.0 \
    && docker-php-ext-enable xdebug

WORKDIR /var/www

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');"

# taken from Wordpress offical fpm Dockerfile
# https://github.com/docker-library/wordpress/blob/7d40c4237f01892bb6dbc67d1a82f5b15f807ca1/php7.0/fpm/Dockerfile
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=2'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN { \
    echo 'xdebug.remote_enable = 1'; \
    echo 'xdebug.remote_port = 9000'; \
    echo 'xdebug.scream = 0'; \
    echo 'xdebug.show_local_vars = 1'; \
    echo 'xdebug.idekey = PHPSTORM'; \
} > /usr/local/etc/php/conf.d/xdebug.ini

# taken from mkz71's comment on Wordpress official Docker Hub page
# https://hub.docker.com/_/wordpress/
RUN { \
		echo 'file_uploads = On'; \
		echo 'memory_limit = 256M'; \
		echo 'upload_max_filesize = 256M'; \
		echo 'post_max_size = 300M'; \
		echo 'max_execution_time = 600'; \
	} > /usr/local/etc/php/conf.d/uploads.ini
