FROM ubuntu

# Adapted from: https://index.docker.io/u/toby/mysql/

# Install MySQL
RUN apt-get update
RUN apt-get install -y mysql-server
RUN apt-get clean

# Listen on all interfaces
RUN sed -i -e 's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf

# Allow root from non localhost IPs
RUN /usr/sbin/mysqld & sleep 10s && mysql --host=127.0.0.1 --user=root -e "CREATE DATABASE development_db; GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'; FLUSH PRIVILEGES;"

EXPOSE 3306

ENTRYPOINT ["/usr/sbin/mysqld"]