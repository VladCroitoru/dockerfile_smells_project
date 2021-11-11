FROM centos:7
MAINTAINER Arturo Volpe <arturovolpe@gmail.com>

ENV PYTHON_VERSION 3.6.2

RUN yum update -y &&\
    yum install yum-utils curl make -y &&\
    yum-builddep python -y &&\
    yum clean all

RUN curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz &&\
    tar xf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure && \
    make && \
    make install &&\
    cd .. &&\
    rm -rf Python*

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" &&\
    python get-pip.py


RUN yum update -y &&\
    yum install rpm-build -y &&\
    yum install python-devel -y &&\
    yum clean all

RUN python --version && pip --version
