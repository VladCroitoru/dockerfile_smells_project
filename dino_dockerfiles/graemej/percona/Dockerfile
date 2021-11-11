FROM ubuntu:14.04

# Install Percona Server, client, toolkit
RUN \
  apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A && \
  echo "deb http://repo.percona.com/apt `lsb_release -cs` main" > /etc/apt/sources.list.d/percona.list && \
  apt-get update && \
  apt-get install -y percona-server-server-5.6 percona-server-client-5.6 percona-toolkit percona-xtrabackup

ADD my.cnf /etc/mysql/my.cnf

ADD create-users.sh /usr/local/bin/create-users.sh

RUN /usr/local/bin/create-users.sh

# Define default command.
CMD ["mysqld_safe"]

# Expose ports.
EXPOSE 3306
