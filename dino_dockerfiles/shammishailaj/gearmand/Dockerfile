FROM ubuntu:16.04
ARG DEBIAN_FRONTEND=noninteractive
RUN ln -sf ../usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo -e "LC_ALL=\"en_US.UTF-8\"\nLANG=\"en_US.UTF-8\"\nLANGUAGE=\"en_US.UTF-8\"\nLC_TYPE=\"UTF-8\"\n" | tee -a /etc/environment && export LC_ALL="en_US.UTF-8" && export LANG="en_US.UTF-8" && export LANGUAGE="en_US.UTF-8" && export LC_TYPE="UTF-8"
RUN apt-get update && apt-get -y install apt-utils && apt-get -y upgrade
RUN echo "mysql-server mysql-server/root_password password 123456" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password 123456" | debconf-set-selections
RUN apt-get -y install mysql-server wget g++ make libevent-dev uuid-dev libmysql++-dev python-sphinx libtool automake libsqlite3-dev libssl-dev libmemcached-dev git gperf libboost-program-options-dev && wget https://github.com/gearman/gearmand/releases/download/1.1.16/gearmand-1.1.16.tar.gz && tar -xvzf gearmand-1.1.16.tar.gz && rm gearmand-1.1.16.tar.gz && cd gearmand-1.1.16 && ./configure --enable-ssl && make && make install
RUN echo -e "\n[mysqld]\nbind-address = 0.0.0.0\nsql_mode = NO_ENGINE_SUBSTITUTION\n" | tee -a /etc/mysql/conf.d/mysql.cnf
RUN service mysql restart && mysqladmin -u root -p123456 create gearman && touch /var/log/gearmand.log && apt-get -y remove g++ make libevent-dev uuid-dev libmysql++-dev python-sphinx libtool automake libsqlite3-dev libssl-dev libmemcached-dev gperf libboost-program-options-dev && apt-get -y autoremove && apt-get -y install libmysqlclient20 libboost-program-options1.58.0 libmemcached11 libevent-2.0-5
EXPOSE 4730 8080
CMD gearmand --listen 0.0.0.0 --port 4730 --queue-type mysql --mysql-host localhost --mysql-port 3306 --mysql-user root --mysql-password 123456 --mysql-db gearman --log-file /var/log/gearmand.log --verbose DEBUG --http-port=8080 --protocol=http