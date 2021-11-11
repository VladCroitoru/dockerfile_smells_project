##
# Jb Nahan PHP 5.6 + Apache 2 container
##

FROM        	macintoshplus/php:php56
MAINTAINER 	Jean-Baptiste Nahan <jean-baptiste@nahan.fr>

# Supervisor
RUN 		apt-get install -y supervisor
RUN 		mkdir -p /var/log/supervisor
COPY 		conf/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Apache
RUN		apt-get -y install apache2 libapache2-mod-php5
RUN		a2enmod rewrite
RUN		a2enmod headers
ENV 		APACHE_RUN_USER www-data
ENV 		APACHE_RUN_GROUP www-data
ENV 		APACHE_LOG_DIR /var/log/apache2
RUN		rm /etc/apache2/sites-enabled/000-default.conf
RUN		usermod -u 10000 www-data

# PHP
RUN 		cp /usr/share/php5/php.ini-development /etc/php5/apache2/php.ini
RUN 		sed -i 's/\;date\.timezone\ \=/date\.timezone\ \=\ Europe\/Paris/g' /etc/php5/apache2/php.ini

#RUN 		sed -i 's/\;include_path = ".:\/usr\/share\/php"/include_path = ".:\/var\/www\/library"/g' /etc/php5/apache2/php.ini
RUN		sed -i 's/post_max_size = 8M/post_max_size = 50M/g' /etc/php5/apache2/php.ini
RUN   sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 50M/g' /etc/php5/apache2/php.ini
RUN   sed -i 's/\;\ max_input_vars\ \=\ 1000/max_input_vars\ \=\ 250000/g' /etc/php5/apache2/php.ini
RUN   sed -i 's/memory_limit\ \=\ 128M/memory_limit\ \=\ 512M/g' /etc/php5/apache2/php.ini
RUN   sed -i 's/max_execution_time\ \=\ 30/max_execution_time\ \=\ 120/g' /etc/php5/apache2/php.ini
RUN     sed -i 's/\output_buffering\ \=\ 4096/output_buffering\ \=\ Off/g' /etc/php5/apache2/php.ini
RUN     sed -i 's/\session.cookie_httponly\ \=/session.cookie_httponly\ \=\ On/g' /etc/php5/apache2/php.ini

RUN   php5enmod amqp xdebug

# PaaS bootstrap
COPY		bin/container-bootstrap.sh /usr/bin/container-bootstrap.sh
RUN 		chmod +x /usr/bin/container-bootstrap.sh

EXPOSE      	80

VOLUME 		/sources
VOLUME		/etc/apache2/sites-available
VOLUME		/var/log/apache2

WORKDIR		/sources

CMD 		["/usr/bin/container-bootstrap.sh"]
