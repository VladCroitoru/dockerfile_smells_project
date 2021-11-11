################################################
# Dockerfile to build Seltzers web frontend    #
################################################

# Set the base image
FROM    phusion/baseimage:0.9.17

# File Author / Maintainer
MAINTAINER Miguel Luís <mkxpto@gmail.com>

CMD ["/sbin/my_init"]

# Some Environment Variables
ENV DEBIAN_FRONTEND noninteractive

# Installation
RUN apt-get update && \
	echo "mysql-server mysql-server/root_password password" | debconf-set-selections && \
	echo "mysql-server mysql-server/root_password_again password" | debconf-set-selections && \
	apt-get -y install mysql-server php5-fpm php5-mysql nginx wget unzip

# COPY seltzer-master/crm  /usr/share/nginx/html/crm

RUN wget https://github.com/elplatt/seltzer/archive/master.zip && \
	unzip master.zip && \
	rm -rf master.zip && \
	mv seltzer-master/crm /usr/share/nginx/html/

# Configuration
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf && \
    sed -e 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/' -i /etc/php5/fpm/php.ini && \
    sed -e 's/listen = 127.0.0.1:9000/listen = \/var\/run\/php5-fpm.sock/' -i /etc/php5/fpm/pool.d/www.conf && \
	echo "php_flag[magic_quotes_gpc] = Off\nphp_flag[magic_quotes_runtime] = Off\nphp_flag[magic_quotes_sybase] = Off" >> /etc/php5/fpm/pool.d/www.conf && \
	chown www-data:www-data -R /usr/share/nginx/html/ && \
	mv /usr/share/nginx/html/crm/config.sample.inc.php /usr/share/nginx/html/crm/config.inc.php && \
	sed -e "s/\$config_db_user = .*/\$config_db_user = \'root\';/" -i /usr/share/nginx/html/crm/config.inc.php && \
	sed -e "s/\$config_db_db = .*/\$config_db_db = \'hackaveiro\';/" -i /usr/share/nginx/html/crm/config.inc.php



ADD build/nginx/default.conf   	/etc/nginx/sites-available/default
ADD build/mysqld/my.cnf    		/etc/mysql/my.cnf

RUN mkdir           		/etc/service/nginx
ADD build/nginx/nginx.sh  	/etc/service/nginx/run
RUN chmod +x        		/etc/service/nginx/run

RUN mkdir           		/etc/service/phpfpm
ADD build/nginx/phpfpm.sh 	/etc/service/phpfpm/run
RUN chmod +x        		/etc/service/phpfpm/run

RUN mkdir           		/etc/service/mysql
ADD build/mysqld/mysqld.sh  /etc/service/mysql/run
RUN chmod +x        		/etc/service/mysql/run

RUN mkdir -p        /var/lib/mysql/
RUN chmod -R 755    /var/lib/mysql/

ADD build/99_init.sh /etc/my_init.d/99_init.sh
RUN chmod +x /etc/my_init.d/99_init.sh


EXPOSE 80

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
