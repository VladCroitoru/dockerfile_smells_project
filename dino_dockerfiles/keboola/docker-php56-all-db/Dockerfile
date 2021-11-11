#VERSION 1.0.0
FROM keboola/base-php56
MAINTAINER Miro Cillik <miro@keboola.com>

# Install required tools
RUN yum install -y wget && yum install -y tar
RUN yum -y install vim
RUN yum -y --enablerepo=epel,remi,remi-php56 install php-devel
RUN yum -y --enablerepo=epel,remi,remi-php56 install gcc
RUN yum -y --enablerepo=epel,remi,remi-php56 install make
RUN yum -y --enablerepo=epel,remi,remi-php56 install php-pear
RUN yum -y --enablerepo=epel,remi,remi-php56 install php-mysql
RUN yum -y --enablerepo=epel,remi,remi-php56 install php-mssql
RUN yum -y --enablerepo=epel,remi,remi-php56 install php-odbc

# Oracle
ADD oracle/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm /tmp/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
ADD oracle/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm /tmp/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm
ADD oracle/oracle.sh /tmp/oracle.sh
RUN yum -y --nogpgcheck install /tmp/oracle-instantclient*
RUN export LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib/
RUN export ORACLE_HOME=/usr/lib/oracle/12.1/client64/lib/
RUN echo 'instantclient,/usr/lib/oracle/12.1/client64/lib/' | pecl install -f oci8-1.4.10
RUN echo "extension=oci8.so" > /etc/php.d/30-oci8.ini

# Cloudera
RUN yum -y install unixODBC
RUN yum -y install cyrus-sasl-gssapi
RUN yum -y install cyrus-sasl-plain
ADD cloudera/ClouderaImpalaODBC-2.5.30.1011-1.el6.x86_64.rpm /tmp/ClouderaImpalaODBC-2.5.30.1011-1.el6.x86_64.rpm
RUN ln  -s  /usr/lib64/libsasl2.so.3  /usr/lib64/libsasl2.so.2
RUN rpm -ivh ClouderaImpalaODBC* --nodeps

RUN cp -Rf /opt/cloudera/impalaodbc/Setup/* /etc/
ADD cloudera/odbc.ini /etc/odbc.ini
ADD cloudera/cloudera.impalaodbc.ini /etc/cloudera.impalaodbc.ini
ADD cloudera/cloudera.impalaodbc.ini /opt/cloudera/impalaodbc/lib/64/cloudera.impalaodbc.ini
RUN ln -s /usr/lib64/libodbccr.so.2 /usr/lib64/libodbccr.so

ENV ODBCSYSINI /etc
ENV ODBCINI /etc/odbc.ini
ENV SIMBAINI /opt/cloudera/impalaodbc/lib/64/cloudera.impalaodbc.ini

# MSSQL
ADD mssql/freetds.conf /etc/freetds.conf

# resources
#https://sskaje.me/2014/07/php-odbc-connect-cloudera-impala-hive/
#http://www.shekhargovindarajan.com/open-source/connect-and-query-cloudera-impala-using-php-odbc-on-centos-7/




