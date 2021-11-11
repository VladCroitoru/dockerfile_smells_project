FROM php:7.1-fpm

LABEL com.example.vendor="pinoniq" \
      version="1.3"

MAINTAINER Jeroen "pinoniq" Meeus

# Copy our ini file
COPY ./conf/local.ini /usr/local/etc/php/conf.d/local.ini

# Set timezone
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Brussels /etc/localtime && "date"

# install some basic tools
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        unzip \
        mysql-client \
        unzip \
        git \
        libgmp-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install pdo pdo_mysql \
    && docker-php-ext-install gmp


# Install xdebug
RUN pecl install xdebug \
&& docker-php-ext-enable xdebug \
&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
&& echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

# Now we have that we need, we continue installing some usefull cli tools
## composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer

## Drush
RUN php -r "readfile('https://s3.amazonaws.com/files.drush.org/drush.phar');" > drush \
    && chmod +x drush \
    && mv drush /usr/local/bin

## Symfony installer
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony \
    && chmod a+x /usr/local/bin/symfony

# add some useful symfony shortcuts
RUN echo 'alias dev="php bin/console --env=dev"' >> ~/.bashrc \
&& echo 'alias prod="php bin/console --env=prod"' >> ~/.bashrc

# add node and npm
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

# add some additional exposed ports to listen to, like xdebug, webpack-dev-server, ...
EXPOSE 8080
EXPOSE 9000
EXPOSE 9001

WORKDIR /var/www
