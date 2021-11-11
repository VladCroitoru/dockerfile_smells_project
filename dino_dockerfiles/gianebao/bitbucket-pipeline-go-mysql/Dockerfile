FROM golang:latest
MAINTAINER Gian Carlo Val Ebao <gianebao@gmail.com>

ENV MYSQL_MAJOR 5.7
ENV MYSQL_ROOT_PASSWORD root
ENV GOOSE_DIR /db

# Update and Fix Language
RUN \
 apt-get update && apt-get -y upgrade &&\
 apt-get -y --no-install-recommends install locales &&\
 echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\
 locale-gen en_US.UTF-8 &&\
 /usr/sbin/update-locale LANG=en_US.UTF-8

# Add MySQL repository
RUN \
 apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5 &&\
 echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-$MYSQL_MAJOR" > /etc/apt/sources.list.d/mysql.list &&\
 apt-get update &&\
 { \
       echo mysql-community-server mysql-community-server/data-dir select ''; \
       echo mysql-community-server mysql-community-server/root-pass password $MYSQL_ROOT_PASSWORD; \
       echo mysql-community-server mysql-community-server/re-root-pass password $MYSQL_ROOT_PASSWORD; \
       echo mysql-community-server mysql-community-server/remove-test-db select false; \
   } | debconf-set-selections &&\
 apt-get -y --no-install-recommends install mysql-server

# Install built in's
RUN \
 apt-get -y --no-install-recommends install mysql-client redis-server &&\
 apt-get autoclean && apt-get clean && apt-get autoremove

# Install Goose
RUN go get bitbucket.org/liamstask/goose/cmd/goose
