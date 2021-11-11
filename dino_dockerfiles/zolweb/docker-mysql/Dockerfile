FROM cedvan/ubuntu:14.04.20150206
MAINTAINER dev@cedvan.com

# Install MySQL
RUN apt-get update \
 && apt-get install -y mysql-server-5.6 \
 && rm -rf /var/lib/mysql/mysql

# Delete useless list packages
RUN rm -rf /var/lib/apt/lists/*

ADD assets/start /start
RUN chmod 755 /start

EXPOSE 3306

VOLUME ["/var/lib/mysql"]
VOLUME ["/run/mysqld"]

CMD ["/start"]