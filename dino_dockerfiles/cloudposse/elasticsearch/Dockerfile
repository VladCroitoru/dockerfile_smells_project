FROM ubuntu:14.04

ENV ELASTICSEARCH_VERSION 2.2.0

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle


RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    locale-gen en_US en_US.UTF-8 && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    wget -O - https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ELASTICSEARCH_VERSION/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz | tar xz && \
    mv elasticsearch-* /elasticsearch

#RUN useradd -c "ElasticSearch" -d /elasticsearch -m elasticsearch

VOLUME ["/vol"]

WORKDIR /elasticsearch

ADD config/ /elasticsearch/config/

EXPOSE 9200
EXPOSE 9300
ENTRYPOINT ["/elasticsearch/bin/elasticsearch"]

