FROM sungsu7437/ubuntu_hadoop
MAINTAINER sungsu7437

USER root

RUN apt-get install -y scala
RUN apt-get install -y python
RUN apt-get install -y python3

RUN wget https://people.apache.org/~pwendell/spark-nightly/spark-branch-2.2-bin/latest/spark-2.2.0-SNAPSHOT-bin-hadoop2.6.tgz
RUN tar -xvzf spark-2.2.0-SNAPSHOT-bin-hadoop2.6.tgz -C /usr/local
RUN cd /usr/local && ln -s ./spark-2.2.0-SNAPSHOT-bin-hadoop2.6 spark

ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_YARN_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV LD_LIBRARY_PATH=/usr/local/hadoop/lib/native/:$LD_LIBRARY_PATH

ENV SPARK_HOME /usr/local/spark
ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

RUN mkdir $SPARK_HOME/yarn-remote-client
ADD yarn-remote-client $SPARK_HOME/yarn-remote-client
ADD spark-env.sh $SPARK_HOME/conf/spark-env.sh
ADD spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf
RUN cp $HADOOP_CONF_DIR/slaves $SPARK_HOME/conf/slaves

COPY bootstrap.sh /etc/bootstrap.sh
RUN chown root.root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh

ENTRYPOINT ["/etc/bootstrap.sh"]

