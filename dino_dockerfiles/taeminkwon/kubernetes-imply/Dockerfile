FROM ubuntu:14.04

# Prepare OS
COPY setup-os.sh /root/setup-os.sh
COPY nodesource-pubkey /root/nodesource-pubkey
RUN /root/setup-os.sh

# Setup imply
ENV implyversion 1.1.0
COPY setup-imply.sh /root/setup-imply.sh
RUN /root/setup-imply.sh

# Copy package from build directory
ENV KAFKA_HOST_NAME kafka-zoo-svc

# Setup kafka hostname
COPY setup-kafka-server.sh /root/setup-kafka-server.sh
RUN /root/setup-kafka-server.sh

# Copy files
COPY quickstart.conf /root/imply-${implyversion}/conf/supervise/quickstart.conf
COPY kafka.json /root/imply-${implyversion}/conf-quickstart/tranquility/kafka.json

EXPOSE 1527 2181 8081 8082 8083 8090 8091 8100 8101 8102 8103 8104 8105 8106 8107 8108 8109 8110 8200 9095

# Start imply pivot
WORKDIR /root/imply-${implyversion}

#CMD ["bin/supervise", "-c", "conf/supervise/quickstart.conf"]
