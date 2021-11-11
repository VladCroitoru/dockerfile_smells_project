FROM php:apache
ENV COMPOSER_ALLOW_SUPERUSER 1 # Setup the Composer installer 
RUN a2enmod headers rewrite && \
    apt-get update && \
    apt-get install -y git curl unzip libpng12-dev libpq-dev libjpeg62-turbo-dev libfreetype6-dev && \
    docker-php-ext-configure gd  --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install gd mbstring pdo_pgsql pdo_mysql

RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \
    && curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \
    && php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }" && \
    php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer

RUN git clone https://github.com/SSilence/selfoss.git /var/www/html/ && \
cd /var/www/html && \
composer install && \
ln -s /var/www/html/data/config.ini /var/www/html/config.ini && \
chown -R www-data .
