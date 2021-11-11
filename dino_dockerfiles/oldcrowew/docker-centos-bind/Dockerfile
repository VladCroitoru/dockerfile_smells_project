FROM centos:latest
MAINTAINER John Favorite <john.favorite@gmail.com>

RUN yum update -y \
 && yum install -y bind bind-utils openssl \
 && yum clean all \
 && yum clean metadata

EXPOSE 53/udp
VOLUME ["/data"]
CMD ["/usr/sbin/named"]