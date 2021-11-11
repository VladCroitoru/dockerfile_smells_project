#
# Supervisoring Elasticsearch, Logstash and Kibana
#

# Pull base image.
FROM ubuntu:14.04
MAINTAINER WEISONG WANG <wangwscn@hotmail.com>

#Set package envs.
ENV DEBIAN_FRONTEND noninteractive
ENV ES_PKG_NAME elasticsearch-1.5.2
ENV KIB_PKG_NAME kibana-4.0.2-linux-x64
ENV LGS_PKG_NAME logstash-1.5.0

# Install Utilities.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget npm && \
  apt-get install -y nodejs && \
  rm -rf /var/lib/apt/lists/*

#Install Oracle Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

#Install supervisor.
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

# Install ElasticSearch.
RUN \
  cd / && \
  wget https://download.elastic.co/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /elasticsearch

#Install Kibana.
RUN \
  cd / && \
  wget https://download.elastic.co/kibana/kibana/$KIB_PKG_NAME.tar.gz && \
  tar xvzf $KIB_PKG_NAME.tar.gz && \
  rm -f $KIB_PKG_NAME.tar.gz && \
  mv /$KIB_PKG_NAME /kibana

#Install Logstash.
RUN \
  cd / && \
  wget http://download.elastic.co/logstash/logstash/$LGS_PKG_NAME.tar.gz && \
  tar xvzf $LGS_PKG_NAME.tar.gz && \
  rm -f $LGS_PKG_NAME.tar.gz && \
  mv /$LGS_PKG_NAME /logstash

# Define mountable directories.
VOLUME ["/workspace"]

# Mount config.
COPY workspace/supervisord.conf /workspace/supervisord.conf
COPY workspace/elasticsearch.yml /workspace/elasticsearch.yml
COPY workspace/kibana.yml /workspace/kibana.yml
COPY workspace/logstash.conf /workspace/logstash.conf

# Define working directory.
WORKDIR /workspace

#Install elasticsearch Head and Marvel plugins.
RUN /elasticsearch/bin/plugin -i elasticsearch/marvel/latest
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head
RUN /elasticsearch/bin/plugin -install lukas-vlcek/bigdesk
RUN /elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf
RUN /elasticsearch/bin/plugin -install elasticsearch/license/latest
RUN /elasticsearch/bin/plugin -install elasticsearch/watcher/latest

# Define default command.
CMD ["/usr/bin/supervisord"]

# Expose ports.
EXPOSE 9200 9300 5601 5000/udp 6666
