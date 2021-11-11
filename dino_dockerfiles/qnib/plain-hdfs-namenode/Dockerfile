FROM qnib/plain-hadoop

ENV HADOOP_DFS_REPLICATION=1 \
    HADOOP_HDFS_NAMENODE_PORT=8020 \
    HADOOP_HDFS_NAMENODE_URI=tasks.namenode
VOLUME ["/data/hadoopdata/"]
COPY opt/qnib/hdfs/namenode/bin/start.sh /opt/qnib/hdfs/namenode/bin/
COPY opt/qnib/entry/*.sh /opt/qnib/entry/
CMD ["/opt/qnib/hdfs/namenode/bin/start.sh"]
