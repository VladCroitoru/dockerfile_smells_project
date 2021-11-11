FROM centos:centos6

MAINTAINER coleman <coleman_dlut@hotmail.com>

ENV MYSQL_ROOT_PASSWD password

#************************************************************
#*  Updateし、Mysqlをインストールする                       *
#************************************************************
RUN yum -y update && yum -y install mysql-server expect && yum clean all

#************************************************************
#*  mysql_secure_installationを利用して、Mysqlを初期化する  *
#************************************************************
RUN /etc/init.d/mysqld start && \
expect -c "
spawn /usr/bin/mysql_secure_installation
expect \"(enter for none):\"
send \"\r\"
expect \"\[Y/n\]\"
send \"Y\r\"
expect \"New password:\"
send \"$MYSQL_ROOT_PASSWD\r\"
expect \"Re-enter new password:\"
send \"$MYSQL_ROOT_PASSWD\r\"
expect \"\[Y/n\]\"
send \"Y\r\"
expect \"\[Y/n\]\"
send \"Y\r\"
expect \"\[Y/n\]\"
send \"Y\r\"
" \
&& /etc/init.d/mysqld stop

VOLUME  ["/var/lib/mysql"]

EXPOSE 3306

CMD ["/usr/bin/mysqld_safe"]
