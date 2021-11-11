FROM brightlee6/docker-ubuntu-java

RUN apt-get -y update
RUN apt-get -y install curl

# SPARK
ARG SPARK_ARCHIVE=http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz
ENV SPARK_HOME /usr/local/spark-2.0.0-bin-hadoop2.7

ENV PATH $PATH:${SPARK_HOME}/bin
RUN curl -s ${SPARK_ARCHIVE} | tar -xz -C /usr/local/

WORKDIR $SPARK_HOME

