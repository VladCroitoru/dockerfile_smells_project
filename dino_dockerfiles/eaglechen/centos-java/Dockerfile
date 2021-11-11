FROM centos:7
MAINTAINER Eagle Chen <chygr1234@gmail.com>

RUN curl -L -k --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u40-b26/jre-8u40-linux-x64.rpm -o /tmp/jre.rpm && rpm -i /tmp/jre.rpm && rm /tmp/jre.rpm
