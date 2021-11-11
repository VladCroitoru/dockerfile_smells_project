FROM centos:centos7

MAINTAINER simon.dietschi@bluecare.ch

RUN rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install mysql-community-server pwgen bash-completion psmisc net-tools; yum clean all

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld_safe"]
