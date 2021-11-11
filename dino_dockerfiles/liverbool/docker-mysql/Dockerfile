FROM ubuntu:trusty

MAINTAINER  Liverbool "nukboon@gmail.com"

# Install packages
ENV DEBIAN_FRONTEND noninteractive

RUN locale-gen en_US.UTF-8
RUN export LANG=en_US.UTF-8
RUN export LC_ALL=en_US.UTF-8

RUN echo 'Asia/Bangkok' | sudo tee /etc/timezone

RUN apt-get update && \
  apt-get -yq install mysql-server-5.6 pwgen && \
  rm -rf /var/lib/apt/lists/*

# Remove pre-installed database
RUN rm -rf /var/lib/mysql/*

# Remove syslog configuration
RUN rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf

RUN mkdir -p /var/log/mysql
RUN echo "" >> /var/log/mysql/error.log

# Add MySQL configuration
ADD my.cnf /etc/mysql/conf.d/my.cnf
ADD mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf

# Add MySQL scripts
ADD import_sql.sh /import_sql.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh

# Exposed ENV
ENV MYSQL_USER admin
ENV MYSQL_PASS **Random**

# Replication ENV
ENV REPLICATION_MASTER **False**
ENV REPLICATION_SLAVE **False**
ENV REPLICATION_USER replica
ENV REPLICATION_PASS replica

# Add VOLUMEs to allow backup of config and databases
VOLUME  ["/etc/mysql", "/var/lib/mysql"]

EXPOSE 3306
CMD ["/run.sh"]
