FROM ubuntu:14.04
ENV MYSQL_MANAGER_VERSION 1.0.7

RUN apt-get update && \
    apt-get -y install ruby ruby-dev libdbi-ruby ruby-dbd-mysql libmysqlclient-dev make rsync && \
    gem install mysql_manager --version=${MYSQL_MANAGER_VERSION} && \
    apt-get -y remove make ruby-dev && \
    apt-get clean

ENTRYPOINT [ "/usr/local/bin/mysql-manager" ]
