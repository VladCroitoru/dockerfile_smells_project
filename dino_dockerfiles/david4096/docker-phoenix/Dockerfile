FROM sequenceiq/hadoop-docker:2.7.0
MAINTAINER David Steinberg david@resium.com

# zookeeper
ENV ZOOKEEPER_VERSION 3.4.6
RUN curl -s http://mirror.csclub.uwaterloo.ca/apache/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./zookeeper-$ZOOKEEPER_VERSION zookeeper
ENV ZOO_HOME /usr/local/zookeeper
ENV PATH $PATH:$ZOO_HOME/bin
RUN mv $ZOO_HOME/conf/zoo_sample.cfg $ZOO_HOME/conf/zoo.cfg
RUN mkdir /tmp/zookeeper

# hbase
ENV HBASE_MAJOR 1.2
ENV HBASE_MINOR 6
ENV HBASE_VERSION "${HBASE_MAJOR}.${HBASE_MINOR}"
RUN curl -s http://www-eu.apache.org/dist/hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-bin.tar.gz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./hbase-$HBASE_VERSION hbase
ENV HBASE_HOME /usr/local/hbase
ENV PATH $PATH:$HBASE_HOME/bin
RUN rm $HBASE_HOME/conf/hbase-site.xml
ADD hbase-site.xml $HBASE_HOME/conf/hbase-site.xml

# phoenix
ENV PHOENIX_VERSION 4.11.0
RUN curl -s http://www-eu.apache.org/dist/phoenix/apache-phoenix-$PHOENIX_VERSION-HBase-$HBASE_MAJOR/bin/apache-phoenix-$PHOENIX_VERSION-HBase-$HBASE_MAJOR-bin.tar.gz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./apache-phoenix-$PHOENIX_VERSION-HBase-$HBASE_MAJOR-bin phoenix
ENV PHOENIX_HOME /usr/local/phoenix
ENV PATH $PATH:$PHOENIX_HOME/bin
RUN cp $PHOENIX_HOME/phoenix-core-$PHOENIX_VERSION-HBase-$HBASE_MAJOR.jar $HBASE_HOME/lib/phoenix.jar
RUN ls $PHOENIX_HOME
RUN cp $PHOENIX_HOME/phoenix-$PHOENIX_VERSION-HBase-$HBASE_MAJOR-server.jar $HBASE_HOME/lib/phoenix-server.jar

# bootstrap-phoenix
ADD bootstrap-phoenix.sh /etc/bootstrap-phoenix.sh
RUN chown root:root /etc/bootstrap-phoenix.sh
RUN chmod 700 /etc/bootstrap-phoenix.sh

CMD ["/etc/bootstrap-phoenix.sh"]

EXPOSE 8765
EXPOSE 8088
