# Kafka and Zookeeper: thanks to https://hub.docker.com/r/spotify/kafka/
# Maven: Thanks to https://hub.docker.com/_/maven/ version: jdk-8

FROM openjdk:8-jdk

ENV DEBIAN_FRONTEND noninteractive
ENV SCALA_VERSION 2.11
# first kafka version 10.2. to support single value extraction (f.eg. RabbitMQ AMQP msg Body only): org.apache.kafka.connect.transforms.ExtractField$Value
ENV KAFKA_VERSION 0.10.2.0
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"
# maven
ARG MAVEN_VERSION=3.5.0
ARG USER_HOME_DIR="/root"
ARG SHA=beb91419245395bd69a4a6edad5ca3ec1a8b64e41457672dc687c173a495f034
ARG BASE_URL=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/${MAVEN_VERSION}

# Install maven
RUN mkdir -p /usr/share/maven /usr/share/maven/ref && \
    curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    echo "${SHA}  /tmp/apache-maven.tar.gz" | sha256sum -c - && \
    tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 && \
    rm -f /tmp/apache-maven.tar.gz && \
    ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME=/usr/share/maven
ENV MAVEN_CONFIG="$USER_HOME_DIR/.m2"

COPY maven_files/mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh
COPY maven_files/settings-docker.xml /usr/share/maven/ref/
RUN chmod +wrx /usr/local/bin/mvn-entrypoint.sh
RUN chmod +wrx /usr/share/maven/ref/
RUN /usr/local/bin/mvn-entrypoint.sh

# Install Kafka and Zookeeper
RUN apt-get update && \
    apt-get install -y zookeeper wget supervisor dnsutils git vim && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    wget -q https://archive.apache.org/dist/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \
    tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \
    rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz

# Confluent Platform v3.1.1 install
ENV CONFLUENT_PLATFORM_VERSION 3.1.1
RUN apt-get update && \
    apt-get install -y wget gnupg software-properties-common && \
    wget -qO - http://packages.confluent.io/deb/3.1/archive.key | apt-key add - && \
    add-apt-repository "deb [arch=amd64] http://packages.confluent.io/deb/3.1 stable main" && \
    apt-get update && apt-get install -y confluent-platform-oss-2.11 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh

# Supervisor config
ADD supervisor/kafka.conf supervisor/zookeeper.conf /etc/supervisor/conf.d/

# create Kafka Connect Jars...
# RabbitMQ connect
RUN git clone https://github.com/jcustenborder/kafka-connect-rabbitmq.git /kafka-connect-rabbitmq
WORKDIR /kafka-connect-rabbitmq
RUN mvn compile && \
    mvn package && \
    mvn install && \
    cp target/kafka-connect-target/usr/share/kafka-connect/kafka-connect-rabbitmq/* ${KAFKA_HOME}/libs/ && \
    rm -rf /kafka-connect-rabbitmq

# 2181 is zookeeper, 9092 is kafka
EXPOSE 2181 9092

VOLUME "$KAFKA_HOME/config"

WORKDIR $KAFKA_HOME

CMD ["supervisord", "-n"]
