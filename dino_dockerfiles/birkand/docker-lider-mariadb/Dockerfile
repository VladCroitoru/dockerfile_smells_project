FROM phusion/baseimage:0.9.8
MAINTAINER Birkan Duman <birkan.duman@gmail.com>

ENV HOME /root
ENV MYS_DB_NAME mys
ENV MYS_DB_USER mys
ENV MYS_DB_PASS mys
ENV HUBBLE_DB_NAME hubble
ENV HUBBLE_DB_USER hubble
ENV HUBBLE_DB_PASS hubble

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install MariaDB.
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0xcbcb082a1bb943db && \
  echo "deb http://mariadb.mirror.iweb.com/repo/10.0/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/mariadb.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server && \
  rm -rf /var/lib/apt/lists/* && \
  sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf
  
RUN \
  echo "mysqld_safe &" > /tmp/config && \
  echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config && \
  echo "mysql -e 'CREATE USER \"$MYS_DB_USER\"@\"%\" IDENTIFIED BY \"$MYS_DB_PASS\";'" >> /tmp/config && \
  echo "mysql -e 'CREATE USER \"$HUBBLE_DB_USER\"@\"%\" IDENTIFIED BY \"$HUBBLE_DB_PASS\";'" >> /tmp/config && \
  echo "mysql -e 'CREATE DATABASE $MYS_DB_NAME CHARACTER SET utf8 COLLATE utf8_general_ci;'" >> /tmp/config && \
  echo "mysql -e 'CREATE DATABASE $HUBBLE_DB_NAME CHARACTER SET utf8 COLLATE utf8_general_ci;'" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON $MYS_DB_NAME.* TO \"$MYS_DB_USER\"@\"%\";'" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON $HUBBLE_DB_NAME.* TO \"$HUBBLE_DB_USER\"@\"%\";'" >> /tmp/config && \
  bash /tmp/config && \
  rm -f /tmp/config

# Define mountable directories.
VOLUME ["/etc/mysql", "/var/lib/mysql"]

# Define working directory.
WORKDIR /data


#RUN mkdir /etc/service/mariadb
#ADD run /etc/service/slapd/run
#COPY slapd.sh /usr/sbin/run


RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#CMD ["run"]

# Define default command.
CMD ["mysqld_safe"]
#CMD ["mysqld"]

# Expose ports.
EXPOSE 3306
