FROM mesosphere/mesos:0.20.1
MAINTAINER Ian Babrou <ibobrik@gmail.com>

ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so

ENV SPARK_VERSION 1.1.1-bin-hadoop2.4

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y curl python && \
    curl -s "http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}.tgz" | tar zx -C /opt && \
    mv "/opt/spark-${SPARK_VERSION}" /opt/spark && \
    rm /opt/spark/lib/spark-examples-*.jar
