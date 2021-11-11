FROM       centos:7
MAINTAINER Yosuke Yamamoto "yosuke@pyrites.jp"

## Required Packages Install
RUN yum update -y && \
    yum install java-1.8.0-openjdk -y && \
    yum clean all

RUN curl -s https://s3.amazonaws.com/jruby.org/downloads/9.1.6.0/jruby-bin-9.1.6.0.tar.gz | tar -xz -C /opt/ && \
    ln -s /opt/jruby-9.1.6.0 /opt/jruby

ENV JAVA_HOME /usr
ENV PATH /opt/jruby/bin:${PATH}

