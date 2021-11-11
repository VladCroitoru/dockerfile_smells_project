FROM php:5.6-apache

RUN a2enmod rewrite

RUN set -xe \
    && apt-get update \
    && apt-get install -y libpng12-dev libjpeg-dev libmcrypt-dev libfreetype6-dev ssmtp\
    && echo "FromLineOverride=YES" >> /etc/ssmtp/ssmtp.conf\
    && echo 'sendmail_path = "/usr/sbin/ssmtp -t"' > /usr/local/etc/php/conf.d/mail.ini\
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir=/usr/include/ \
    && docker-php-ext-install gd mcrypt mbstring mysqli mysql pdo pdo_mysql zip
