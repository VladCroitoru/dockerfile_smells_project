FROM centos:7

LABEL maintainer="jgilstrap@gmail.com"

RUN yum -y update && \
    yum -y install wget vim && \
    wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" \
http://download.oracle.com/otn-pub/java/jdk/9+181/jdk-9_linux-x64_bin.rpm \
-O jdk-9_linux-x64_bin.rpm && \
    rpm -ivh jdk-9_linux-x64_bin.rpm

ENV JAVA_HOME /usr/java/jdk-9/
ENV PATH "$PATH:$JAVA_HOME/bin"

RUN useradd -ms /bin/bash javauser
USER javauser
WORKDIR /home/javauser

ADD startup.jsh /home/javauser

CMD jshell --start startup.jsh
