# CentOS
#
# VERSION               0.0.1

FROM     centos:centos6

MAINTAINER Spring_MT

RUN yum install -y \
    epel-release \
    openssl-devel \
    readline-devel\
    zlib-devel \
    gcc \
    gcc-c++ \
    cmake \
    ncurses-devel \
    perl \
    wget \
    curl \
    git \
    vim \
    tar \
    python \
&&  yum groupinstall "Development Tools" -y \
&&  yum clean all

ENV MYSQL_VERSION 5.6.35
ENV Q4M_VERSION 0.9.14
ENV MYSQLDIR /var/lib/mysql

RUN groupadd -r mysql && useradd -r -g mysql mysql

RUN mkdir /docker-entrypoint-initdb.d

# install mysql-build
RUN set -x \
&& mkdir /usr/local/src/mysql-build \
&& curl -s -L https://github.com/kamipo/mysql-build/archive/master.tar.gz | tar --verbose --extract --gzip --directory /usr/local/src/mysql-build --strip-components 1 \
&& rm -rf /var/lib/mysql \
&& mkdir -p /var/lib/mysql /var/run/mysqld \
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \
&& chmod 777 /var/run/mysqld \
&& /usr/local/src/mysql-build/bin/mysql-build -v $MYSQL_VERSION $MYSQLDIR q4m-$Q4M_VERSION \
&& chown -R mysql:mysql /var/lib/mysql \
&& rm -rf /usr/local/src/mysql-build

COPY ./my.cnf /etc/my.cnf

VOLUME $MYSQLDIR
#WORKDIR $MYSQLDIR

ENV PATH $MYSQLDIR/bin:$PATH
ENV PATH $MYSQLDIR/scripts:$PATH

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld", "--user=mysql"]

