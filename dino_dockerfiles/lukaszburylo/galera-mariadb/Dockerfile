FROM ubuntu:14.04
MAINTAINER Lukasz Burylo <lukasz@burylo.com>

RUN groupadd -r mysql && useradd -r -g mysql mysql

RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
RUN echo "deb http://mirror.jmu.edu/pub/mariadb/repo/10.0/ubuntu trusty main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y mariadb-client mariadb-galera-server galera --no-install-recommends && rm -rf /var/lib/apt/lists/*

ADD my.cnf /etc/mysql/my.cnf
ADD entrypoint.sh /entrypoint.sh

VOLUME /var/lib/mysql

EXPOSE 3306 4444 4567 4568

ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld"]
