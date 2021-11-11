FROM centos:7.3.1611
MAINTAINER tpham

USER root

RUN yum -y clean all && \
    yum -y update && \
    yum -y install epel-release && \
    yum install -y python-pip gcc python-devel openssl-devel && \
    pip install satori-rtm-sdk && \
    pip install backports.ssl==0.0.9 && \
    easy_install pyOpenSSL==0.15 || true && \
    pip install --upgrade PyOpenSSL || true

COPY test/test_satori.py /tmp/test_satori.py

WORKDIR /tmp
