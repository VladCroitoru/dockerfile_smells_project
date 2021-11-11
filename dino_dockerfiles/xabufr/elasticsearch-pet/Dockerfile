FROM docker.elastic.co/elasticsearch/elasticsearch:5.2.2

RUN elasticsearch-plugin install repository-s3

ENV NODE_DATA=false NODE_MASTER=false HTTP_ENABLE=false ES_JAVA_OPTS=-Djava.net.preferIPv4Stack=true MEM_LOCK=false

ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
USER root
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml
USER elasticsearch
