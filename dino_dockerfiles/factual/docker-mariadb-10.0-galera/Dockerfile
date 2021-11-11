FROM boritzio/docker-base
MAINTAINER Maxime Devalland <maxime@factual.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -q -y update
RUN apt-get -q -y install software-properties-common wget unzip curl
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
RUN add-apt-repository 'deb http://ftp.cc.uoc.gr/mirrors/mariadb/repo/10.0/ubuntu trusty main'
RUN apt-get -q -y update
RUN echo mariadb-galera-server-10.0 mysql-server/root_password password root | debconf-set-selections
RUN echo mariadb-galera-server-10.0 mysql-server/root_password_again password root | debconf-set-selections
RUN LC_ALL=en_US.utf8 DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::='--force-confnew' -qqy install mariadb-galera-server galera mariadb-client

RUN service mysql restart

ADD start /bin/start
RUN chmod +x /bin/start
