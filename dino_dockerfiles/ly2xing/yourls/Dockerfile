FROM php:7.0.2-apache
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install mysqli
RUN a2enmod rewrite
COPY . /var/www/html/
COPY user/config-sample.php /var/www/html/user/config.php
RUN sed -i "s/your db user name/root/" /var/www/html/user/config.php
RUN sed -i "s/'your db password'/getenv('DB_PASSWORD')/" /var/www/html/user/config.php
RUN sed -i "s|'http://your-own-domain-here.com'|getenv('HOST')|" /var/www/html/user/config.php
RUN sed -i "s/'username'/getenv('USERNAME')/" /var/www/html/user/config.php
RUN sed -i "s/'password'/getenv('PASSWORD')/" /var/www/html/user/config.php
RUN sed -i "s/'localhost'/getenv('DB_HOST')/" /var/www/html/user/config.php
EXPOSE 80
