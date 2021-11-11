FROM ubuntu:precise

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server php5-mysql pwgen php-apc php5-mcrypt php5-curl php5-gd vim curl gawk python-setuptools python-setproctitle && \
  echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Add image configuration and scripts
ADD start-apache2.sh /start-apache2.sh
ADD start-mysqld.sh /start-mysqld.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD my.cnf /etc/mysql/conf.d/my.cnf
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf

# Enable SSH
RUN apt-get -y install openssh-server pwgen
RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

# Configure SSH
ADD supervisord-sshd.conf /etc/supervisor/conf.d/supervisord-sshd.conf
ADD set_root_pw.sh /set_root_pw.sh
ADD run_sshd.sh /run_sshd.sh 
RUN chmod +x /*.sh

# Remove pre-installed database
RUN rm -rf /var/lib/mysql/*

# Add MySQL utils
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
RUN chmod 755 /*.sh

# config to enable .htaccess
ADD apache_default /etc/apache2/sites-available/default

# Enable Apache Modules 
RUN a2enmod rewrite
RUN a2enmod headers

# PHP Pear Modules
RUN apt-get install -y php-pear
RUN pear install -o MDB2
RUN pear install -o Mail
RUN pear install -o Mail_mime
RUN pear install -o Log
RUN pear install -o Net_SMTP

# Enable XDebug
RUN apt-get install php5-xdebug 
RUN rm /etc/php5/apache2/php.ini 
ADD php.ini /etc/php5/apache2/php.ini

#Enviornment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

ENV AUTHORIZED_KEYS **None**
ENV MYSQL_PASS password

EXPOSE 80 3306 22 9000
CMD ["/run.sh"]
