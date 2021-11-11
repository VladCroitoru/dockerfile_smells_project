FROM php:5.6-apache
ENV TERM xterm
RUN apt-get update && apt-get install -y \
    wget \
    git \
    unzip \
    nano
# && rm -rf /var/lib/apt/lists/*
# RUN docker-php-ext-install mysqli
ADD composer-install.sh /var/composer-install.sh
RUN chmod +x /var/composer-install.sh
Run /var/composer-install.sh
RUN mv composer.phar /usr/local/bin/composer
RUN composer require lcobucci/jwt "3.2"
RUN composer require hybridauth/hybridauth "3.0.0-rc.7"
#RUN a2enmod rewrite
ADD public/* /var/www/html/
