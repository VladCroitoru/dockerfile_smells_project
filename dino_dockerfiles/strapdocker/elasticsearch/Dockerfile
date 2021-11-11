FROM strapdocker/java:latest

RUN echo '#!/bin/sh' "\nexit 0" >  /usr/sbin/policy-rc.d
RUN apt-get -qq -y update
RUN apt-get -qq -y upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl
RUN curl http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb http://packages.elasticsearch.org/elasticsearch/1.0/debian stable main" >> /etc/apt/sources.list
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -y elasticsearch

EXPOSE 9200 9300

RUN mkdir /etc/service/elasticsearch
ADD run.sh /etc/service/elasticsearch/run
RUN chmod 755 /etc/service/elasticsearch/run

CMD ["/sbin/my_init"]