FROM centos:7

MAINTAINER Janne Pellikka

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING UTF-8

RUN yum update -y && yum install -y \
    which \
    git \
    tar \
    wget \
    sqlite-devel \
    epel-release && \
  yum group install -y "Development Tools" && \
  yum install -y \
    openssl-devel && \
  yum clean all

RUN wget http://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz \
&& xz -d Python-3.5.2.tar.xz \
&& tar -xvf Python-3.5.2.tar

WORKDIR Python-3.5.2
RUN ./configure --prefix=/usr/local \
&& make && make altinstall
WORKDIR /
RUN rm -rf Python-3.5.2; rm Python-3.5.2.tar

RUN useradd -ms /bin/bash foobar
USER foobar
