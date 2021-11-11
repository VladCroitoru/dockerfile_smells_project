# Elasticsearch server

FROM ubuntu:12.04

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update -qq
RUN apt-get upgrade -y

RUN apt-get install -y wget

RUN apt-get install -y python-software-properties
RUN add-apt-repository ppa:webupd8team/java -y

RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN apt-get install -y git curl oracle-java7-installer

RUN wget -O /tmp/elasticsearch.tar.gz https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.10.tar.gz
RUN cd /tmp && tar xzf /tmp/elasticsearch.tar.gz
RUN rm -rf /tmp/elasticsearch.tar.gz
RUN mv /tmp/elasticsearch-0.90.10 /elasticsearch

WORKDIR /elasticsearch

VOLUME /elasticsearch

EXPOSE 9200

CMD ./bin/elasticsearch -f