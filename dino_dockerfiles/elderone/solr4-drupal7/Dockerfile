FROM java:jre

MAINTAINER El de Rone <elderone@ya.ru>

ENV SOLR_VERSION 4.10.4
ENV SOLR solr-$SOLR_VERSION
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

RUN \
    curl -SL http://ftp.byfly.by/pub/apache.org/lucene/solr/$SOLR_VERSION/$SOLR.tgz | tar -xzC /opt && \
    curl -SL http://ftp.drupal.org/files/projects/apachesolr-7.x-1.7.tar.gz | tar -xzC /tmp && \
    ln -s /opt/$SOLR/example /opt/solr && \
    ln -s /tmp/apachesolr/solr-conf/solr-4.x /opt/$SOLR/example/multicore/core0/conf

ENV SOLR_HOME /opt/solr

EXPOSE 8983
WORKDIR /opt/solr
ENTRYPOINT [ "java", "-Xmx1024m", "-DSTOP.PORT=8079", "-DSTOP.KEY=stopkey", "-Dsolr.solr.home=multicore", "-jar", "start.jar" ]
