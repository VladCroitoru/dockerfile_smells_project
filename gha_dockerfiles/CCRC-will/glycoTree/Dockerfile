FROM php:7.4-apache
RUN docker-php-ext-install mysqli
RUN echo 'SetEnv MYSQL_PASSWORD ${MYSQL_PASSWORD}' >> /etc/apache2/conf-enabled/environment.conf
RUN echo 'SetEnv MYSQL_SERVER_NAME mysql' >> /etc/apache2/conf-enabled/environment.conf
RUN echo 'memory_limit = 256M' >> /usr/local/etc/php/conf.d/docker-php-memlimit.ini
