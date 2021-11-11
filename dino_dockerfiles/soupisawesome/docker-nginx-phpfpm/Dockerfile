FROM ubuntu:14.04

MAINTAINER Philip Bower <pabower@gmail.com>

# Surpress Upstart errors/warning
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# No tty
ENV DEBIAN_FRONTEND noninteractive

# Updates
RUN apt-get update
RUN apt-get install -y nginx php5-fpm php5-cli php5-mcrypt git

# Make updates to php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini && \
	sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini && \
	sed -i "s/display_errors = Off/display_errors = stderr/" /etc/php5/fpm/php.ini && \
	sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 30M/" /etc/php5/fpm/php.ini && \
	sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf

# Enable mcrypt / restart fpm
RUN php5enmod mcrypt
RUN service php5-fpm restart

ADD ./default /etc/nginx/sites-available/default

# Make laravel structure
RUN mkdir -p /data/www/laravel
VOLUME ["/data"]

# Restart nginx
RUN service nginx restart

EXPOSE 80
EXPOSE 443
EXPOSE 9000

ENTRYPOINT ["/usr/sbin/php5-fpm", "-F"]

####################
# Swap file replace 1G with 2xRAM
#fallocate -l 1G /swapfile
#mkswap /swapfile
#swapon /swapfile

#cd ~
#curl -sS https://getcomposer.org/installer | php
#mv composer.phar /usr/local/bin/composer
#composer create-project laravel/laravel /data/www/laravel --prefer-dist
#chown -R :www-data /data/www/laravel
#chmod -R 775 /data/www/laravel/storage
####################