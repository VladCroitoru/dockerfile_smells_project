FROM sequenceiq/hadoop-docker:latest
MAINTAINER Riyad Parvez <riyad.parvez@gmail.com>

USER root

# install software
ADD giraph_compile.patch /etc/giraph_compile.patch
ADD giraph-setup.sh /etc/giraph-setup.sh
RUN chown root:root /etc/giraph-setup.sh && chmod 700 /etc/giraph-setup.sh 
RUN /etc/giraph-setup.sh

# set home variables
ENV HADOOP_HOME $HADOOP_PREFIX
ENV HADOOP_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV GIRAPH_HOME /usr/local/giraph
ENV GIRAPH_PREFIX /usr/local/giraph
ENV ZOOKEEPER_HOME /usr/local/zookeeper
ENV ZOOKEEPER_PREFIX /usr/local/zookeeper

# add zookeeper configuration
ADD zoo.cfg $ZOOKEEPER_PREFIX/conf/zoo.cfg

# add sample intput
ADD tiny-graph.txt $GIRAPH_PREFIX/tiny-graph.txt

# our bootstrap file
ADD giraph-bootstrap.sh /etc/giraph-bootstrap.sh
RUN chown root:root /etc/giraph-bootstrap.sh && chmod 700 /etc/giraph-bootstrap.sh

ADD run-giraph-example.sh $GIRAPH_PREFIX/run-giraph-example.sh
RUN chown root:root $GIRAPH_PREFIX/run-giraph-example.sh && chmod 700 $GIRAPH_PREFIX/run-giraph-example.sh

ENV YARN_HOME $HADOOP_PREFIX
RUN echo '# Hadoop' >> /etc/profile \
 && echo "export HADOOP_PREFIX=$HADOOP_PREFIX" >> /etc/profile \
 && echo 'export PATH=$PATH:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin' >> /etc/profile \
 && echo 'export HADOOP_MAPRED_HOME=$HADOOP_PREFIX' >> /etc/profile \
 && echo 'export HADOOP_COMMON_HOME=$HADOOP_PREFIX' >> /etc/profile \
 && echo 'export HADOOP_HDFS_HOME=$HADOOP_PREFIX' >> /etc/profile \
 && echo 'export HADOOP_HOME=$HADOOP_PREFIX' >> /etc/profile \
 && echo 'export ENV HADOOP_CONF_DIR=$HADOOP_PREFIX/etc/hadoop' >> /etc/profile \
 && echo 'export YARN_HOME=$HADOOP_PREFIX' >> /etc/profile

RUN echo '# Giraph' >> /etc/profile \
 && echo "export GIRAPH_PREFIX=$GIRAPH_PREFIX" >> /etc/profile \
 && echo 'export GIRAPH_HOME=$GIRAPH_PREFIX' >> /etc/profile

# default command
CMD ["/etc/giraph-bootstrap.sh", "-d"]
