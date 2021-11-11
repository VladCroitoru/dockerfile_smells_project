FROM edbizarro/bitbucket-pipelines-php7:latest

MAINTAINER Eduardo Bizarro <edbizarro@gmail.com>

# MYSQL ROOT PASSWORD
ARG MYSQL_ROOT_PASS=root    

# MYSQL
# /usr/bin/mysqld_safe
RUN service mysql stop && \
    DEBIAN_FRONTEND=noninteractive apt-get remove --purge -qqy mysql-server-5.7 && \
    rm /var/lib/mysql/debian-5.7.flag && \
    rm -rf /etc/mysql/ /var/lib/mysql
    
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y 'deb http://archive.ubuntu.com/ubuntu trusty universe' && \
    bash -c 'debconf-set-selections <<< "mysql-server-5.6 mysql-server/root_password password $MYSQL_ROOT_PASS"' && \
		bash -c 'debconf-set-selections <<< "mysql-server-5.6 mysql-server/root_password_again password $MYSQL_ROOT_PASS"' && \
		DEBIAN_FRONTEND=noninteractive apt-get update && \
		DEBIAN_FRONTEND=noninteractive apt-get install -qqy mysql-server-5.6

RUN apt-get clean -y && \
		apt-get autoremove -y && \
		rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
