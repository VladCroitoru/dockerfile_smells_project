#
# VERSION 0.0.1
#

FROM centos:centos6
MAINTAINER chidakiyo "chidakiyo@gmail.com"

# epel
RUN rpm -ivh http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm

# update
RUN yum -y update

# td-agent
ADD GPG-KEY-td-agent /tmp/GPG-KEY-td-agent
RUN rpm --import /tmp/GPG-KEY-td-agent
ADD td.repo /etc/yum.repos.d/td.repo
RUN yum -y install td-agent
RUN sed -i 's/ulimit/# ulimit/' /etc/init.d/td-agent
RUN cat /dev/null > /var/log/td-agent/td-agent.log
RUN chown td-agent. -R /var/log/td-agent/
RUN chkconfig td-agent on

EXPOSE 8888
EXPOSE 24224

