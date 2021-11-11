FROM centos:latest
MAINTAINER duffqiu@gmail.com

RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7
RUN yum -y  update
RUN yum install -y wget curl

RUN curl  -L -O -k https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64

RUN mv confd-0.10.0-linux-amd64 /usr/bin/confd

RUN chmod +x /usr/bin/confd

VOLUME /etc/confd/conf.d/

VOLUME /etc/confd/templates/

VOLUME /workspace/

WORKDIR /workspace/

ENTRYPOINT [ "/usr/bin/confd" ]

