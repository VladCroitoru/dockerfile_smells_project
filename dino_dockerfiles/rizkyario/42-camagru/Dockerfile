FROM php:7.2-apache

RUN a2enmod rewrite

RUN yes | pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini

# Installs sendmail
RUN apt-get update && apt-get install -q -y ssmtp mailutils libpng-dev && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install gd pdo_mysql

# root is the person who gets all mail for userids < 1000
RUN echo "root=camagru.rizky@gmail.com" >> /etc/ssmtp/ssmtp.conf

# Here is the gmail configuration (or change it to your private smtp server)
RUN echo "mailhub=smtp.gmail.com:587" >> /etc/ssmtp/ssmtp.conf
RUN echo "AuthUser=camagru.rizky@gmail.com" >> /etc/ssmtp/ssmtp.conf
RUN echo "AuthPass=Paris2018" >> /etc/ssmtp/ssmtp.conf

RUN echo "UseTLS=YES" >> /etc/ssmtp/ssmtp.conf
RUN echo "UseSTARTTLS=YES" >> /etc/ssmtp/ssmtp.conf
RUN echo "FromLineOverride=YES" >> /etc/ssmtp/ssmtp.conf

# Set up php sendmail config
RUN echo "sendmail_path=sendmail -i -t" >> /usr/local/etc/php/conf.d/php-sendmail.ini

# docker build -t rizkyario/42-camagru .
# docker push rizkyario/42-camagru