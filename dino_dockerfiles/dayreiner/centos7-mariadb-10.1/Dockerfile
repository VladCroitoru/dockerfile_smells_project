FROM centos:centos7
MAINTAINER dayreiner

ENV MARIADB_MAJOR=10.1

# MariaDB Repo
COPY config/MariaDB.repo /etc/yum.repos.d/MariaDB.repo

# Install required packages and MariaDB Vendor Repo
RUN yum -y update && yum clean all && \
    rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \
    yum -y install MariaDB-server MariaDB-client && yum clean all && \
    mkdir /docker-entrypoint-initdb.d

COPY config/server.cnf /etc/my.cnf.d/server.cnf
COPY scripts/docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 3306
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["mysqld"]
