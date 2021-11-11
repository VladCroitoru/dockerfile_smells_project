# set the base image first
FROM olegpuzanov/docker-nginx-php5-fpm

# specify maintainer
MAINTAINER Oleg Puzanov <oleg.puzanov@gmail.com>

# install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# fix security issue in php.ini, more info https://nealpoole.com/blog/2011/04/setting-up-php-fastcgi-and-nginx-dont-trust-the-tutorials-check-your-configuration/
RUN sed -i.bak "s@;cgi.fix_pathinfo=1@cgi.fix_pathinfo=0@g" /etc/php5/fpm/php.ini

# set timezone in php.ini
RUN sed -i".bak" "s/^\;date\.timezone.*$/date\.timezone = \"Europe\/Kiev\" /g" /etc/php5/fpm/php.ini