FROM java:8u92-jre-alpine

RUN apk -U add bash bc

ENV ES_VERSION=5.6.2

ADD https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ES_VERSION.tar.gz /tmp/es/
RUN cd /tmp/es && \
  tar zxvf /tmp/es/elasticsearch-$ES_VERSION.tar.gz && \
  cp -rfvp /tmp/es/elasticsearch-$ES_VERSION /usr/share/ && \
  rm -rf  /tmp/es

EXPOSE 9200 9300

ENV ES_HOME=/usr/share/elasticsearch-$ES_VERSION \
    DEFAULT_ES_USER=elasticsearch \
    DISCOVER_IP=eth0 \
    ES_JAVA_OPTS="" \ 
    PCT_HEAP_MEM=75

#pagarme used plugins
RUN $ES_HOME/bin/elasticsearch-plugin install discovery-ec2  --batch && \
    $ES_HOME/bin/elasticsearch-plugin install repository-s3  --batch
    #consul discovery plugin, see more in https://github.com/vvanholl/elasticsearch-consul-discovery
    # $ES_HOME/bin/elasticsearch-plugin install https://github.com/claytonsilva/elasticsearch-consul-discovery/releases/download/$ES_VERSION/elasticsearch-consul-discovery-$ES_VERSION.zip --batch 

#add log4j support for json
# ADD http://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.5.0/jackson-annotations-2.5.0.jar $ES_HOME/lib
# ADD http://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.5.3/jackson-databind-2.5.3.jar $ES_HOME/lib

#add java policies for plugins
COPY java.policy $JAVA_HOME/lib/security

## change owner for the elasticsearch resources 
RUN adduser -S -s /bin/sh $DEFAULT_ES_USER && \ 
    chown -R $DEFAULT_ES_USER /usr/share/elasticsearch-$ES_VERSION


#remove duplicate deps for instaled plugins 
# RUN rm -rf  /usr/share/elasticsearch-$ES_VERSION/plugins/**/jackson-databind-* && \
#     rm -rf  /usr/share/elasticsearch-$ES_VERSION/plugins/**/jackson-annotations-* 


VOLUME ["/data","/conf"]

WORKDIR $ES_HOME

COPY start /start
COPY log4j2.properties $ES_HOME/config/

CMD ["bash","/start"]