# Python3-oracle-pgsql-pandas base image
#
# VERSION               1.0

FROM      python:3.6
MAINTAINER Miura Takuma <m.takuma@gmail.com>

# Install alien
RUN apt-get -y update
RUN apt-get install -y alien

# Install Oracle Instant Client 12 from Pennsylvania State University repository
RUN curl -O http://repo.dlt.psu.edu/RHEL5Workstation/x86_64/RPMS/oracle-instantclient12.1-basic-12.1.0.1.0-1.x86_64.rpm
RUN curl -O http://repo.dlt.psu.edu/RHEL5Workstation/x86_64/RPMS/oracle-instantclient12.1-devel-12.1.0.1.0-1.x86_64.rpm
RUN alien -i *.rpm
RUN rm *.rpm

# Setup Oracle environment
ENV ORACLE_HOME /usr/lib/oracle/12.1/client64
RUN echo $ORACLE_HOME/lib > /etc/ld.so.conf.d/oracle.conf
RUN ldconfig

# Install Python Packages
RUN pip3 install requests cx_oracle sqlalchemy pyyaml pandas psycopg2 nose openpyxl paramiko cryptography xlrd
