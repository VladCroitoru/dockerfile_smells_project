FROM ubuntu:trusty
MAINTAINER Viacheslav Pryimak <vpryimak@intropro.com"

################## BEGIN INSTALLATION ######################
RUN apt-get update && \
  apt-get -y upgrade && \
  apt-get -y install wget libssl1.0.0 python openjdk-7-jre nload && \
  wget -q https://download.elastic.co/logstash-forwarder/binaries/logstash-forwarder_0.4.0_amd64.deb -O logstash-forwarder.deb && \
  dpkg -i logstash-forwarder.deb && \
  rm logstash-forwarder.deb && rm /etc/logstash-forwarder.conf && mkdir /etc/logstash-forwarder

RUN mkdir -p /etc/logstash/ssl
ADD ./ssl    /etc/logstash/ssl
ADD ./src    /
ADD ./conf   /etc/logstash-forwarder
RUN chmod +x /usr/local/sbin/start.sh
##################### INSTALLATION END #####################

ENTRYPOINT ["/usr/local/sbin/start.sh"]

