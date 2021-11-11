FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get -y install apache2 php5 php5-cli php5-mysql curl vim supervisor

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN cd /var/www/html 
RUN composer require slim/slim "^3.0"

RUN rm -rf /var/www/html/index.html

RUN a2enmod rewrite

ADD template/.htaccess /var/www/html/.htaccess
ADD template/apache.conf /etc/apache2/sites-available/000-default.conf

ADD supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80
CMD ["/usr/bin/supervisord"]
