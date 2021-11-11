FROM centos:6.7
MAINTAINER Jimmy The Dog <jimmythedog@kgibbs.co.uk>

WORKDIR /opt

RUN yum install -y tar

RUN curl --insecure --junk-session-cookies --location --remote-name --silent \
  --header "Cookie: oraclelicense=accept-securebackup-cookie" \
  http://download.oracle.com/otn-pub/java/jdk/8u72-b15/jdk-8u72-linux-x64.tar.gz

RUN tar -xvf jdk-8u72-linux-x64.tar.gz
RUN rm jdk-8u72-linux-x64.tar.gz
RUN ln -s jdk1.8.0_72 java

ENV JAVA_HOME /opt/java
ENV PATH $PATH:$JAVA_HOME/bin
