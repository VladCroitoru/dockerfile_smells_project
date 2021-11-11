FROM centos:latest

MAINTAINER pesia

RUN yum -y update && \
    yum clean all && \
    yum -y groupinstall 'Development Tools' && \
    yum -y install java-1.8.0-openjdk-devel && \
    yum -y install git

# install wkr https://github.com/wg/wrk/wiki/Installing-Wrk-on-Linux
RUN yum -y install openssl-devel && \
    cd /tmp/ && \
    git clone https://github.com/wg/wrk.git && \
    cd wrk && \
    make && \
    mv /tmp/wrk/wrk /usr/local/bin/ && \
    cd /tmp/ && \
    rm -fr wrk

