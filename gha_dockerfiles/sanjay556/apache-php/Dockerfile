FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

# install tools
RUN apt update && apt install -y nano apache2 libapache2-mod-fcgid
RUN a2enmod proxy && a2enmod proxy_fcgi && a2enmod ssl && a2enmod http2

# Install PHP-fpm Configure Apache to use our PHP-FPM socket for all PHP files
RUN apt install -y php7.4-fpm && a2enconf php7.4-fpm
RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer
EXPOSE 80

# Start servers
# Start PHP-FPM worker service and run Apache in foreground
CMD service php7.4-fpm start && /usr/sbin/apache2ctl -D FOREGROUND

#set working directory to where Apache serves files
WORKDIR /var/www/html

# php file to check php is running
RUN rm index.html && echo "<?php phpinfo() ?>" >> index.php
