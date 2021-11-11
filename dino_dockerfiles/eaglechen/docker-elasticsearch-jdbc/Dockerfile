FROM java:8-jre
MAINTAINER Eagle Chen <chygr1234@gmail.com>

ENV VERSION=2.2.1.0

RUN \
  cd /tmp && \
  wget http://xbib.org/repository/org/xbib/elasticsearch/importer/elasticsearch-jdbc/$VERSION/elasticsearch-jdbc-$VERSION-dist.zip && \
  unzip elasticsearch-jdbc-$VERSION-dist.zip && \
  mv elasticsearch-jdbc-$VERSION /elasticsearch-jdbc && \
  rm /tmp/elasticsearch-jdbc-$VERSION-dist.zip && \
  wget https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-linux.gz && \
  zcat go-cron-linux.gz > /usr/local/bin/go-cron && \
  chmod u+x /usr/local/bin/go-cron && \
  rm go-cron-linux.gz

COPY sqljdbc42.jar /elasticsearch-jdbc/lib/
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
