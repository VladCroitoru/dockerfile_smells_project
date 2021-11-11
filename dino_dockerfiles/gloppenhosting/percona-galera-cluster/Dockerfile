FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A
RUN echo "deb http://repo.percona.com/apt jessie main" >> /etc/apt/sources.list
RUN echo "deb-src http://repo.percona.com/apt jessie main" >> /etc/apt/sources.list
RUN apt-get update -yqq
RUN apt-get install --no-install-recommends --no-install-suggests -yqq host socat unzip ca-certificates wget curl
RUN apt-get install -y percona-xtradb-cluster-client-5.6 percona-xtradb-cluster-server-5.6 percona-xtradb-cluster-galera-3.x percona-xtrabackup

# install galera-healthcheck
RUN wget -O /bin/galera-healthcheck 'https://github.com/sttts/galera-healthcheck/releases/download/v20150303/galera-healthcheck_linux_amd64'
RUN test "$(sha256sum /bin/galera-healthcheck | awk '{print $1;}')" = "86f60d9d82b1f9d2d474368ed7e81a0a361508031a292244847136b0ed2ee770"
RUN chmod +x /bin/galera-healthcheck

# Install etcd
WORKDIR /
RUN curl -skL https://github.com/coreos/etcd/releases/download/v2.2.0/etcd-v2.2.0-linux-amd64.tar.gz | tar xz

# configure mysqld
#RUN sed -i 's/#? *bind-address/# bind-address/' /etc/mysql/my.cnf
#RUN sed -i 's/#? *log-error/# log-error/' /etc/mysql/my.cnf

COPY conf.d/galera.cnf /etc/mysql/my.cnf
RUN chmod 0644 /etc/mysql/my.cnf

COPY random.sh /tmp/random.sh
RUN /tmp/random.sh

RUN cat /etc/mysql/my.cnf

EXPOSE 3306 4444 4567 4568

VOLUME ["/var/lib/mysql"]

COPY mysqld.sh /mysqld.sh
COPY start /start

RUN chmod 555 /start /mysqld.sh

ENTRYPOINT ["/start"]
