#FROM phusion/baseimage
FROM centos:7

EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600/udp

#RUN apt-get update && apt-get install wget zip unzip && \
#  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN yum -y install wget unzip && \
    yum clean all && \
    rm -rf /var/cache/yum/ 


RUN wget https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_linux_amd64.zip -O /tmp/consul.zip \
 && unzip /tmp/consul.zip \
 && rm /tmp/consul.zip \
 && mv /consul /usr/bin/consul \
 && mkdir /dist && cd /dist \
 && wget https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_web_ui.zip -O /tmp/consul_webui.zip \
 && unzip /tmp/consul_webui.zip \
 && mv /dist /webui \
 && rm /tmp/consul_webui.zip \ 
 && mkdir /config \ 
 && mkdir /data 

CMD /usr/bin/consul agent -config-dir /config -data-dir /data
