FROM ubuntu:latest
MAINTAINER kiyopon.onopon@gmail.com

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update

### SOME Utils ###
RUN apt-get install -q -y git debconf-utils curl wget aptitude zip unzip

### Sudo ###
RUN aptitude install sudo

### MYSQL ###
# mysql install(root_assword is "root")
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections
RUN apt-get install -y mysql-server

# char set utf8
RUN sed -i -e "$ a [mysqld]" /etc/mysql/my.cnf
RUN sed -i -e "$ a character-set-server = utf8" /etc/mysql/my.cnf
RUN sed -i -e "$ a [client]" /etc/mysql/my.cnf
RUN sed -i -e "$ a default-character-set = utf8" /etc/mysql/my.cnf
RUN sed -i -e "$ a [mysqldump]" /etc/mysql/my.cnf
RUN sed -i -e "$ a default-character-set = utf8" /etc/mysql/my.cnf
RUN sed -i -e "$ a [mysql]" /etc/mysql/my.cnf
RUN sed -i -e "$ a default-character-set = utf8" /etc/mysql/my.cnf

### PHP ###
RUN apt-get install -q -y php php-mysql php-xml php-cli php-gd php-intl php-mbstring php-curl

### Composer ###
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

### PHPunit ###
RUN wget https://phar.phpunit.de/phpunit.phar
RUN chmod +x phpunit.phar
RUN mv phpunit.phar /usr/local/bin/phpunit

### Create User ###
RUN useradd testuser

CMD /bin/sh
