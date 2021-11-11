FROM centos:centos7

MAINTAINER Axel Napolitano <docker.2015@skjt.de>

RUN yum -y install wget
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jre-8u51-linux-x64.rpm
RUN echo "0f200e6ca52ef4f52f3c7b0f1e55ebe3 jre-8u51-linux-x64.rpm" >> MD5SUM
RUN md5sum -c MD5SUM
RUN rpm -Uvh jre-8u51-linux-x64.rpm
RUN yum -y remove wget
RUN rm -f jre-8u51-linux-x64.rpm
RUN rm -f MD5SUM