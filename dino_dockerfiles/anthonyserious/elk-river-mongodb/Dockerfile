FROM ubuntu:14.04
MAINTAINER Anthony Schneider <anthonyserious@gmail.com>
RUN apt-get update && apt-get install -y curl && apt-get install -y openjdk-7-jdk

RUN mkdir /local

VOLUME /data
VOLUME /logs

# MongoDB
RUN cd /local \
  && curl -O 'https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.6.5.tgz' \
  && tar xpzf mongodb-linux-x86_64-2.6.5.tgz \
  && rm -f mongodb-linux-x86_64-2.6.5.tgz

# ElasticSearch
RUN cd /local \
  && curl -O https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.0.tar.gz \
  && tar xpzf elasticsearch-1.4.0.tar.gz \
  && rm -f elasticsearch-1.4.0.tar.gz

# River MongoDB plugin
RUN cd /local/elasticsearch-1.4.0 \
  && ./bin/plugin --install com.github.richardwilly98.elasticsearch/elasticsearch-river-mongodb/2.0.4

# Kibana
RUN cd /local \
  && curl -O 'https://download.elasticsearch.org/kibana/kibana/kibana-4.0.0-BETA2.tar.gz' \ 
  && tar xpzf kibana-4.0.0-BETA2.tar.gz \
  && rm -f kibana-4.0.0-BETA2.tar.gz

ADD mongod.conf /local/mongodb-linux-x86_64-2.6.5/mongod.conf
ADD elasticsearch.yml /local/elasticsearch-1.4.0/config/elasticsearch.yml
ADD entrypoint.sh /entrypoint.sh

EXPOSE 5601 9200 27017
ENTRYPOINT /entrypoint.sh

