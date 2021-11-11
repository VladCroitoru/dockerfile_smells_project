# Dockerfile for moodle instance. more dockerish version of https://github.com/sergiogomez/docker-moodle
FROM ubuntu:16.04
MAINTAINER Aldo Necci <necci@ing.uniroma3.it>

VOLUME ["/var/moodledata"]
EXPOSE 80 443
COPY moodle-config.php /var/www/html/config.php

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Database info
#ENV MYSQL_HOST 127.0.0.1
#ENV MYSQL_USER moodle
#ENV MYSQL_PASSWORD moodle
#ENV MYSQL_DB moodle
ENV MOODLE_URL http://172.16.239.146

# ADD http://downloads.sourceforge.net/project/moodle/Moodle/stable27/moodle-latest-27.tgz /tmp/moodle-latest-27.tgz
ADD ./foreground.sh /etc/apache2/foreground.sh

RUN apt-get update && apt-get -y upgrade && \
	apt-get -y install mysql-client pwgen python-setuptools curl git unzip apache2 php7.0 ghostscript imagemagick \
		php7.0-gd libapache2-mod-php7.0 postfix wget supervisor php7.0-pgsql libcurl3 \
		libcurl3-dev php7.0-curl php7.0-xmlrpc php7.0-xml php7.0-intl php7.0-mysql git-core \
		graphviz aspell php7.0-pspell php7.0-ldap php7.0-zip php7.0-soap php7.0-mbstring && \
	cd /tmp && \
	git clone -b MOODLE_31_STABLE git://git.moodle.org/moodle.git --depth=1 && \
	mv /tmp/moodle/* /var/www/html/ && \
	rm /var/www/html/index.html && \
	chown -R www-data:www-data /var/www/html && \
	chmod +x /etc/apache2/foreground.sh

RUN echo "*/5 * * * * root /usr/bin/php /var/www/html/admin/cli/cron.php >> /var/log/cron.log 2>&1" > /etc/cron.d/moodle_cron

# Enable SSL, moodle requires it
RUN a2enmod ssl && a2ensite default-ssl # if using proxy, don't need actually secure connection

CMD ["/etc/apache2/foreground.sh"]

