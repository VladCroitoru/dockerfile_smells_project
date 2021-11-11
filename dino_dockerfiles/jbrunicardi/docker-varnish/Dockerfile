FROM million12/centos-supervisor:latest
MAINTAINER jbrunicardi@gmail.com

RUN yum update -y && \
  yum install -y epel-release && \
  yum install -y varnish && \
  yum install -y libmhash-devel && \
  yum install -y vixie-cron crontabs && \  
  curl -LO https://download.elastic.co/beats/filebeat/filebeat-1.2.3-x86_64.rpm && \
  yum localinstall -y filebeat-1.2.3-x86_64.rpm && \
  rm -f filebeat-1.2.3-x86_64.rpm && \
  yum clean all

ENV VCL_CONFIG      /etc/varnish/default.vcl
ENV CACHE_SIZE      64m
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600
ENV LOGSTASH_HOST   127.0.0.1:5044

ADD container-files /

EXPOSE 80
