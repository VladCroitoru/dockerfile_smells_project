FROM ubuntu:14.04
MAINTAINER Morgan Blackthorne <morgan@windsofstorm.net>

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Apply updates
RUN apt-get update
RUN apt-get -y upgrade

# Basic Requirements
RUN apt-get -y install mysql-client apache2 libapache2-mod-php5 pwgen python-setuptools vim-tiny pwgen python-setuptools curl git unzip php5-curl php5-gd php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode php5-sqlite php5-tidy php5-xmlrpc php5-xsl php5-ldap php5-mysql php-apc

# php config
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php5/apache2/php.ini
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php5/apache2/php.ini
RUN sed -i -e "s/short_open_tag\s*=\s*Off/short_open_tag = On/g" /etc/php5/apache2/php.ini

# Apache site conf
ADD ./scripts/foreground.sh /etc/apache2/foreground.sh
RUN chmod 755 /etc/apache2/foreground.sh
ADD ./configs/000-default.conf /etc/apache2/sites-available/000-default.conf

# Supervisor Config
RUN /usr/bin/easy_install supervisor
RUN /usr/bin/easy_install supervisor-stdout
ADD ./configs/supervisord.conf /etc/supervisord.conf

# Startup Script
ADD ./scripts/start.sh /start.sh
RUN chmod 755 /start.sh

# private expose
EXPOSE 80

# volume for Apache
VOLUME ["/var/www/html"]

CMD ["/bin/bash", "/start.sh"]
