FROM phpstorm/php-71-apache-xdebug-25

RUN apt-get update && apt-get install -y libzip-dev zip \
    && docker-php-ext-install zip pdo_mysql pdo exif

RUN apt-get -y update \
&& apt-get install -y libicu-dev \
&& docker-php-ext-configure intl \
&& docker-php-ext-install intl

RUN cd ~ && curl -sS https://getcomposer.org/installer -o composer-setup.php \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer

RUN a2enmod rewrite
RUN service apache2 restart

RUN chown www-data:www-data /var/www/html/
RUN groupadd dev -g 1000
RUN useradd dev -g dev -d /home/dev -m
RUN echo '%dev ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER dev:dev