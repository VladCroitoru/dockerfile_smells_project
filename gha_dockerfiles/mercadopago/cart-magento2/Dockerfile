FROM php:7.3-apache

# Download script to install PHP extensions and dependencies
ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/
RUN chmod uga+x /usr/local/bin/install-php-extensions && sync

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y nano unzip git
RUN install-php-extensions intl gd soap bcmath pdo_mysql xsl zip

# Install and configure xdebug
RUN yes | pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.mode=coverage" >> /usr/local/etc/php/php.ini

# Install composer and downgrade to version 1
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php \
    && HASH=`curl -sS https://composer.github.io/installer.sig` \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && rm -rf composer-setup.php \
    && composer self-update --1

# Install phpmd
RUN git clone git://github.com/phpmd/phpmd.git \
    && cd phpmd \
    && git submodule update --init \
    && composer install

# Install Magento 2
COPY bin/install-mg2.sh bin/install-mg2.sh
RUN sh bin/install-mg2.sh

# Install plugin
COPY src magento2/app/code

# phpunit config file
COPY phpunit.xml phpunit.xml

# Fix permissions
RUN chmod 777 -Rf magento2
