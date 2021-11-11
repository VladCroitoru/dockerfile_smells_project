FROM php:7-apache

MAINTAINER Yu-Hsin Lu <kerol2r20@gmail.com>

RUN sed -i 's/deb.debian.org/ftp.tw.debian.org/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y git libcurl4-openssl-dev libxml2-dev zlib1g-dev libpng-dev libmcrypt-dev libbz2-dev && \
    docker-php-source extract && \
    CFLAGS="-I/usr/src/php" docker-php-ext-configure xmlreader && \
    docker-php-ext-install pdo pdo_mysql mysqli curl json xml xmlwriter xmlreader tokenizer mbstring session zip gd mcrypt bz2 && \
    cd /etc/apache2/mods-enabled && \
    ln -s ../mods-available/ssl.conf && \
    ln -s ../mods-available/ssl.load && \
    ln -s ../mods-available/socache_shmcb.load && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');" && \
    composer global require "laravel/installer" && \
    echo PATH=$HOME/.composer/vendor/bin:$PATH >> ~/.bashrc

WORKDIR /var/www/html

ENTRYPOINT ["docker-php-entrypoint"]

EXPOSE 80

CMD ["apache2-foreground"]
