FROM dataiku/dss:latest

MAINTAINER Cedric DUE <cedric@saagie.com>

USER root

RUN apt-get update && apt-get install -y wget

RUN wget http://apache.mirrors.tds.net/hadoop/common/hadoop-2.6.5/hadoop-2.6.5.tar.gz && \
	mkdir -p /etc/hadoop && \
	tar -xzf hadoop-2.6.5.tar.gz -C /etc/hadoop --strip-components=1

RUN wget https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.6.tgz && \
	mkdir -p /opt/spark && \
	tar -xzf spark-2.1.0-bin-hadoop2.6.tgz -C /opt/spark --strip-components=1

COPY run-dataiku.sh /home/dataiku
RUN chown dataiku:dataiku /home/dataiku/run-dataiku.sh && \
  chmod 755 /home/dataiku/run-dataiku.sh

USER dataiku

RUN mkdir /home/dataiku/lib/
RUN wget http://central.maven.org/maven2/org/apache/hive/hive-common/1.1.0/hive-common-1.1.0.jar -P /home/dataiku/lib/ && \
  wget http://central.maven.org/maven2/org/apache/hive/hive-jdbc/1.1.0/hive-jdbc-1.1.0.jar -P /home/dataiku/lib/ && \
  wget http://central.maven.org/maven2/org/apache/hive/hive-service/1.1.0/hive-service-1.1.0.jar -P /home/dataiku/lib/ && \
  wget http://central.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.3/httpclient-4.5.3.jar -P /home/dataiku/lib/ && \
  wget http://central.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.7/httpcore-4.4.7.jar -P /home/dataiku/lib/ && \
  wget http://central.maven.org/maven2/org/apache/thrift/libthrift/0.10.0/libthrift-0.10.0.jar -P /home/dataiku/lib/


ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/jre/
ENV PATH $PATH:/etc/hadoop/bin/:/etc/hadoop/sbin:/opt/spark/bin
ENV HADOOP_CONF_DIR /etc/hadoop/conf
ENV HIVE_CONF_DIR /etc/hadoop/conf
ENV HADOOP_HOME /etc/hadoop
ENV HADOOP_LIB_EXEC /etc/hadoop/libexec/
ENV SPARK_HOME /opt/spark

ENTRYPOINT ["/home/dataiku/run-dataiku.sh"]
