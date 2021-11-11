FROM java:8-jre

ENV HBASE_VERSION 1.2.1
RUN apt-get update
RUN apt-get -y install supervisor python-pip
RUN pip install supervisor-stdout

WORKDIR /opt
RUN curl -O http://ftp.wayne.edu/apache/hbase/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz
RUN tar -zvxf hbase-${HBASE_VERSION}-bin.tar.gz
RUN ln -s hbase-${HBASE_VERSION} hbase

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY hbase-site.xml /opt/hbase-${HBASE_VERSION}/conf/hbase-site.xml
RUN mkdir -p /data/hbase /data/zookeeper

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $PATH:/opt/hbase-${HBASE_VERSION}/bin

# Zookeeper port
EXPOSE 2181 

# REST port
EXPOSE 8080

# Master port
EXPOSE 16000

# Master info port
EXPOSE 16010

# Regionserver port
EXPOSE 16020

# Regionserver info port
EXPOSE 16030

VOLUME /data/hbase
VOLUME /data/zookeeper

CMD ["/usr/bin/supervisord"]
