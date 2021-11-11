FROM ubuntu:14.04

MAINTAINER Rocco Bruyn <rocco.bruyn@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install packages
# Allow all interfaces
# Remove apt cache
# Remove pre-installed database
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        nano \
        libaio1 \
        libaio-dev \
        mysql-server && \
    sed -ri "s/bind-address\s+= 127.0.0.1/bind-address = 0.0.0.0/" \
        /etc/mysql/my.cnf && \
    sed -ri "s/key_buffer\s/key_buffer_size /" \
        /etc/mysql/my.cnf && \
    rm -rf /var/lib/mysql/* && \
    rm -rf /var/lib/apt/lists/*

# Add charset configuration for mysql
ADD mysqld_charset.cnf /etc/mysql/conf.d/mysql_charset.cnf

# Mount volume for data
VOLUME /var/lib/mysql
RUN chmod 0755 -R /var/lib/mysql

# Add init file that sets root password
ADD init.sql /tmp/init-mysql.sql

# Add script that starts the server
ADD run.sh /bin/run.sh
RUN chmod +x /bin/run.sh

# Expose port 3306 for database traffic
EXPOSE 3306

# Execute script to start mysql server
CMD ["run.sh"]
