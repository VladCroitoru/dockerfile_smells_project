FROM ubuntu:16.04

RUN apt update -y
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections && \
    echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections && \
    apt-get -y install mysql-server

RUN mkdir -p /var/run/mysqld && chown mysql:mysql /var/run/mysqld

ADD requirements.txt ./
RUN apt-get -y install python3 python3-pip
RUN apt-get install -y libmysqlclient-dev
RUN pip3 install -r requirements.txt
ADD src/main/main.py ./

RUN apt-get -y install wget
RUN wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-category.sql.gz
RUN gunzip jawiki-latest-category.sql.gz
RUN wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-categorylinks.sql.gz
RUN gunzip jawiki-latest-categorylinks.sql.gz
RUN wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-page.sql.gz
RUN gunzip jawiki-latest-page.sql.gz

RUN ls -lat

RUN mkdir -p /opt/
ENV LANG C.UTF-8

CMD /bin/bash /usr/bin/mysqld_safe --skip-grant-tables & \
  sleep 5 && \
  mysql -u root -e "CREATE DATABASE wikipedia default character set utf8" && \
  mysql -u root wikipedia < jawiki-latest-category.sql && \
  mysql -u root wikipedia < jawiki-latest-categorylinks.sql && \
  mysql -u root wikipedia < jawiki-latest-page.sql && \
  python3 main.py && \
  echo "done!"

VOLUME ["/opt/"]
