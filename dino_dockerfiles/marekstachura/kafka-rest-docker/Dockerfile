FROM jeanblanchard/java:jre-8

MAINTAINER Marek Stachura

RUN apk add --update bash curl wget vim htop && rm -rf /var/cache/apk/*

ADD kafka-rest.properties /etc/kafka-rest/kafka-rest.properties

# Install Confluent platform.
ENV CONFLUENT_DIR_NAME confluent-1.0
ENV CONFLUENT_PKG_NAME $CONFLUENT_DIR_NAME-2.10.4

RUN \
  cd / && \
  wget http://packages.confluent.io/archive/1.0/$CONFLUENT_PKG_NAME.tar.gz && \
  tar xvzf $CONFLUENT_PKG_NAME.tar.gz && \
  rm -f $CONFLUENT_PKG_NAME.tar.gz && \
  mv /$CONFLUENT_DIR_NAME /opt/confluent

EXPOSE 8082

ADD start-kafka-rest.sh /usr/local/bin/start-kafka-rest.sh
RUN chmod +x /usr/local/bin/start-kafka-rest.sh
CMD ["/usr/local/bin/start-kafka-rest.sh"]
