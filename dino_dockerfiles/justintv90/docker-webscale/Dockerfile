# vim:set ft=dockerfile:
FROM ubuntu:vivid

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r mysql && useradd -r -g mysql mysql

RUN mkdir /docker-entrypoint-initdb.d

#Install Webscale 

RUN apt-get update
#RUN apt-get upgrade
RUN apt-get install -y bison cmake g++ gcc git libaio-dev libncurses5-dev libreadline-dev make

RUN git clone https://github.com/webscalesql/webscalesql-5.6.git
RUN cd webscalesql-5.6 && \
    cmake . -DBUILD_CONFIG=mysql_release -DENABLE_DOWNLOADS=1 && \
    make && \
    make install && \
    cd .. && \
    rm -rf webscalesql-5.6

#Config mysql

RUN cd /usr/local/mysql && \
    chown -R mysql . && \
    chgrp -R mysql . && \
    scripts/mysql_install_db --user=mysql && \
    chown -R root . && \
    chown -R mysql data && \
    echo "bind-address = 0.0.0.0" >> my.cnf && \
    cp support-files/mysql.server /etc/init.d/mysql.server

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /

RUN apt-get purge -y bison cmake g++ gcc git libaio-dev libncurses5-dev libreadline-dev make

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]
