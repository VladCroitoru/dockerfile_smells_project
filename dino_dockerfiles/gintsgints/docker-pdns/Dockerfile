# docker-pdns
#
# VERSION 0.1

FROM centos:7
MAINTAINER Gints Polis <gints.polis@lattelecom.lv>

# EPEL7 for additional packages
RUN yum -y install http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

# Development tools
RUN yum -y groupinstall "Development Tools"

# PG repo
RUN rpm -i https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm

# Install server itself
RUN yum install -y postgresql95-server postgresql95-contrib

# Install power dns and backends
RUN yum install -y pdns bind-utils pdns-backend-postgresql.x86_64

# initialize DB data files
RUN su - postgres -c '/usr/pgsql-9.5/bin/initdb -D /var/lib/pgsql/data'

# set permissions to allow logins, trust the bridge, this is the default for docker YMMV
RUN echo "host    all             all             172.17.42.1/32            trust" >> /var/lib/pgsql/data/pg_hba.conf

#listen on all interfaces
RUN echo "listen_addresses='*'" >> /var/lib/pgsql/data/postgresql.conf

ADD ./pdns.conf /etc/pdns/pdns.conf
ADD ./pdns.sql /pdns.sql
ADD ./start.sh /start.sh
RUN chmod u+x /start.sh

RUN yum install -y postgresql93-devel nodejs npm
RUN PATH=/usr/pgsql-9.3/bin/:$PATH npm install pgproc.http

EXPOSE 5432
EXPOSE 53
EXPOSE 53/udp
EXPOSE 8053
EXPOSE 5380

CMD ./start.sh
