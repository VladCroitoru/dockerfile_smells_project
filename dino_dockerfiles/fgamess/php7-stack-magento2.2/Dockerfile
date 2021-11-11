FROM php:7.0-fpm

# Install dependencies
RUN apt-get update \
    && apt-get install -y \
    git \
    cron \
    vim \
    zlib1g-dev \
    libmcrypt-dev \
    openssh-server \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libxslt-dev \
    libxml2-dev \
    libicu-dev \
    --no-install-recommends \
    && mkdir -p /var/run/sshd \
    && rm -rf /var/lib/apt/lists/*

# Install required PHP extensions
RUN docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ --with-freetype-dir=/usr/lib64/
RUN docker-php-ext-install bcmath \
    mbstring \
    opcache \
    pcntl \
    zip \
    mcrypt \
    pdo \
    pdo_mysql \
    mysqli \
    xsl \
    soap \
    intl \
    gd

#RUN docker-php-ext-install exif

#Add composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer --version

# Set timezone
RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime
RUN "date"

# install xdebug
RUN pecl install xdebug
RUN docker-php-ext-enable xdebug
RUN echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN echo "xdebug.cli_color=1\nxdebug.remote_autostart=1\nxdebug.remote_connect_back=1" > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini


COPY php.ini /tmp/php.ini_extension
RUN cat /tmp/php.ini_extension >> /usr/local/etc/php/php.ini \
    && rm /tmp/php.ini_extension

# COPY php7-fpm.conf /usr/local/etc/php-fpm.conf

RUN usermod -u 1000 www-data
RUN useradd -ms /bin/bash magento_user 
RUN usermod -a -G www-data magento_user

#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

WORKDIR /var/www/

# Make ssh dir
RUN mkdir /root/.ssh/
