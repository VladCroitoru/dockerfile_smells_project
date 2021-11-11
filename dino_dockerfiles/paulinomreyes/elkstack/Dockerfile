FROM centos

RUN adduser -u 1000 elk -G root

RUN mkdir -p /opt/elastic \
  && cd /opt/elastic \
  && yum -y install java-1.8.0-openjdk-headless tar \
  && curl -s https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.1.tar.gz | tar -xz --strip-components=1 \
  && mkdir -p /opt/kibana \
  && cd /opt/kibana \
  && curl -s https://artifacts.elastic.co/downloads/kibana/kibana-6.2.1-linux-x86_64.tar.gz | tar -xz --strip-components=1 \
  && yum clean all


RUN chmod -R a=u /opt/elastic
RUN chmod -R a=u /opt/kibana
WORKDIR /opt/elastic

VOLUME /tmp/elastic /tmp/kibana

EXPOSE 9200 5601

USER elk
