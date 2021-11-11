# LogicalDOC Document Management System Community Edition ( https://www.logicaldoc.com )
FROM phusion/baseimage
MAINTAINER "Alessandro Gasparini" <devel@logicaldoc.com>

ENV LDOC_VERSION="7.7.3"
ENV LDOC_MEMORY="2000"
ENV SSH_PSWD="logicaldoc"
ENV MYSQL_VERSION="5.7"
ENV MYSQL_DATADIR="/var/lib/mysql"
ENV DEBIAN_FRONTEND="noninteractive"
ENV CATALINA_HOME="/opt/logicaldoc/tomcat"
ENV JAVA_HOME="/usr/lib/jvm/java-8-oracle/"
ENV KILL_PROCESS_TIMEOUT=100
ENV KILL_ALL_PROCESSES_TIMEOUT=100

# Prepare system for mysql installation
RUN groupadd -r mysql && useradd -r -g mysql mysql
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y perl pwgen --no-install-recommends 

# Install mysql
RUN apt-get install -y mysql-server-${MYSQL_VERSION} \
    && rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql

RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \
    && echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
    && mv /tmp/my.cnf /etc/mysql/my.cnf

RUN mkdir /var/run/mysqld && \
    chown mysql /var/run/mysqld


# Prepare system for java installation
RUN apt-get -y install software-properties-common python-software-properties

# Install oracle java
RUN \
  echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer

# Some required software for LogicalDOC plugins
RUN apt-get -y install \ 
    imagemagick \
    ghostscript \
    curl \
    unzip \
    sudo \
    tar 

# Download and unzip logicaldoc installer 
RUN mkdir /opt/logicaldoc
RUN curl -L https://sourceforge.net/projects/logicaldoc/files/distribution/LogicalDOC%20CE%207.7/logicaldoc-community-installer-${LDOC_VERSION}.zip/download \
    -o /opt/logicaldoc/logicaldoc-installer-${LDOC_VERSION}.zip  && \
    unzip /opt/logicaldoc/logicaldoc-installer-${LDOC_VERSION}.zip -d /opt/logicaldoc && \
    rm /opt/logicaldoc/logicaldoc-installer-${LDOC_VERSION}.zip

# Add configuration scripts
ADD 01_mysql.sh /etc/my_init.d/
ADD 02_logicaldoc.sh /etc/my_init.d/
ADD wait-for-it.sh /opt/logicaldoc
ADD auto-install.xml /opt/logicaldoc
RUN chmod +x /etc/my_init.d/* && \
chmod +x /opt/logicaldoc/wait-for-it.sh

# mysql service setup
RUN mkdir /etc/service/mysqld/
ADD mysqld.sh /etc/service/mysqld/run
RUN chmod +x /etc/service/mysqld/run

# logicaldoc service setup
RUN mkdir /etc/service/logicaldoc/
ADD logicaldoc.sh /etc/service/logicaldoc/run
RUN chmod +x /etc/service/logicaldoc/run

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Enable SSH
RUN rm -f /etc/service/sshd/down

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Setup the logicaldoc password
RUN useradd logicaldoc && \
echo "logicaldoc:${SSH_PSWD}" | chpasswd && \
echo "logicaldoc  ALL=(ALL:ALL) ALL" >> /etc/sudoers 

# Volumes for persistent storage
VOLUME /var/lib/mysql
VOLUME /opt/logicaldoc/conf
VOLUME /opt/logicaldoc/repository

# Ports to connect to
EXPOSE 8080 22

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

