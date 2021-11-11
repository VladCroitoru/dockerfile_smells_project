FROM php:7.1-apache

ENV AP_SERVERNAME localhost
ENV AP_SERVERALIAS docker.local
ENV AP_SERVERADMIN c@docker.local
ENV AP_ROOT /var/www



# Set the locale
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  


# Install selected extensions and other stuff
RUN apt-get update \
    && apt-get -y --no-install-recommends install git \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# php config
COPY php.ini /usr/local/etc/php/
COPY php.ini /etc/php5/apache2/conf.d/

# PDO & mysqli
RUN docker-php-ext-install pdo pdo_mysql mysqli

#Install Composer globally
RUN curl -s -o /usr/local/bin/composer https://getcomposer.org/composer.phar && \
    chmod 0755 /usr/local/bin/composer

#xdebug
RUN pecl install xdebug
RUN docker-php-ext-enable xdebug opcache

# Install mcrypt extension
RUN apt-get update && apt-get install -y \
    libmcrypt-dev \
    libssl-dev && \
    docker-php-ext-install mcrypt \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install gd
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg-dev \
    libjpeg62-turbo-dev \
    libpng12-dev && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install gd \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install zip extension & mb string exention
RUN docker-php-ext-install zip
RUN docker-php-ext-install mbstring

ADD 001-docker.conf /etc/apache2/sites-available/
RUN ln -s /etc/apache2/sites-available/001-docker.conf /etc/apache2/sites-enabled/

RUN a2enmod rewrite

# Clean image
RUN apt-get -yqq clean && \
    apt-get -yqq purge && \
    rm -rf /tmp/* /var/tmp/* && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80

WORKDIR /var/www