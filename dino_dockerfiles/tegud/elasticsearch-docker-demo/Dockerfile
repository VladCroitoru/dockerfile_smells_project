FROM elasticsearch:2.2.0

ENV ES_HEAP_SIZE=1024m

ENV ES_JAVA_OPTS=" \
  -server \
  -Djava.net.preferIPv4Stack=true \
  -Xms1024m \
  -Xmx1024m \
  -Xss256k \
    -XX:+UseParNewGC \
  -XX:+UseConcMarkSweepGC \
  -XX:CMSInitiatingOccupancyFraction=75 \
  -XX:+UseCMSInitiatingOccupancyOnly \
  -XX:+HeapDumpOnOutOfMemoryError"

RUN /usr/share/elasticsearch/bin/plugin install lmenezes/elasticsearch-kopf/2.0

ADD ./elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
