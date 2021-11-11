FROM ubuntu:18.04

# disable interactive apt-get
ENV DEBIAN_FRONTEND=noninteractive

# install and configure required packages
RUN apt-get update && \
        apt-get install -y \
	tzdata \
        nano \
        wget \
        curl \
        ruby \
        rubygems-integration \
        ruby-dev \
        libmysqlclient-dev \
        build-essential \
        git \
        curl \
        sudo

# set locale to en_US.utf8 since it is required by bundle
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# install rake and bundler
RUN gem install rake bundler foreman mysql2

# checkout huginn, open folder and install dependencies
RUN git clone https://github.com/huginn/huginn.git && \
	cd huginn && \ 
	cp .env.example .env && \
	bundle

# install and configure db
RUN echo "mysql-server mysql-server/root_password password " | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password " | debconf-set-selections

RUN apt-get update && \
	apt-get -y install mysql-server-5.7 && \
	mkdir -p /var/lib/mysql && \
	mkdir -p /var/run/mysqld && \
	mkdir -p /var/log/mysql && \
	chown -R mysql:mysql /var/lib/mysql && \
	chown -R mysql:mysql /var/run/mysqld && \
	chown -R mysql:mysql /var/log/mysql

# UTF-8 and bind-address
RUN sed -i -e "$ a [client]\n\n[mysql]\n\n[mysqld]"  /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[client\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[mysql\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[mysqld\]\)/\1\ninit_connect='SET NAMES utf8'\ncharacter-set-server = utf8\ncollation-server=utf8_unicode_ci\nbind-address = 0.0.0.0/g" /etc/mysql/my.cnf

# for some reason a writable volume is required for databases
VOLUME /var/lib/mysql

# enable sudo for docker user
RUN echo "docker ALL=NOPASSWD: ALL" >> /etc/sudoers

# copy db initilisation script
COPY init-db.sh /usr/sbin/
RUN chmod +x /usr/sbin/init-db.sh

# start huginn
COPY start-huginn.sh /usr/sbin/
RUN chmod +x /usr/sbin/start-huginn.sh
CMD ["/usr/sbin/start-huginn.sh"]
