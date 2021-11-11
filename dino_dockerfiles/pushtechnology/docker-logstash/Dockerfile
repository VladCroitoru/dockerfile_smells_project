# Download and install logstash, and insert our custom modules

FROM debian:stretch
MAINTAINER Push Technology "cloudops@pushtechnology.com"

# Install Deps and Download logstash
RUN apt-get update && apt-get install -y wget openjdk-8-jre m4
RUN wget https://artifacts.elastic.co/downloads/logstash/logstash-5.5.2.tar.gz -O /tmp/logstash.tar.gz 2> /dev/null

# Unzip logstash and put in place
RUN tar zxf /tmp/logstash.tar.gz -C /opt && mv /opt/logstash-5.5.2 /opt/logstash && rm -rf /tmp/logstash.tar.gz

# Install Plugins
RUN /opt/logstash/bin/logstash-plugin install x-pack
