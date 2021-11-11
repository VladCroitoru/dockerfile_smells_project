FROM php:5.6-apache

RUN a2enmod rewrite

# install the PHP extensions we need
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev ghostscript git \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd mysql calendar zip

RUN apt-get update \
    && apt-get install -y libmagickwand-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pecl install imagick-beta \
    && echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \
    && apt-get remove -y libmagickwand-dev \
    && apt-get install -y libmagickwand-6.q16-2 \
    && apt-get autoremove -y

RUN    echo "display_errors = off"                                >> /usr/local/etc/php/conf.d/php.ini \
    && echo "log_errors = on"                                     >> /usr/local/etc/php/conf.d/php.ini \
    && echo "post_max_size = 64M"                                 >> /usr/local/etc/php/conf.d/php.ini \
    && echo "upload_max_filesize = 16M"                           >> /usr/local/etc/php/conf.d/php.ini \
    && echo "memory_limit = 256M"                                 >> /usr/local/etc/php/conf.d/php.ini \
    && echo "include_path = '.:/usr/local/lib/php:/var/www/html'" >> /usr/local/etc/php/conf.d/php.ini
    
    

VOLUME /var/www/html

