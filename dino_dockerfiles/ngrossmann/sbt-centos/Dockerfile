FROM centos:7.1.1503

MAINTAINER "Niklas Grossmann" <ngrossmann@gmx.net>

RUN yum install -y java-1.8.0-openjdk-devel.x86_64 tar git bzip2 rpm-build

RUN yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

RUN yum install -y npm

RUN npm install -g grunt-cli

RUN curl  -sLo /tmp/sbt.tar.gz 'https://dl.bintray.com/sbt/native-packages/sbt/0.13.8/sbt-0.13.8.tgz'

RUN tar xzf /tmp/sbt.tar.gz -C /opt && rm /tmp/sbt.tar.gz

RUN ln -s /opt/sbt/bin/sbt /usr/bin/

