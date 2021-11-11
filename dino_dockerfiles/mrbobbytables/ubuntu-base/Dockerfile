################################################################################
# ubuntu-base:1.1.0
# Date: 1/11/2016
# 
# Description:
# Base Ubuntu build with logstash forwarder, supervisor, and various
# helper scripts.
################################################################################

FROM ubuntu:14.04
MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables


ENV DEBIAN_FRONTEND=noninteractive  \
    VERSION_CONSUL_TEMPLATE=0.12.2  \
    VERSION_ENVCONSUL=0.6.0

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D88E42B4                                                                \
 && echo "deb http://packages.elastic.co/logstashforwarder/debian stable main" >> /etc/apt/sources.list.d/logstash-forwarder.list    \
 && apt-get -y update    \
 && apt-get -y install   \
     logstash-forwarder  \
     supervisor          \
     unzip               \
     wget                \
 && wget -O /tmp/consul-template.zip  \
    https://releases.hashicorp.com/consul-template/${VERSION_CONSUL_TEMPLATE}/consul-template_${VERSION_CONSUL_TEMPLATE}_linux_amd64.zip  \
 && wget -O /tmp/envconsul.zip  \
    https://releases.hashicorp.com/envconsul/${VERSION_ENVCONSUL}/envconsul_${VERSION_ENVCONSUL}_linux_amd64.zip  \
 && unzip /tmp/consul-template.zip -d /usr/local/bin  \
 && unzip /tmp/envconsul.zip -d /usr/local/bin        \
 && mkdir -p /etc/consul/template/conf.d              \
 && mkdir -p /etc/consul/template/templates           \
 && mkdir -p /etc/consul/envconsul/conf.d             \
 && mkdir -p /var/log/consul-template  \
 && mkdir -p /var/log/keepalived       \
 && mkdir -p /var/log/nslcd            \
 && apt-get clean              \
 && rm -rf /etc/rsyslog.d/*    \
 && rm -rf /etc/logrotate.d/*  \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./skel /

RUN chmod 640 /etc/logrotate.conf                       \
 && chmod 640 /etc/logrotate.d/*                        \
 && chmod +x /opt/scripts/container_functions.lib.sh    \
 && chmod +x /opt/scripts/logrotate.sh                  \
 && chmod +x /opt/scripts/redpill.sh                    \
 && chown -R logstash-forwarder:logstash-forwarder /opt/logstash-forwarder
