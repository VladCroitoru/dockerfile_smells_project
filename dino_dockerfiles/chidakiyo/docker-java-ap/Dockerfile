#
# VERSION 0.0.1
#

FROM centos:centos6
MAINTAINER chidakiyo "chidakiyo@gmail.com"

# Setup
RUN rpm -ivh http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN yum -y update

# Java7
RUN yum -y install java-1.7.0-openjdk-devel

# Tomcat
RUN yum -y install tomcat
RUN chkconfig tomcat on

EXPOSE 8080

CMD /etc/init.d/tomcat start && tail -f /dev/null
