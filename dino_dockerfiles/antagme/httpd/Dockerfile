FROM ubuntu:14.04
MAINTAINER "Pedro Romero Aguado" <pedroromeroaguado@gmail.com> 
ENV DEBIAN_FRONTEND noninteractive
COPY /scripts/dfg.sh /usr/local/bin/dfg.sh
COPY /files/zabbix.backup /var/tmp/zabbix.backup

RUN locale-gen en_US.UTF-8 && \
    apt-get update && apt-get install wget -y && \
    wget http://repo.zabbix.com/zabbix/3.2/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.2-1+trusty_all.deb && \
    dpkg -i zabbix-release_3.2-1+trusty_all.deb && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install  vim apache2 openssh-server supervisor zabbix-agent zabbix-server-mysql zabbix-frontend-php  php5-mysql dos2unix -y && \
    apt-get clean && \
    rm -rf /tmp/* /var/lib/apt/lists/* && \
    
    dos2unix /usr/local/bin/dfg.sh &&\
    dos2unix "/var/tmp/zabbix.backup" &&\
    chmod +x /usr/local/bin/dfg.sh && \
    a2enconf zabbix.conf && \
    chmod -R 0777  /etc/zabbix && \
    chmod -R 0777  /var/tmp/ && \
    mkdir /var/run/zabbix && \
    chmod -R 0777 /var/run/zabbix && \
    /bin/bash -c "/usr/bin/mysqld_safe &" && \
    sleep 5 && \
    mysql -e "create user 'zabbix'@'localhost';" && \
    mysql -e "create database zabbix;" && \
    cd /var/tmp && cat "/var/tmp/zabbix.backup" | mysql -uroot zabbix && \
    mysql -e "grant all privileges on zabbix.* to 'zabbix'@'localhost';" && \
    mysql -e "flush privileges;" 
    
#cd /usr/share/doc/zabbix-server-mysql && zcat create.sql.gz | mysql -uroot zabbix 
ENV NOTVISIBLE "in users profile"
#-------------------------------------------------------------------------------------------------------
COPY /files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY /files/zabbix.conf /etc/apache2/conf-available/zabbix.conf
COPY /files/zabbix.conf.php /etc/zabbix/web/zabbix.conf.php 
# COPY conf/zabbix_server.conf /etc/zabbix/zabbix_server.conf

VOLUME /var/lib/mysql

EXPOSE 10051 80 3306
CMD ["/usr/bin/supervisord"]    
