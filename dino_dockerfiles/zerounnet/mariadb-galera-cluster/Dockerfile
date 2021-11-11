FROM centos

MAINTAINER ZerounNet

COPY mariadb.repo /etc/yum.repos.d/mariadb.repo
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN yum -y update && \
    rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \
    groupadd -r mysql && useradd -r -g mysql mysql && \
    yum -y install http://www.percona.com/downloads/percona-release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm && \
    yum -y install MariaDB-server MariaDB-client galera percona-xtrabackup-24 which socat && \
    yum clean all && \
    mkdir /docker-entrypoint-initdb.d && \
    chmod u+x /docker-entrypoint.sh

COPY server.cnf /etc/my.cnf.d/server.cnf

EXPOSE 3306 4444 4567 4568 
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["mysqld"]
