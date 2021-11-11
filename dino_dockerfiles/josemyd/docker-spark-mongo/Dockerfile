FROM ubuntu:16.04

MAINTAINER Josemy Duarte <duartejosemy@gmail.com>

# See https://github.com/phusion/baseimage-docker/issues/58
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update \
    && apt-get install -y wget ipython python-setuptools build-essential python-dev python-pip openjdk-8-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

RUN pip --no-cache-dir install pymongo 

ENV SPARK_VERSION 2.4.3
ENV HADOOP_VERSION 2.6
ENV MONGO_HADOOP_VERSION 1.5.2
ENV MONGO_HADOOP_COMMIT r1.5.2

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME /usr/local/spark

ENV APACHE_MIRROR http://ftp.ps.pl/pub/apache
ENV SPARK_URL ${APACHE_MIRROR}/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
ENV SPARK_DIR spark-${SPARK_VERSION}-bin-hadoop2.6

ENV MONGO_HADOOP_URL https://github.com/mongodb/mongo-hadoop/archive/${MONGO_HADOOP_COMMIT}.tar.gz

ENV MONGO_HADOOP_LIB_PATH /usr/local/mongo-hadoop/build/libs
ENV MONGO_HADOOP_JAR  ${MONGO_HADOOP_LIB_PATH}/mongo-hadoop-${MONGO_HADOOP_VERSION}.jar

ENV MONGO_HADOOP_SPARK_PATH /usr/local/mongo-hadoop/spark
ENV MONGO_HADOOP_SPARK_JAR ${MONGO_HADOOP_SPARK_PATH}/build/libs/mongo-hadoop-spark-${MONGO_HADOOP_VERSION}.jar
ENV PYTHONPATH  ${MONGO_HADOOP_SPARK_PATH}/src/main/python:$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip

ENV SPARK_DRIVER_EXTRA_CLASSPATH ${MONGO_HADOOP_JAR}:${MONGO_HADOOP_SPARK_JAR}
ENV CLASSPATH ${SPARK_DRIVER_EXTRA_CLASSPATH}
ENV JARS ${MONGO_HADOOP_JAR},${MONGO_HADOOP_SPARK_JAR}

ENV PYSPARK_DRIVER_PYTHON /usr/bin/ipython
ENV PATH $PATH:$SPARK_HOME/bin

ENV NB_USER spark
ENV NB_UID 1000

# Download  Spark
RUN wget -qO - ${SPARK_URL} | tar -xz -C /usr/local/ \
    && cd /usr/local && ln -s ${SPARK_DIR} spark

RUN wget -qO - ${MONGO_HADOOP_URL} | tar -xz -C /usr/local/ \
    && mv /usr/local/mongo-hadoop-${MONGO_HADOOP_COMMIT} /usr/local/mongo-hadoop \
    && cd /usr/local/mongo-hadoop \
    && ./gradlew jar

RUN echo "spark.driver.extraClassPath   ${CLASSPATH}" > $SPARK_HOME/conf/spark-defaults.conf

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

USER $NB_USER
WORKDIR /home/$NB_USER

CMD ["/bin/bash", "-c", "$SPARK_HOME/bin/pyspark --jars ${JARS} --driver-class-path ${SPARK_DRIVER_EXTRA_CLASSPATH}"]