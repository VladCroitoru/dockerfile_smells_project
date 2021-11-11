FROM ubuntu:14.04
MAINTAINER Zane Miller <houwebasst@uoregon.edu>

# Keep upstart from complaining
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Basic Requirements
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install\
		apache2\
		libapache2-mod-php5\
		php5-mysql php-apc\
		python-setuptools\
		curl\
		git\
		unzip\
		nano\
		mysql-server

# Laravel Requirements
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install\
		php5-curl\
		php5-gd\
		php5-intl\
		php-pear\
		php5-imagick\
		php5-imap\
		php5-mcrypt\
		php5-memcache\
		php5-ming\
		php5-ps\
		php5-pspell\
		php5-recode\
		php5-sqlite\
		php5-tidy\
		php5-xmlrpc\
		php5-xsl

# apache config
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html
# copy the config file
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf
#Set the ENV vars
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
#Turn mod_rewrite on
RUN /usr/sbin/a2enmod rewrite
#Set the file perms correctly on the web root
RUN chown -R www-data:www-data /var/www/

# php config
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php5/apache2/php.ini
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php5/apache2/php.ini
RUN sed -i -e "s/short_open_tag\s*=\s*Off/short_open_tag = On/g" /etc/php5/apache2/php.ini

# fix for php5-mcrypt
RUN /usr/sbin/php5enmod mcrypt

#MySQL setup
COPY laravel_init.sh /laravel_init.sh
RUN chmod 777 /laravel_init.sh

WORKDIR /var/www/html

EXPOSE 80
EXPOSE 3306

#Add the directory to the web root
ONBUILD ADD . /var/www/html

#Make sure apache can access it
ONBUILD RUN chown -R www-data:www-data /var/www

#ONBUILD CMD chmod 777 /laravel_init.sh

#Bootstrap the DB and site
ENTRYPOINT ["/laravel_init.sh"]