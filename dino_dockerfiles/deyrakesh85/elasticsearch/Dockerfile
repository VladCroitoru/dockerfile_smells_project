FROM deyrakesh85/ubuntu:jdk8

MAINTAINER Rakesh Dey <deyrakesh85@gmail.com>

RUN groupadd -r elasticsearch && useradd -r -g elasticsearch -s /bin/bash -m elasticsearch

USER elasticsearch

WORKDIR /home/elasticsearch

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.2.tar.gz

RUN tar -xzf elasticsearch-6.2.2.tar.gz

COPY elasticsearch.yml /home/elasticsearch/elasticsearch-6.2.2/config/

RUN mkdir data

RUN chmod -R 777 data

EXPOSE 9200

EXPOSE 9300

ENTRYPOINT ["/home/elasticsearch/elasticsearch-6.2.2/bin/elasticsearch-plugin", "install", "ingest-geoip"]

ENTRYPOINT ["/home/elasticsearch/elasticsearch-6.2.2/bin/elasticsearch-plugin", "install", "ingest-user-agent"]

ENTRYPOINT ["/home/elasticsearch/elasticsearch-6.2.2/bin/elasticsearch"]
