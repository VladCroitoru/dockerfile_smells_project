FROM openjdk:8u131-jre-alpine
ENV INSTALL_DIR /opt/elasticmq
ENV ELASTICMQ_VERSION 0.13.5

# Setup
RUN \
  # Fix for Java DNS Caching
  grep '^networkaddress.cache.ttl=' $JAVA_HOME/lib/security/java.security \
      || echo 'networkaddress.cache.ttl=60' >> $JAVA_HOME/lib/security/java.security \
  #  Add openssl
  && apk add --no-cache --update \
      openssl \
  # Setup elasticmq
  && mkdir -p $INSTALL_DIR \
  && wget -O $INSTALL_DIR/elasticmq-server.jar \
      https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-$ELASTICMQ_VERSION.jar \
  # Cleanup
  && rm -rf ~/.cache /tmp/*

WORKDIR $INSTALL_DIR

ADD conf $INSTALL_DIR/conf

EXPOSE 9324

CMD ["java", "-Dconfig.file=conf/default.conf", "-jar", "elasticmq-server.jar"]
