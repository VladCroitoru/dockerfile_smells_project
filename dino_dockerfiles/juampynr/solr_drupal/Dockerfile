FROM openjdk:7-jre

RUN apt-get update && \
  apt-get -y install wget && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /opt/solr

RUN wget https://archive.apache.org/dist/lucene/solr/1.4.1/apache-solr-1.4.1.tgz
RUN tar xvzf apache-solr-1.4.1.tgz

RUN wget https://ftp.drupal.org/files/projects/apachesolr-7.x-1.9.tar.gz
RUN tar xvzf apachesolr-7.x-1.9.tar.gz
RUN cp /opt/solr/apachesolr/solr-conf/solr-1.4/* /opt/solr/apache-solr-1.4.1/example/solr/conf

ADD start.sh /opt/solr

EXPOSE 8983
ENTRYPOINT ["/opt/solr/start.sh"]
