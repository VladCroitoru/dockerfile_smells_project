FROM yangqi/docker-debian
MAINTAINER Qi Yang <i@yangqi.me>

ENV DEBIAN_FRONTEND noninteractive
ENV MYSQL_ROOT_PASSWORD '123456'

WORKDIR /root

RUN \
  apt-get update && \
  apt-get install -y wget procps psmisc debconf debconf-utils perl && \
  wget -q http://dev.mysql.com/get/mysql-apt-config_0.3.6-1debian8_all.deb && \
  echo mysql-apt-config	mysql-apt-config/select-server	select	mysql-5.6 | debconf-set-selections && \
  echo mysql-apt-config	mysql-apt-config/select-product	select	Apply | debconf-set-selections && \
  dpkg -i mysql-apt-config_0.3.6-1debian8_all.deb && \
  apt-get update && \
  echo mysql-community-server	mysql-community-server/root-pass password $MYSQL_ROOT_PASSWORD | debconf-set-selections && \
  echo mysql-community-server	mysql-community-server/re-root-pass	password $MYSQL_ROOT_PASSWORD | debconf-set-selections && \
  apt-get install -y mysql-community-server

ADD my.cnf /etc/mysql/my.cnf
ADD startup.sh startup.sh

VOLUME ["/etc/mysql", "/var/lib/mysql", "/var/log/mysql"]

CMD ["/bin/bash", "startup.sh"]

EXPOSE 3306
