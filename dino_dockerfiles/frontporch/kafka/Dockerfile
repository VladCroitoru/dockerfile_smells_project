FROM java:openjdk-8-jre

ENV DEBIAN_FRONTEND="noninteractive"
ENV SCALA_VERSION="2.11"
ENV KAFKA_VERSION="0.9.0.1"
ENV KAFKA_HOME=/opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"
ENV PATH="$PATH:$KAFKA_HOME/bin"

# Expose default Kafka port
EXPOSE 9092

# Expose metrics via JMX
EXPOSE 9999

# Expose JMX RMI Port
EXPOSE 9998

# https://github.com/Yelp/dumb-init
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && chmod +x /usr/local/bin/dumb-init

# Install Kafka and dependencies
RUN wget -q http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \
    tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \
    rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz

# Copy over init script
COPY start-kafka.sh /usr/bin/start-kafka.sh

ENTRYPOINT ["/usr/local/bin/dumb-init"]
CMD ["/usr/bin/start-kafka.sh"]
