FROM centos:6

RUN \ 
  yum -y update && yum clean all && \
  rpm -Uvh http://www.percona.com/downloads/percona-release/percona-release-0.0-1.x86_64.rpm && \
  yum -y install \
  inotify-tools \
  Percona-Server-client-55-5.5.41-rel37.0.el6 \
  Percona-Server-server-55-5.5.41-rel37.0.el6 \
  Percona-Server-shared-55-5.5.41-rel37.0.el6 \
  percona-xtrabackup-2.2.8-5059.el6 && \
  mkdir -p /etc/mysql/conf.d \
    && { \
      echo '[mysqld]'; \
      echo '!includedir /etc/mysql/conf.d/'; \
    } > /etc/mysql/my.cnf \
    && { \
      echo '[mysqld]'; \
      echo 'user = mysql'; \
      echo 'datadir = /var/lib/mysql'; \
    } > /etc/mysql/conf.d/docker.cnf

RUN \
  mysqld_safe & \
  /usr/bin/mysqladmin --silent --wait=30 ping || exit 1 && \
  mysql -e 'GRANT ALL PRIVILEGES ON *.* TO "root"@"%" WITH GRANT OPTION;'

VOLUME ["/var/lib/mysql", "/etc/mysql/conf.d/"]

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]
