FROM ubuntu:latest

# Include our scripts
ADD ./scripts /mysql-sakila

# Tell debconf to use the noninteractive frontend
ENV DEBIAN_FRONTEND noninteractive

# Tell debconf that the default MySQL root password should be "sakila"
RUN echo 'mysql-server mysql-server/root_password password sakila' | debconf-set-selections
RUN echo 'mysql-server mysql-server/root_password_again password sakila' | debconf-set-selections

# Install MySQL
RUN apt-get update && apt-get -y install mysql-server

# Start MySQL and run our scripts
RUN service mysql restart \
  && mysql --user=root --password=sakila < /mysql-sakila/init.sql \
  && mysql --user=root --password=sakila < /mysql-sakila/sakila-schema.sql \
  && mysql --user=root --password=sakila < /mysql-sakila/sakila-data.sql

EXPOSE 3306

ENTRYPOINT mysqld_safe --bind-address=0.0.0.0
