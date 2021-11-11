FROM oraclelinux
MAINTAINER Toby Ferguson <toby@cloudera.com>
RUN  yum -y update; yum clean all
RUN yum -y install wget;yum clean all
ENV JDK_VERSION 7.8
RUN wget -nv --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/7u80-b15/jdk-7u80-linux-x64.rpm
RUN yum -y localinstall jdk-7u80-linux-x64.rpm; yum clean all
ENV DIRECTOR_VERSION 2.3
RUN wget -nv -O /etc/yum.repos.d/cloudera-director.repo http://archive.cloudera.com/director/redhat/7/x86_64/director/cloudera-director.repo
RUN yum -y install cloudera-director-client
ENTRYPOINT [ "/usr/bin/cloudera-director" ]
