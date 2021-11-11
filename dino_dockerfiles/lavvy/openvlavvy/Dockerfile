FROM debian:jessie

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server php5-mysql pwgen wget net-tools iptables nano sudo php-apc php5-mcrypt
  
ADD run.sh /run.sh
RUN chmod 755 /*.sh
RUN rm -rf /var/lib/mysql/*

# Add MySQL utils
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
RUN chmod 755 /*.sh

# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]
EXPOSE 80 3306
CMD ["/run.sh"]
  
