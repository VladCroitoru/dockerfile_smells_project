FROM openjdk:8-jdk

ENV FLUME_VERSION 1.7.0
ENV FLUME_HOME /opt/apache-flume
ENV FLUME_AGENT my-flume-agent
ENV HADOOP_VERSION=2.7.1
ENV HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION

WORKDIR /opt

RUN wget -O flume.tar.gz http://archive.apache.org/dist/flume/$FLUME_VERSION/apache-flume-$FLUME_VERSION-bin.tar.gz \
    && tar -xvzf flume.tar.gz \
    && mv /opt/apache-flume-$FLUME_VERSION-bin/ $FLUME_HOME \
    && mkdir /data-source /flume $FLUME_HOME/plugins.d

WORKDIR $FLUME_HOME

ADD entrypoint.sh /

RUN chmod +x /entrypoint.sh \
    && wget -q http://www.eu.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -O /opt/hadoop-$HADOOP_VERSION.tar.gz \
    && tar xf /opt/hadoop-$HADOOP_VERSION.tar.gz -C /opt/ \
    && rm /opt/hadoop-$HADOOP_VERSION.tar.gz

CMD /entrypoint.sh
