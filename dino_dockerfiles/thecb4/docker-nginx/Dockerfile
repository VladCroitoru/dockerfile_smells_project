FROM centos:centos7
MAINTAINER Tomas Kral <tomas.kral@gmail.com>

RUN yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs install epel-release && \
    yum -y --setopt=tsflags=nodocs install nginx && \
    yum clean all


ADD nginx.conf /etc/nginx/nginx.conf

#  for some reason nginx is still trying to create /var/log/nginx/error.log
#  even if error_log /dev/stderr is set
RUN chmod -R go+rwx /var/log/nginx


EXPOSE 8080
RUN chmod -R go+rwx /var/lib/nginx

USER 997

ENTRYPOINT [ "/usr/sbin/nginx" ]
