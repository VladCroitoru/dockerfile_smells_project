FROM qnib/d-java7

ADD etc/apt/sources.list.d/cloudera.list /etc/apt/sources.list.d/
RUN curl -s archive.key http://archive.cloudera.com/cdh5/debian/wheezy/amd64/cdh/archive.key | apt-key add - && \
    apt-get update

# Carve this out for different host types
## JobTracker host
RUN apt-get install -y hadoop-0.20-mapreduce-jobtracker
## NameNode
RUN apt-get install -y hadoop-hdfs-namenode
## ??
RUN apt-get install -y hadoop-0.20-mapreduce-tasktracker hadoop-hdfs-datanode

RUN apt-get install -y wget && \
    wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-init_1.0.0_amd64 && \
    chmod +x /usr/local/bin/dumb-init

#### History
RUN echo "hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-client-jobclient.jar TestDFSIO -write -nrFiles 64 -fileSize 16GB -resFile /tmp/TestDFSIOwrite.txt" >> /root/.bash_history && \
    echo "hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-client-jobclient.jar DistributedFSCheck -resFile /tmp/DistributedFSCheck.txt" >> /root/.bash_history && \
    echo "hadoop fs -ls /" >> /root/.bash_history && \
    echo "hadoop fs -mkdir /\${HOSTNAME}" >> /root/.bash_history && \
    echo "hadoop fs -copyFromLocal /etc/hosts /\${HOSTNAME}/" >> /root/.bash_history
## Configure HDFS
RUN mv /etc/hadoop/conf /etc/hadoop/conf.orig
ADD etc/hadoop/*.xml /etc/hadoop/conf/

ENV HADOOP_HDFS_NAMENODE_PORT=8020 \
    HADOOP_DFS_REPLICATION=2
## Startscript - namenode
ADD opt/qnib/hdfs/namenode/bin/start.sh /opt/qnib/hdfs/namenode/bin/
ADD etc/supervisord.d/hdfs-namenode.ini /etc/supervisord.d/
## Startscript - datanode
ADD opt/qnib/hdfs/datanode/bin/start.sh /opt/qnib/hdfs/datanode/bin/
ADD etc/supervisord.d/hdfs-datanode.ini /etc/supervisord.d/
## put me in qnib/d-terminal please
ADD etc/consul-templates/hdfs/core-site.xml.ctmpl \
    etc/consul-templates/hdfs/core-site.xml-INIT.ctmpl \
    /etc/consul-templates/hdfs/
ADD etc/consul.d/hdfs-namenode.json \
    etc/consul.d/hdfs-datanode.json \
    /etc/consul.d/

VOLUME ["/data/hadoopdata/hdfs/"]
