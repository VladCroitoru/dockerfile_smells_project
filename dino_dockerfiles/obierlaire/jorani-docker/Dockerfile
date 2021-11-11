FROM ubuntu:15.10
RUN apt-get update -y
RUN apt-get install -y unzip apache2 php5 libapache2-mod-php5 php5-ldap apache2-utils
RUN apt-get install -y wget
RUN apt-get install -y php5-mysql
RUN php5enmod mcrypt
RUN php5enmod openssl
RUN wget https://github.com/bbalet/jorani/archive/v0.4.3.tar.gz
RUN rm -Rf /var/www/html
RUN tar zxvf v0.4.3.tar.gz
RUN mv /jorani-0.4.3 /var/www/html/
RUN a2enmod rewrite
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY database.php /var/www/html/application/config/database.php
COPY email.php /var/www/html/application/config/email.php
# Configure Apache2
ENV APACHE_RUN_USER     www-data
ENV APACHE_RUN_GROUP    www-data
ENV APACHE_LOG_DIR      /var/log/apache2
env APACHE_PID_FILE     /var/run/apache2.pid
env APACHE_RUN_DIR      /var/run/apache2
env APACHE_LOCK_DIR     /var/lock/apache2
env APACHE_LOG_DIR      /var/log/apache2
EXPOSE 80
ENTRYPOINT [ "/usr/sbin/apache2", "-DFOREGROUND" ]
