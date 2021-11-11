FROM qnib/plain-hadoop

VOLUME ["/data/hadoop/data/", "/data/hadoop/tmp/"]
COPY opt/qnib/hdfs/datanode/bin/start.sh /opt/qnib/hdfs/datanode/bin/
COPY opt/qnib/entry/*.sh /opt/qnib/entry/
CMD ["/opt/qnib/hdfs/datanode/bin/start.sh"]
