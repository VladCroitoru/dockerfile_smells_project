# # MariaDB Galera 5.5.39/Ubuntu 14.04 64bit
FROM ubuntu:14.04
MAINTAINER Pythian Nikolaos Vyzas <vyzas@pythian.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list # add the universe repo
RUN apt-get -q -y update # update apt
RUN apt-get -q -y install software-properties-common wget unzip curl # install software-properties-common for key management
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db # add the key for Mariadb Ubuntu repos
RUN add-apt-repository 'deb http://ftp.cc.uoc.gr/mirrors/mariadb/repo/5.5/ubuntu trusty main' # add the MariaDB repository for 5.5
RUN apt-get -q -y update # update apt again
RUN echo mariadb-galera-server-5.5 mysql-server/root_password password root | debconf-set-selections # configure the default root password during installation
RUN echo mariadb-galera-server-5.5 mysql-server/root_password_again password root | debconf-set-selections # confirm the password (as in the usual installation)
RUN LC_ALL=en_US.utf8 DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::='--force-confnew' -qqy install mariadb-galera-server galera mariadb-client # install the necessary packages
ADD ./my.cnf /etc/mysql/my.cnf 
# upload the locally created my.cnf (obviously this can go into the default MariaDB path
RUN service mysql restart 
# startup the service - this will fail since the nodes haven't been configured on first boot
RUN mkdir -p /data
EXPOSE 3306 4444 4567 4568 
# open the ports required to connect to MySQL and for Galera SST / IST operations
ADD start /bin/start
RUN chmod +x /bin/start
