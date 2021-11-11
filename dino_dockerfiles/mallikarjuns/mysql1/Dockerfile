FROM ubuntu:16.04
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections
RUN apt-get update
RUN apt-get install -y mysql-server
EXPOSE 3306
CMD bash
