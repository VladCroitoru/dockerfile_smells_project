# Base on latest CentOS image
FROM centos:latest

MAINTAINER “Jon Ervine” <jon.ervine@gmail.com>
ENV container docker

# Install updates and some dev tools
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y znc supervisor; yum clean all; rm -rf /var/cache/yum

ADD start.sh /sbin/start.sh
ADD supervisord.conf /etc/supervisord.conf
ADD znc.ini /etc/supervisord.d/znc.ini
RUN chmod 755 /sbin/start.sh

VOLUME /config

EXPOSE 6667 8080

ENTRYPOINT ["/sbin/start.sh"]
