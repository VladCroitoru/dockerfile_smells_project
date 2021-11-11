# Download and install elasticsearch

FROM debian:stretch
MAINTAINER Push Technology "cloudops@pushtechnology.com"

# Install deps and download elasticsearch
RUN apt-get update && apt-get install -y wget openjdk-8-jre m4
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.2.tar.gz -O /tmp/elasticsearch.tar.gz 2> /dev/null

# Unzip elasticsearch and put in place
RUN tar zxf /tmp/elasticsearch.tar.gz -C /opt && mv /opt/elasticsearch-5.5.2 /opt/elasticsearch && rm -rf /tmp/elasticsearch.tar.gz

# Install the AWS plugin and X-Pack
RUN /opt/elasticsearch/bin/elasticsearch-plugin install repository-s3
RUN /opt/elasticsearch/bin/elasticsearch-plugin install discovery-ec2
RUN /opt/elasticsearch/bin/elasticsearch-plugin install x-pack
