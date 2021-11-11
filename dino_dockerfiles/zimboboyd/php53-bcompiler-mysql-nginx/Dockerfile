# Pull base image.
FROM ubuntu:12.04
MAINTAINER Zimbo Boyd
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y curl python-software-properties apt-transport-https


RUN apt-get install python-software-properties
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
RUN add-apt-repository 'deb http://mirrors.n-ix.net/mariadb/repo/10.0/ubuntu precise main'
RUN apt-get update -y

RUN apt-get install -y --fix-missing mariadb-server
RUN apt-get install -y --fix-missing wget vim-tiny nginx php5 php-apc php-pear php5-cli php5-common php5-curl php5-dev php5-fpm php5-gd php5-imagick php5-imap php5-intl php5-json php5-mcrypt php5-memcache php5-ming php5-mysql php5-ps php5-pspell php5-recode php5-snmp php5-sqlite php5-tidy php5-xmlrpc php5-xsl libmysqlclient18
RUN apt-get install -y --fix-missing make libpcre3-dev cron


RUN pecl channel-update pecl.php.net
RUN pecl install apc bcompiler lzf mailparse pdflib rar


RUN mkdir -p /var/www

# index.html
ADD index.html /var/www/home.html

# Nginx
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini
ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx-site.conf /etc/nginx/sites-available/default

ADD bcompiler.ini /etc/php5/fpm/conf.d/bcompiler.ini


#ADD ssl/server.crt /etc/nginx/server.crt
#ADD ssl/server.key /etc/nginx/server.key

#phpmyadmin
#ADD phpMyAdmin/ /var/www/phpMyAdmin
#ADD phpmyadmin.config.inc.php /var/www/phpMyAdmin/config.inc.php


RUN chown -R www-data:www-data /var/www

RUN apt-get -y -q autoclean && apt-get -y -q autoremove

# Expose ports.

# Nginx
EXPOSE 80
EXPOSE 443

# MariaDB
EXPOSE 3306

ADD start.sh /start.sh
RUN chmod +x /start.sh
CMD /start.sh
