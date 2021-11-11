FROM phusion/baseimage

RUN echo '#!/bin/sh' "\nexit 0" >  /usr/sbin/policy-rc.d

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A

RUN echo "deb http://repo.percona.com/apt precise main" >> /etc/apt/sources.list
RUN echo "deb-src http://repo.percona.com/apt precise main" >> /etc/apt/sources.list
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes percona-server-server-5.6 percona-server-client-5.6

RUN echo "[mysqld]\nbind-address=0.0.0.0" > /etc/mysql/my.cnf

RUN mkdir /etc/service/percona
ADD run.sh /etc/service/percona/run
RUN chmod 755 /etc/service/percona/run

EXPOSE 3306
VOLUME ["/var/lib/mysql"]

CMD ["/sbin/my_init"]