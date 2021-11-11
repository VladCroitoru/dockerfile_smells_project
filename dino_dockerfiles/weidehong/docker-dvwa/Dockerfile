FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install -y sudo apache2 
RUN apt-get install -y php7.0 libapache2-mod-php7.0 libapache2-mod-php php7.0-mysql php7.0-gd

RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections

RUN apt-get update && \
	apt-get -y install mysql-server mysql-client && \
	mkdir -p /var/lib/mysql && \
	mkdir -p /var/run/mysqld && \
	mkdir -p /var/log/mysql && \
	chown -R mysql:mysql /var/lib/mysql && \
	chown -R mysql:mysql /var/run/mysqld && \
	chown -R mysql:mysql /var/log/mysql


# UTF-8 and bind-address
RUN sed -i -e "$ a [client]\n\n[mysql]\n\n[mysqld]"  /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[client\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[mysql\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[mysqld\]\)/\1\ninit_connect='SET NAMES utf8'\ncharacter-set-server = utf8\ncollation-server=utf8_unicode_ci\nbind-address = 0.0.0.0/g" /etc/mysql/my.cnf


ENV LOG_STDOUT **Boolean**
ENV LOG_STDERR **Boolean**
ENV LOG_LEVEL warn
ENV ALLOW_OVERRIDE All
ENV DATE_TIMEZONE UTC
ENV TERM dumb

COPY run-lamp.sh /usr/sbin/

RUN a2enmod rewrite && \
    chmod +x /usr/sbin/run-lamp.sh && \
    chown -R www-data:www-data /var/www/html

COPY ./DVWA /var/www/html/DVWA
RUN mkdir /var/www/html/DVWA/config
COPY ./DVWA/config.inc.php /var/www/html/DVWA/config/ 
COPY ./DVWA/php.ini /etc/php/7.0/apache2
RUN chmod 777 -R /var/www/html



VOLUME /var/www/html
VOLUME /var/log/httpd
VOLUME /var/lib/mysql
VOLUME /var/log/mysql

EXPOSE 80
CMD ["/usr/sbin/run-lamp.sh"]
