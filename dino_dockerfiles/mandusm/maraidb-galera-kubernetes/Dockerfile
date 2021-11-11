FROM ubuntu:16.04
MAINTAINER Mandus Momberg <mandus@momberg.me>

ENV MYSQL_DATA_DIR="/opt/mysql/data" MYSQL_ROOT_PASSWORD="c-krit"

RUN apt update && \
DEBIAN_FRONTEND=noninteractive apt install -y software-properties-common && \
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 && \
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.heanet.ie/mirrors/mariadb/repo/10.1/ubuntu xenial main' && \
apt update && \
DEBIAN_FRONTEND=noninteractive apt install -y mariadb-server

RUN /usr/bin/mysql_install_db --datadir=/opt/mysql/data

ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]