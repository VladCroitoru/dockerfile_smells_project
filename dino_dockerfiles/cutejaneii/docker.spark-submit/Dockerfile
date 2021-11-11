FROM python:2.7

MAINTAINER Jennifer Liao <cutejaneii@hotmail.com>

ENV HADOOP_USER_NAME=pbxuser

RUN \
  pip install wget && \
  wget https://downloads.lightbend.com/scala/2.11.11/scala-2.11.11.tgz && \
  wget http://apache.stu.edu.tw/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz && \
  wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jre-8u131-linux-x64.tar.gz

RUN apt-get update
RUN apt-get -y install python-pip
RUN pip install kafka-python

# unzip tgz files and move to /usr/local/
RUN \
  tar xvf scala-2.11.11.tgz && \
  mv scala-2.11.11 /usr/local/scala && \
  tar xvf spark-2.2.0-bin-hadoop2.7.tgz && \
  mv spark-2.2.0-bin-hadoop2.7 /usr/local/spark2.2.0_h2.7 && \
  tar xvf jre-8u131-linux-x64.tar.gz && \
  mv jre1.8.0_131 /usr/local/jre

# Install py4j / Cassandra-driver / pandas
RUN \
  pip install py4j && \
  pip install cassandra-driver && \
  pip install pandas && \
  pip install hdfs

RUN pip install flask
RUN pip install requests

# Environment variables

ENV SPARK_HOME=/usr/local/spark2.2.0_h2.7
ENV JAVA_HOME=/usr/local/jre \
    PATH=$PATH:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/python:$JAVA_HOME/bin \
    JRE_HOME=/usr/local/jdk/jre \
    CLASSPATH=$CLASSPATH:.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib \
    HADOOP_USER_NAME=$HADOOP_USER_NAME

ENV PYTHONPATH=$PYTHONPATH:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/python

RUN mkdir /usr/local/spark_jars

RUN mkdir /app

# Install Supervisord
RUN apt-get update && apt-get install -y supervisor

# Custom Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
