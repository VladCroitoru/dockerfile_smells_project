FROM ubuntu:14.04
MAINTAINER Homare Shimizu <homare@dova.co.jp>

#--------------------------------------------
# Initialize
#--------------------------------------------
ENV DEBIAN_FRONTEND noninteractive

# for snmp-mibs-downloader
#RUN sed -i 's/universe/universe multiverse/' /etc/apt/sources.list

#--------------------------------------------
# for Install Softwares
#--------------------------------------------
RUN apt-get update

#--------------------------------------------
# Install NTP
#--------------------------------------------
RUN apt-get install -y ntp

#--------------------------------------------
# Install Postfix
#--------------------------------------------
RUN echo "postfix postfix/main_mailer_type string Internet site" | debconf-set-selections
RUN echo "postfix postfix/mailname string mail.example.com" | debconf-set-selections
RUN apt-get install -y postfix

#--------------------------------------------
# Install Net-SNMP
#--------------------------------------------
#RUN apt-get install -y snmpd snmp-mibs-downloader

#--------------------------------------------
# Install MySQL
# root password: my_password
#--------------------------------------------
RUN echo "mysql-server-5.5 mysql-server/root_password password my_password" | debconf-set-selections
RUN echo "mysql-server-5.5 mysql-server/root_password_again password my_password" | debconf-set-selections

RUN apt-get install -y mysql-server

# for Settings
ADD custom_mysql.cnf /etc/mysql/conf.d/custom.cnf

#--------------------------------------------
# Install Apache2
#--------------------------------------------
RUN apt-get install -y apache2
RUN apt-get install -y apache2-utils

# for Settings
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

RUN mkdir /var/lock/apache2
RUN chown www-data /var/lock/apache2

#--------------------------------------------
# Install PHP5
#--------------------------------------------
RUN apt-get install -y php5

# for Settings
ADD custom_php5.ini /etc/php5/mods-available/custom.ini
RUN /usr/sbin/php5enmod custom

#--------------------------------------------
# Install Zabbix-Server
# zabbix password: zabbixpassword
#---------------------------------------------
RUN apt-get install -y zabbix-server-mysql

# for Settings
RUN (cd /usr/share/zabbix-server-mysql; /bin/gunzip data.sql.gz)
RUN (cd /usr/share/zabbix-server-mysql; /bin/gunzip images.sql.gz)
RUN (cd /usr/share/zabbix-server-mysql; /bin/gunzip schema.sql.gz)
RUN \
 /usr/bin/service mysql start && \
 sleep 10s && \
   /usr/bin/mysqladmin -u root -pmy_password create zabbix &&  \
   (/usr/bin/mysql -u root -pmy_password zabbix < /usr/share/zabbix-server-mysql/schema.sql) && \
   (/usr/bin/mysql -u root -pmy_password zabbix < /usr/share/zabbix-server-mysql/images.sql) && \
   (/usr/bin/mysql -u root -pmy_password zabbix < /usr/share/zabbix-server-mysql/data.sql) && \
   (echo 'grant all privileges on zabbix.* to zabbix@localhost identified by "zabbixpassword" with grant option;' | mysql -u root -pmy_password) && \
   (echo 'update hosts set status=0 where host="Zabbix Server"' | mysql -u root -pmy_password zabbix) && \
 /usr/bin/service mysql stop
 
RUN /bin/sed -ri 's/^START=no/START=yes/g' /etc/default/zabbix-server
RUN /bin/sed -ri 's/^# DBPassword=/DBPassword=zabbixpassword/g' /etc/zabbix/zabbix_server.conf
RUN /bin/sed -ri 's/^# DBSocket=\/tmp\/mysql.sock/DBSocket=\/var\/run\/mysqld\/mysqld.sock/g' /etc/zabbix/zabbix_server.conf

#--------------------------------------------
# Install Zabbix-Agent
#---------------------------------------------
RUN apt-get install -y zabbix-agent

#--------------------------------------------
# Install Zabbix-Frontend
#--------------------------------------------
RUN apt-get install -y zabbix-frontend-php php5-mysql
RUN apt-get install -y fonts-ipafont-gothic
RUN apt-get install -y language-pack-ja

# for Settings
RUN ln -s /usr/share/fonts/opentype/ipafont-gothic/ipag.ttf /usr/share/zabbix/fonts/ipag.ttf
RUN ln -s /usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf /usr/share/zabbix/fonts/ipagp.ttf
RUN /bin/sed -ri 's/DejaVuSans/ipagp/g' /usr/share/zabbix/include/defines.inc.php

RUN cp /usr/share/doc/zabbix-frontend-php/examples/apache.conf /etc/apache2/sites-available/zabbix.conf
RUN /usr/sbin/a2ensite zabbix

ADD zabbix.conf.php /etc/zabbix/zabbix.conf.php
RUN chmod 0444 /etc/zabbix/zabbix.conf.php

ADD index.html /var/www/html/index.html

#---------------------------------------------
# for Debugging
#---------------------------------------------
RUN apt-get install -y mysql-client
RUN apt-get install -y telnet
RUN apt-get install -y snmp
#ADD test.php /var/www/html/test.php

#--------------------------------------------
# for Service Port
#--------------------------------------------
EXPOSE 80
EXPOSE 10051

#--------------------------------------------
# for Initial Startup
#--------------------------------------------
ADD start.sh /start.sh 
RUN chmod 0755 /start.sh 
CMD ["./start.sh"] 
