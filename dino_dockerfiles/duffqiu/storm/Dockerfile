FROM duffqiu/dockerjdk7:latest
MAINTAINER duffqiu@gmail.com

RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7
RUN yum -y  update
RUN yum install -y wget tar

RUN wget --no-cookies --no-check-certificate http://www.us.apache.org/dist/storm/apache-storm-0.9.4/apache-storm-0.9.4.tar.gz
RUN tar zxf apache-storm-0.9.4.tar.gz
RUN mv apache-storm-0.9.4 storm

ADD start-nb /storm/start-nb

RUN chmod +x /storm/start-nb

EXPOSE 6627

EXPOSE 3772 3773

WORKDIR storm

ENTRYPOINT [ "/storm/start-nb" ]

