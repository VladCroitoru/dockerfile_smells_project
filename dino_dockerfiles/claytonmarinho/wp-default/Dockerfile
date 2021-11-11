FROM php:5.6-apache
RUN apt-get update 
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev openssh-server libmcrypt-dev
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd mbstring mysqli pdo pdo_mysql mysql mcrypt pcntl sockets 
RUN a2enmod rewrite && service apache2 restart
ADD sshd_config /etc/ssh/
RUN groupadd ftpaccess && service ssh restart
ENTRYPOINT ["apache2-foreground"]


