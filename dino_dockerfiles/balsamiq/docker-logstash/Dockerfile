# BUILD: docker build -t balsamiq/docker-logstash .
# RUN: docker run -i -t -v /var/log:/host/var/log -e CLUSTER_NAME=docker -e LOGSTASH_OPTS=--verbose balsamiq/docker-logstash
FROM ubuntu:trusty
MAINTAINER Luis Arias <luis@balsamiq.com>

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install wget unzip

# Install logstash
RUN wget -O- http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb http://packages.elasticsearch.org/logstash/1.4/debian stable main" > /etc/apt/sources.list.d/logstash.list
RUN apt-get update && apt-get -y install logstash=1.4.2-1-2c0f5a1

# Install elasticsearch ec2 discovery plugin
RUN mkdir -p /opt/logstash/plugins/cloud-aws
WORKDIR /opt/logstash/plugins/cloud-aws
RUN wget http://download.elasticsearch.org/elasticsearch/elasticsearch-cloud-aws/elasticsearch-cloud-aws-2.1.1.zip && unzip elasticsearch-cloud-aws-2.1.1.zip && rm elasticsearch-cloud-aws-2.1.1.zip

# Install elasticsearch config
WORKDIR /opt/logstash
RUN ln -s /etc/elasticsearch/elasticsearch.yml

ADD run /opt/logstash/run
RUN chmod +x run

ADD config/etc /etc

ENV ES_CLUSTER_NAME elasticsearch
ENV ES_AWS_REGION us-east-1
VOLUME ["/host/var/log"]

EXPOSE 9200 9300

CMD ./run
