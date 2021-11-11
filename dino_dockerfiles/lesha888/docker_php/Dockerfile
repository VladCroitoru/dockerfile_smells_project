FROM php:7.0.5-fpm


RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libcurl4-gnutls-dev \
        git \
    && docker-php-ext-install iconv mcrypt mysqli curl iconv json mbstring opcache sockets zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && cd /usr/src/php/ext/ \
    && git clone https://github.com/phpredis/phpredis.git \
    && cd phpredis \
    && git checkout php7 \
	&& docker-php-ext-install phpredis  \
	&& cd /usr/src/php/ext/ \
	&& git clone https://github.com/igbinary/igbinary.git \
	&& cd igbinary \
	&& git checkout php7-dev-playground1 \
	&& docker-php-ext-install igbinary \
	&& rm -r /var/lib/apt/lists/*

#RUN cd /usr/src/php/ext/ &&  git clone git://github.com/xdebug/xdebug.git && docker-php-ext-install xdebug
#RUN  apt-get install gcc make autoconf libc-dev pkg-config zlib1g-dev libmemcached-dev && git clone https://github.com/php-memcached-dev/php-memcached && cd php-memcached && git checkout php7 && cd .. && docker-php-ext-install php-memcached 	

# RUN wget https://pecl.php.net/get/mysqlnd_memcache-1.0.1.tgz
# && tar -zxvf mysqlnd_memcache-1.0.1.tgz
# && mv mysqlnd_memcache-1.0.1 mysqlnd_memcache
# && cd mysqlnd_memcache
# docker-php-ext-install mysqlnd_memcache
