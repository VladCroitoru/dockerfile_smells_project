# https://github.com/gettyimages/docker-spark

FROM debian:stable

MAINTAINER Carlo Alberto Degli Atti <lordkada@gmail.com>

# Update & Install packages
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list

RUN apt-get update && apt-get install -y --force-yes \
        curl

# JAVA Setup
ENV JAVA_HOME /usr/jdk1.8.0_45
ENV PATH $PATH:$JAVA_HOME/bin
RUN curl -sL --retry 3 --insecure \
        --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
        "http://download.oracle.com/otn-pub/java/jdk/8u45-b14/server-jre-8u45-linux-x64.tar.gz" \
        | gunzip \
        | tar x -C /usr/ \
        && ln -s $JAVA_HOME /usr/java \
        && rm -rf $JAVA_HOME/man

# Spark
ENV SPARK_VERSION 1.2.2
ENV SPARK_HOME /usr/local/spark

RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_VERSION-bin-hadoop2.4.tgz | tar -xz -C /usr/local/

RUN ln -s /usr/local/spark-$SPARK_VERSION-bin-hadoop2.4 $SPARK_HOME

ADD scripts/master_start.sh /usr/local/master_start.sh
RUN chmod +x /usr/local/master_start.sh

ADD scripts/worker_start.sh /usr/local/worker_start.sh
RUN chmod +x /usr/local/worker_start.sh

CMD ["/usr/local/master_start.sh"]
