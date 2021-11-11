FROM centos:7
MAINTAINER samuraitaiga

WORKDIR /root

RUN yum clean all && \
    yum install -y wget unzip dnsmasq && \
    wget https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip && \
    wget https://dl.bintray.com/mitchellh/consul/0.5.0_web_ui.zip && \
    unzip 0.5.0_linux_amd64.zip && \
    unzip 0.5.0_web_ui.zip && \
    chmod 755 consul && \
    cp consul /usr/local/bin && \
    mv dist /opt/ && \
    rm -rf ./*
