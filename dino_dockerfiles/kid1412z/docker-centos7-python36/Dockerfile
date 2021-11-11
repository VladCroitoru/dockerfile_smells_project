FROM centos:7
MAINTAINER kid1412z <zuoqy.gk@gmail.com>

ENV PYTHON_VERSION "3.6.0" 

ADD Centos-7.repo /etc/yum.repos.d/CentOS-Base.repo
ADD epel-7.repo /etc/yum.repos.d/epel.repo
RUN mkdir /root/.pip
ADD pip.conf /root/.pip

RUN yum clean all && \
    yum -y update && \
    yum -y install zlib-dev openssl-devel sqlite-devel bzip2-devel

RUN yum -y install curl wget tar bzip2 unzip yum-utils hostname net-tools && \
    yum -y install gcc gcc-c++ git make automake cmake patch logrotate  && \
    yum -y install libpng-devel libjpeg-devel && \
    yum clean all


RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar xvf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall && \
    cd / && \
    rm -rf Python-${PYTHON_VERSION}*

RUN cd /usr/local/bin && \
    ln -s easy_install-3.6 easy_install && \
    ln -s pip3.6 pip && \
    ln -s pydoc3.6 pydoc && \
    ln -s python3.6 python && \
    ln -s python-config3.6 python-config

ENV PATH "/usr/local/bin:${PATH}"


