FROM raycoding/piggybank
MAINTAINER Shuddhashil Ray rayshuddhashil@gmail.com

# Environment Variables
ENV ZK_VERSION 3.4.6
ENV ZK zookeeper-$ZK_VERSION
ENV ZK_HOME /usr/lib/$ZK

# Fetching Zookeeper 3.4.6
RUN (cd /usr/lib && wget  -q -nc "http://apache.mirrors.pair.com/zookeeper/$ZK/$ZK.tar.gz")
RUN tar -xzvf /usr/lib/$ZK.tar.gz -C /usr/lib/

# Setting Up Zookeeper 3.4.6
RUN mkdir -p "$ZK_HOME/zookeeper-data"
RUN mkdir -p "$ZK_HOME/zookeeper-logs"
ADD zoo.cfg /usr/lib/zookeeper-3.4.6/conf/zoo.cfg
WORKDIR /usr/lib/zookeeper-3.4.6
RUN rm -f /usr/lib/$ZK.tar.gz

# Building Exhibitor Stand-Alone version 1.5.1
RUN mkdir -p /usr/lib/exhibitor
ADD pom.xml /usr/lib/exhibitor/pom.xml
RUN cd /usr/lib/exhibitor && mvn assembly:single
RUN ln -s /usr/lib/exhibitor/target/exhibitor-1.0-jar-with-dependencies.jar /usr/lib/exhibitor/exhibitor.jar
ADD startup.sh /usr/lib/exhibitor/startup.sh
RUN export PATH=$PATH:/usr/lib/jvm/jdk1.7.0_60/bin
ENV PATH $JAVA_HOME/bin:$PATH

# Exposing client port
EXPOSE 2181 2888 3888 8383

# Exposing Mount Volumes in Host
VOLUME ["/usr/lib/zookeeper-3.4.6/conf", "/usr/lib/zookeeper-3.4.6/zookeeper-data", "/usr/lib/zookeeper-3.4.6/zookeeper-logs"]
# CMD ["start-foreground"]
# ENTRYPOINT ["/usr/lib/zookeeper-3.4.6/bin/zkServer.sh"]

WORKDIR /usr/lib/exhibitor
ENTRYPOINT ["bash", "-ex", "/usr/lib/exhibitor/startup.sh"]