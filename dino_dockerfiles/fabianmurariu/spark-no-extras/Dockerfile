FROM anapsix/alpine-java
MAINTAINER fabianmurariu

RUN apk update && apk add curl

ENV SPARK_VERSION 1.5.2
ENV HADOOP_VERSION 2.6
ENV SPARK_PACKAGE $SPARK_VERSION-bin-hadoop$HADOOP_VERSION
ENV SPARK_HOME /usr/spark-$SPARK_PACKAGE
ENV PATH $PATH:$SPARK_HOME/bin
RUN curl -L --retry 3 \
  "http://apache.mirrors.lucidnetworks.net/spark/spark-$SPARK_VERSION/spark-$SPARK_PACKAGE.tgz" \
  | gunzip \
  | tar x -C /usr/ \
  && ln -s $SPARK_HOME /usr/spark \
  && rm /usr/spark-$SPARK_PACKAGE/lib/spark-examples* \
  && rm -rf /usr/spark-$SPARK_PACKAGE/examples

# HADOOP/S3
RUN curl -sL --retry 3 "http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.6.0/hadoop-aws-2.6.0.jar" -o $SPARK_HOME/lib/hadoop-aws-2.6.0.jar \
 && curl -sL --retry 3 "http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.14/aws-java-sdk-1.7.14.jar" -o $SPARK_HOME/lib/aws-java-sdk-1.7.14.jar \
 && curl -sL --retry 3 "http://central.maven.org/maven2/com/google/collections/google-collections/1.0/google-collections-1.0.jar" -o $SPARK_HOME/lib/google-collections-1.0.jar \
 && curl -sL --retry 3 "http://central.maven.org/maven2/joda-time/joda-time/2.8.2/joda-time-2.8.2.jar" -o $SPARK_HOME/lib/joda-time-2.8.2.jar

WORKDIR /usr/spark/bin/
