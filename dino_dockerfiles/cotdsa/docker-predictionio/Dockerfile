FROM ubuntu
MAINTAINER Matteo Sessa <webops@catchoftheday.com.au>

ENV PIO_VERSION 0.9.6
ENV SPARK_VERSION 1.5.2
ENV SQLITE_JDBC_VER 3.8.9.1

ENV PIO_HOME /PredictionIO-${PIO_VERSION}
ENV PATH=${PIO_HOME}/bin:$PATH
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN apt-get update \
    && apt-get install -y --auto-remove --no-install-recommends curl openjdk-8-jdk libgfortran3 python-pip sqlite3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -O https://s3-ap-southeast-2.amazonaws.com/cotdsa-public/PredictionIO-${PIO_VERSION}-spark1.5.2.tar.gz \
    && tar -xvzf PredictionIO-${PIO_VERSION}-spark1.5.2.tar.gz -C / && mkdir -p ${PIO_HOME}/vendors \
    && rm PredictionIO-${PIO_VERSION}-spark1.5.2.tar.gz

RUN curl -O http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop2.6.tgz \
    && tar -xvzf spark-${SPARK_VERSION}-bin-hadoop2.6.tgz -C ${PIO_HOME}/vendors \
    && rm spark-${SPARK_VERSION}-bin-hadoop2.6.tgz

RUN mkdir ${PIO_HOME}/plugins && cd ${PIO_HOME}/plugins && curl -O https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/${SQLITE_JDBC_VER}/sqlite-jdbc-${SQLITE_JDBC_VER}.jar

#triggers fetching the complete sbt environment
RUN ${PIO_HOME}/sbt/sbt -batch

COPY files/pio-env.sh ${PIO_HOME}/conf/pio-env.sh
