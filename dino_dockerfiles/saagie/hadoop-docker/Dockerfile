FROM anapsix/alpine-java

RUN wget http://archive-primary.cloudera.com/cdh5/cdh/5/hadoop-2.6.0-cdh5.7.1.tar.gz

RUN tar -xzf hadoop-2.6.0-cdh5.7.1.tar.gz \
   && mv hadoop-2.6.0-cdh5.7.1 /usr/local/hadoop

ENV HADOOP_HOME=/usr/local/hadoop

ENV PATH=$PATH:$HADOOP_HOME/bin

