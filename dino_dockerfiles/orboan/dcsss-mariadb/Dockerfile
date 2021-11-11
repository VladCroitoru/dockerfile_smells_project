FROM orboan/dcss-shellinabox
MAINTAINER Oriol Boix Anfosso <dev@orboan.com>

RUN yum -y install --setopt=tsflags=nodocs epel-release

RUN yum -y install --setopt=tsflags=nodocs mariadb-server bind-utils pwgen psmisc hostname

# - Clean YUM caches to minimise Docker image size...
RUN \
  yum clean all && rm -rf /tmp/yum*

# Place VOLUME statement below all changes to /var/lib/mysql
VOLUME /var/lib/mysql

#
#If you do not want to provide a password for the mariadb root
#i.e. to not pass the MYSQL_ROOT_PASSWORD enviroment variable
#at runtime when creating the container, just give some value
#to here. Otherwise, leave it null (default).
ENV MYSQL_ALLOW_EMPTY_PASSWORD=

ENV MYSQL_ROOT_PASSWORD=mariadb

ENV USER=www
ENV PASSWORD=iaw

ADD container-files /

# Fix permissions to allow for running on openshift
COPY fix-permissions.sh ./
RUN chmod +x ./fix-permissions.sh
RUN ./fix-permissions.sh /var/lib/mysql/   && \
    ./fix-permissions.sh /var/log/mariadb/ && \
    ./fix-permissions.sh /var/run/

EXPOSE 3306
