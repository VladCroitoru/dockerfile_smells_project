FROM centos:6
MAINTAINER Jonas Otten <jonadev95@posteo.org>
RUN yum install -y epel-release
RUN yum install -y boost-filesystem boost-thread libmicrohttpd logrotate libcurl boost-regex mongodb mongodb-server
COPY testbed-fi-ware.repo /etc/yum/repos.d/testbed-fi-ware.repo
RUN yum install -y contextBroker
RUN mkdir -p /data/db
EXPOSE 1026
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
