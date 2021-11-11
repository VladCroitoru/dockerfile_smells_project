FROM python:2.7

MAINTAINER Jennifer Liao <cutejaneii@hotmail.com>

RUN \
  pip install wget && \
  wget https://downloads.lightbend.com/scala/2.11.11/scala-2.11.11.tgz && \
  wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.6.tgz && \
  wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jre-8u131-linux-x64.tar.gz

RUN apt-get update
RUN apt-get -y install python-pip
RUN pip install kafka-python

# unzip tgz files and move to /usr/local/
RUN \
  tar xvf scala-2.11.11.tgz && \
  mv scala-2.11.11 /usr/local/scala && \
  tar xvf spark-2.0.2-bin-hadoop2.6.tgz && \
  mv spark-2.0.2-bin-hadoop2.6 /usr/local/spark && \
  tar xvf jre-8u131-linux-x64.tar.gz && \
  mv jre1.8.0_131 /usr/local/jre

# Install py4j / Cassandra-driver / pandas
RUN \
  pip install py4j && \
  pip install cassandra-driver && \
  pip install pandas

RUN pip install flask
RUN pip install requests
RUN pip install pywebhdfs

# Environment variables

ENV SPARK_HOME=/usr/local/spark
ENV JAVA_HOME=/usr/local/jre \
    PATH=$PATH:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/python:$JAVA_HOME/bin \
    JRE_HOME=/usr/local/jdk/jre \
    CLASSPATH=$CLASSPATH:.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib

ENV PYTHONPATH=$PYTHONPATH:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/python

# Download jars
RUN mkdir /usr/local/spark_jars

WORKDIR /usr/local/spark_jars

COPY ./spark_jars /usr/local/spark_jars

# Copy spark-defaults.conf to add spark.driver.extraClassPath
COPY spark-defaults.conf /usr/local/spark/conf/spark-defaults.conf

RUN mkdir /app

COPY ./app /app

# Install Supervisord
RUN apt-get update && apt-get install -y supervisor

# Custom Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
