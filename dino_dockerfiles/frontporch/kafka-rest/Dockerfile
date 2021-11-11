FROM openjdk:8-jdk

ENV ZK_CONNECTION_STRING=localhost:2181

ENV KAFKA_REST_VERSION=2.0.1
ENV KAFKA_REST_ZIP=confluent-2.0.1-2.11.7.zip
ENV KAFKA_REST_URI=http://packages.confluent.io/archive/2.0/$KAFKA_REST_ZIP
ENV KAFKA_REST_PROPS=./etc/kafka-rest/kafka-rest.properties
ENV WORKDIR=/tmp/confluent

RUN mkdir $WORKDIR && cd $WORKDIR && \

    # Download the zip 
    wget -q $KAFKA_REST_URI && \

    # Create output directory for zip
    mkdir /opt/confluent-$KAFKA_REST_VERSION && \

    # Unzip
    unzip $KAFKA_REST_ZIP -d /opt && \

    # Cleanup after ourselves
    rm -rf $WORKDIR

EXPOSE 8082

WORKDIR /opt/confluent-$KAFKA_REST_VERSION

# Add the Zookeeper connnection string to the properties file & start kafka-rest
CMD echo "zookeeper.connect=${ZK_CONNECTION_STRING}" >> $KAFKA_REST_PROPS && ./bin/kafka-rest-start $KAFKA_REST_PROPS
