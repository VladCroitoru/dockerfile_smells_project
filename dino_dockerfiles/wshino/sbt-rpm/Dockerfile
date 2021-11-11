FROM centos:7

MAINTAINER "wshino"

RUN yum install -y java-1.8.0-openjdk-devel.x86_64 tar git bzip2 rpm-build

RUN yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm

RUN curl  -sLo /tmp/sbt.tar.gz 'https://dl.bintray.com/sbt/native-packages/sbt/0.13.8/sbt-0.13.8.tgz'

RUN tar xzf /tmp/sbt.tar.gz -C /opt && rm /tmp/sbt.tar.gz

RUN ln -s /opt/sbt/bin/sbt /usr/bin/

WORKDIR /app
