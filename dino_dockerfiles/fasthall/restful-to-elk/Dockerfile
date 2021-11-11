FROM ubuntu:14.04
MAINTAINER Wei-Tsung Lin <fasthall@gmail.com>

RUN apt-get update
RUN apt-get install -y tar wget curl

# Install Oracle JDK
RUN curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k "http://download.oracle.com/otn-pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.tar.gz" && \
    tar zxvf jdk-8u73-linux-x64.tar.gz && \
    mkdir /usr/local/java/ && \
    mv jdk1.8.0_73/ /usr/local/java && \
    rm jdk-8u73-linux-x64.tar.gz
ENV JAVA_HOME /usr/local/java/jdk1.8.0_73
ENV PATH $PATH:$JAVA_HOME/bin

WORKDIR /opt
# Download Elasticsearch
RUN wget https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.2.0/elasticsearch-2.2.0.tar.gz
RUN tar zxvf elasticsearch-2.2.0.tar.gz
RUN rm elasticsearch-2.2.0.tar.gz

# Download Logstash
RUN wget https://download.elastic.co/logstash/logstash/logstash-2.2.2.tar.gz
RUN tar zxvf logstash-2.2.2.tar.gz
RUN rm logstash-2.2.2.tar.gz

# Download Kibana
RUN wget https://download.elastic.co/kibana/kibana/kibana-4.4.1-linux-x64.tar.gz
RUN tar zxvf kibana-4.4.1-linux-x64.tar.gz
RUN rm kibana-4.4.1-linux-x64.tar.gz

ADD http_poller.conf /opt/http_poller.conf
ADD entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

# Kibana
EXPOSE 5601
# Elasticsearch
EXPOSE 9200 

ENTRYPOINT ["/opt/entrypoint.sh"]