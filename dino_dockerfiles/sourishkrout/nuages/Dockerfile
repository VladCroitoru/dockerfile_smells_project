FROM ubuntu:precise

MAINTAINER Sebastian Tiedtke <sebastiantiedtke@gmail.com> version: 0.1

RUN \
  echo "deb http://archive.ubuntu.com/ubuntu precise universe" >> /etc/apt/sources.list ;\
  apt-get update ;\
  apt-get install -y --force-yes mysql-server ;\
  sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf ;\
  /usr/bin/mysqld_safe & \
  sleep 10s && \
  mysql -e "GRANT ALL ON *.* to 'root'@'%'; FLUSH PRIVILEGES"
# END RUN

EXPOSE 3306
CMD /usr/bin/mysqld_safe
