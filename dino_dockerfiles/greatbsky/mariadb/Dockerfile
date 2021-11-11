FROM greatbsky/centos7
MAINTAINER architect.bian
LABEL name="mariadb" license="GPLv2" build-date="20161125"

RUN yum clean all && yum update -y
RUN groupadd -r mysql && useradd -r -g mysql mysql && mkdir  -p /data/env/mariadb && cd /data/softs && wget -O mariadb.tar.gz http://downloads.mariadb.com/MariaDB/mariadb-10.1/yum/rhel/mariadb-10.1.19-rhel-7-x86_64-rpms.tar && tar -xf mariadb.tar.gz && cd mariadb-10.1.19-rhel-7-x86_64-rpms && ./setup_repository && yum install -y MariaDB-server && rm -rf /data/softs/mariadb-* && cp /var/lib/mysql/* /data/env/mariadb -r && chown -R mysql:mysql /data/env/mariadb

VOLUME /data/env/mariadb

COPY my.conf /etc/my.cnf
EXPOSE 3306

CMD chown -R mysql:mysql /data/env/mariadb && mysqld --user=mysql
