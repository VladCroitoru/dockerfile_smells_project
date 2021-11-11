FROM centos:centos6

MAINTAINER Clement Laforet

RUN yum install -y wget unzip tar curl

ENV JAVA_UPDATE 72
ENV JAVA_BUILD  14
RUN wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-7u${JAVA_UPDATE}-linux-x64.rpm" -O /opt/jdk-7u${JAVA_UPDATE}-linux-x64.rpm
RUN yum localinstall -y /opt/jdk-7u${JAVA_UPDATE}-linux-x64.rpm
RUN rm -f /opt/jdk-7u${JAVA_UPDATE}-linux-x64.rpm

RUN (curl -0 http://mirror.cc.columbia.edu/pub/software/apache/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz | \
             tar -zx -C /usr/local) && ln -sf /usr/local/apache-maven-3.0.5/bin/mvn /usr/bin/mvn

ENV JAVA_HOME /usr/java/jdk1.7.0_72

VOLUME ["/build"]
WORKDIR /build

RUN yum install -y http://repos.mesosphere.io/el/6/noarch/RPMS/mesosphere-el-repo-6-2.noarch.rpm
RUN yum -y install mesos

CMD ["./build.sh"]


