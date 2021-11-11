FROM nimmis/apache-php7

RUN apt-get -y update && apt-get -y install \
    php-mysql \
    php-mbstring \
    php-xml \
    php-zip


RUN sed -i 's_DocumentRoot /var/www/html_DocumentRoot /var/www/html/web/_' /etc/apache2/sites-enabled/000-default.conf

RUN sed -i 's_AllowOverride None_AllowOverride All_' /etc/apache2/apache2.conf

COPY . /var/www/html
WORKDIR /var/www/html

RUN useradd --no-log-init -r -g www-data apache

RUN chmod -R 775 /var/www/ && chown -R apache:www-data  /var/www/

RUN a2enmod rewrite

RUN service apache2 restart

EXPOSE 80
