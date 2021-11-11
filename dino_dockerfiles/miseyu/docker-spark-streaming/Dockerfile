FROM debian:jessie

# Environment
ENV SPARK_VERSION 2.1.1
ENV HADOOP_VERSION 2.7
ENV SCALA_VERSION 2.11
ENV SPARK_HOME /usr/local/spark

RUN echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list

RUN apt-get -y update && apt-get install -y wget && apt-get install -y -t jessie-backports --no-install-recommends openjdk-8-jdk

# Spark
RUN cd /tmp && \
    wget http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

RUN cd /usr/local && ln -s spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

# Spark Kafka Streaming
RUN cd /tmp && \
    wget http://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_${SCALA_VERSION}/${SPARK_VERSION}/spark-streaming-kafka-0-10-assembly_${SCALA_VERSION}-${SPARK_VERSION}.jar && \
    mv spark-streaming-kafka-0-10-assembly_${SCALA_VERSION}-${SPARK_VERSION}.jar /usr/local/spark/jars


EXPOSE 8080
EXPOSE 6066
EXPOSE 7077
