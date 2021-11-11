FROM php:8.0.9-fpm

WORKDIR /root
 RUN apt-get update            
 RUN apt-get install -y curl
 RUN apt-get install git -y

 RUN echo 'memory_limit = 2048M' >> /usr/local/etc/php/conf.d/docker-php-memlimit.ini
 
 RUN curl -sS https://getcomposer.org/installer | php

 RUN mv composer.phar /usr/bin/composer
 
 RUN apt-get install -y zlib1g-dev && apt-get install -y libzip-dev
 RUN docker-php-ext-install zip
 
 RUN export COMPOSER_ALLOW_SUPERUSER=1
 RUN echo "export COMPOSER_ALLOW_SUPERUSER=1" >> ~/.bashrc

 RUN composer global require laravel/installer
 RUN composer global require laravel/laravel

 RUN ["/bin/bash", "-c", "echo PATH=$PATH:~/.composer/vendor/bin/ >> ~/.bashrc"]
 RUN ["/bin/bash", "-c", "source ~/.bashrc"]

 RUN composer create-project laravel/laravel /workspace/example-test-app
 
 RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
 RUN docker-php-ext-install mysqli pdo pdo_mysql
 RUN pecl install redis && docker-php-ext-enable redis
 
 COPY /source/laravel /workspace/example-test-app

 WORKDIR /workspace/example-test-app
 
 RUN chmod -R 775 /workspace/example-test-app/storage
 RUN chmod -R 775 /workspace/example-test-app/bootstrap/cache
 
EXPOSE 9000
 CMD ["php-fpm"]