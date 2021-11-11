FROM java:8-jre-alpine

MAINTAINER tobilg@gmail.com

# Install requirements
RUN apk add --no-cache bash curl snappy

# Set environment variables
ENV FLINK_DATA /data
ENV FLINK_HOME /usr/local/flink
ENV PATH $PATH:$FLINK_HOME/bin

# Install Flink
ENV FLINK_VERSION=1.1.3
ENV HADOOP_VERSION=27
ENV SCALA_VERSION=2.11

RUN curl -s $(curl -s https://www.apache.org/dyn/closer.cgi\?as_json\=1 | awk '/preferred/ {gsub(/"/,""); print $2}')flink/flink-${FLINK_VERSION}/flink-${FLINK_VERSION}-bin-hadoop${HADOOP_VERSION}-scala_${SCALA_VERSION}.tgz | tar xvz -C /usr/local/ && \
    ln -s /usr/local/flink-$FLINK_VERSION $FLINK_HOME

# Add container entrypoint
ADD docker-entrypoint.sh docker-entrypoint.sh

# Add base config
ADD flink-conf.yaml $FLINK_HOME/conf/flink-conf.yaml

# Set config env variable
ENV FLINK_CONFIG_FILE $FLINK_HOME/conf/flink-conf.yaml

# Make entrypoint executable and create folders
RUN chmod +x docker-entrypoint.sh && \
    mkdir -p $FLINK_DATA/zk && \
    mkdir -p $FLINK_DATA/tasks && \
    mkdir -p $FLINK_DATA/blobs

WORKDIR /

ENTRYPOINT ["/docker-entrypoint.sh"]
