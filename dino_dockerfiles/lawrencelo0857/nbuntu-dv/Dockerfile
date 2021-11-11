FROM ubuntu:16.04
MAINTAINER 	lin law bai  <lawrencelo0857@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
Run apt-get install -y curl
RUN apt-get install -y sudo apache2
RUN apt-get install -y php7.0 libapache2-mod-php7.0 libapache2-mod-php php7.0-mysql php7.0-gd
#RUN echo 'mysql-server mysql-server/root_password password p@ssw0rd' | sudo debconf-set-selections
#RUN echo 'mysql-server mysql-server/root_password_again password p@ssw0rd' | sudo debconf-set-selections
RUN apt-get -y install mysql-server mysql-client
EXPOSE 80
CMD apachectl -D FOREGROUND
VOLUME /var/www/html
WORKDIR /var/www/html
ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars
# and then a few more from $APACHE_CONFDIR/envvars itself
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV LANG C
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR
RUN find "$APACHE_CONFDIR" -type f -exec sed -ri ' \
	s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
	s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
' '{}' ';'
ENV WORDPRESS_VERSION 4.8.2
ENV WORDPRESS_SHA1 a99115b3b6d6d7a1eb6c5617d4e8e704ed50f450
RUN set -ex; \
	curl -o wordpress.tar.gz -fSL "https://wordpress.org/wordpress-4.8.2.tar.gz"; \
	echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \
	tar -xzf wordpress.tar.gz -C /usr/src/; \
	rm wordpress.tar.gz; \
	chown -R www-data:www-data /usr/src/wordpress
# COPY apache_enable.sh /apache_enable.sh
# ENTRYPOINT ["/apache_enable.sh"]
#RUN cd /etc/apache2/sites-available/
#RUN sudo a2ensite *
# RUN sudo service apache2 reload
COPY docker-apache.conf /etc/apache2/sites-available/wordpress
#RUN find /etc/apache2/sites-available/ -type f -and -not -name "*default*" -exec a2ensite {} \;
#RUN a2dissite 000-default && a2ensite wordpress
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
