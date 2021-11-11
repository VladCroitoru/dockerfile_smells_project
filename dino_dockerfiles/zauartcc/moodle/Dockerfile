# Docker-Moodle
# Dockerfile for moodle instance. more dockerish version of https://github.com/sergiogomez/docker-moodle
# Forked from Jon Auer's docker version. https://github.com/jda/docker-moodle
FROM ubuntu:16.04
MAINTAINER Aaron Osher <aaron@aaronosher.io>

VOLUME ["/var/moodledata"]
EXPOSE 80 443
COPY moodle-config.php /var/www/html/config.php

# Keep upstart from complaining
# RUN dpkg-divert --local --rename --add /sbin/initctl
# RUN ln -sf /bin/true /sbin/initctl

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

ENV FORCE_DEBUG false

ENV VERSION MOODLE_33_STABLE

# Database info and other connection information derrived from env variables. See readme.
# Set ENV Variables externally Moodle_URL should be overridden.
ENV MOODLE_URL http://127.0.0.1

ADD ./foreground.sh /etc/apache2/foreground.sh

RUN apt-get update && \
	apt-get -y install mysql-client pwgen python-setuptools curl git unzip apache2 php \
		php-gd libapache2-mod-php postfix wget supervisor php-pgsql curl libcurl3 \
		libcurl3-dev php-curl php-xmlrpc php-intl php-mysql git-core php-xml php-mbstring php-zip php-soap cron php7.0-ldap && \
	cd /tmp && \
	git clone -b ${VERSION} git://git.moodle.org/moodle.git --depth=1 && \
	mv /tmp/moodle/* /var/www/html/ && \
	rm /var/www/html/index.html && \
	cd /var/www/html/auth && \
	git clone -b VERSION_1 https://github.com/ZAUARTCC/moodle-auth.git --depth=1 zauartcc && \
  cd /var/www/html/theme && \
  git clone -b ${VERSION} https://github.com/ZAUARTCC/moodle-theme.git --depth=1 enlightlite

COPY php.ini /var/www/html/php.ini
COPY php.ini /etc/php/7.0/apache2/php.ini

RUN chown -R www-data:www-data /var/www/html && \
	chmod +x /etc/apache2/foreground.sh

#cron
COPY moodlecron /etc/cron.d/moodlecron
RUN chmod 0644 /etc/cron.d/moodlecron

# Enable SSL, moodle requires it
RUN a2enmod ssl && a2ensite default-ssl  #if using proxy dont need actually secure connection

# Cleanup, this is ran to reduce the resulting size of the image.
RUN apt-get clean autoclean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/lib/dpkg/* /var/lib/cache/* /var/lib/log/*

CMD ["/etc/apache2/foreground.sh"]
