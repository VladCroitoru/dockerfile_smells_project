FROM java:8-jre

MAINTAINER Boris Mikhaylov

ENV SPARK_VERSION 1.6.2
ENV HADOOP_VERSION 2.6.4
ENV MAHOUT_VERSION 0.12.2
ENV SPARK_HOME /usr/local/spark-${SPARK_VERSION}-bin-hadoop2.6
ENV HADOOP_HOME /usr/local/hadoop-${HADOOP_VERSION}
ENV MAHOUT_HOME /usr/local/apache-mahout-distribution-${MAHOUT_VERSION}
ENV MAHOUT_LOCAL true

WORKDIR /tmp
RUN wget --quiet http://www-us.apache.org/dist/mahout/${MAHOUT_VERSION}/apache-mahout-distribution-${MAHOUT_VERSION}.tar.gz && \
    tar -xzf apache-mahout-distribution-${MAHOUT_VERSION}.tar.gz && \
    mv apache-mahout-distribution-${MAHOUT_VERSION} /usr/local/apache-mahout-distribution-${MAHOUT_VERSION} && \
    ln -sf /usr/local/apache-mahout-distribution-${MAHOUT_VERSION}/bin/mahout /usr/local/bin/mahout

RUN wget --quiet https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} /usr/local/hadoop-${HADOOP_VERSION}

RUN wget --quiet http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop2.6.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop2.6.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop2.6 /usr/local/spark-${SPARK_VERSION}-bin-hadoop2.6

ENV RC_VERSION 0.0.8
RUN wget --quiet https://github.com/kagux/go-remote-cli/releases/download/${RC_VERSION}/linux-amd64-remote_cli.tar.bz2 \
    && tar -jxf linux-amd64-remote_cli.tar.bz2 \
    && mv bin/linux/amd64/remote_cli /usr/local/bin/remote_cli

RUN rm -rf /tmp/*

ADD entrypoint.sh /opt/entrypoint.sh
ADD spark/ $SPARK_HOME/

EXPOSE 9021
ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["remote_cli", "--server", "--host=0.0.0.0", "--port=9021"]
