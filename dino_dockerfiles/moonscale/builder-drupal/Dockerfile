FROM php:5.6-fpm

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        git \
        unzip \
    && docker-php-ext-install zip

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

RUN cd /usr/local && git clone http://github.com/drush-ops/drush && cd drush && composer install

RUN ln -s /usr/local/drush/drush /usr/local/bin/drush

RUN echo "date.timezone = UTC" > /usr/local/etc/php/conf.d/date.ini

RUN echo "user0:x:1000:1000:User 0:/tmp:/bin/false" >> /etc/passwd && \
    echo "user1:x:1001:1001:User 1:/tmp:/bin/false" >> /etc/passwd && \
    echo "user2:x:1002:1002:User 2:/tmp:/bin/false" >> /etc/passwd && \
    echo "user3:x:1003:1003:User 3:/tmp:/bin/false" >> /etc/passwd && \
    echo "user4:x:1004:1004:User 4:/tmp:/bin/false" >> /etc/passwd
