FROM php:fpm
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
		wget \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
	&& docker-php-ext-install opcache \
	&& docker-php-ext-install pdo_mysql \
	&& docker-php-ext-install mysqli \
	&& usermod -u 1000 www-data && groupmod -g 1000 www-data
  
RUN wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - && \
    echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list &&\
	apt-get update && \
    apt-get -yq install newrelic-php5 && \
	apt-get clean
    
ENV NR_INSTALL_SILENT 1
ENV NR_INSTALL_KEY "1234567890abcdefghij1234567890abcdefghij"
ENV NR_APP_NAME "Default App Name"
	
COPY config/custom.ini config/zcustom.ini /usr/local/etc/php/conf.d/
COPY php-fpm/zcustom.conf /usr/local/etc/php-fpm.d/

#RUN bash newrelic-install install

