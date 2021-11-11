FROM oliverkenyon/spark_base:latest

RUN mkdir /tmp/spark-events/
WORKDIR /usr/local/spark

COPY run-worker.sh /run-worker.sh
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY conf-hadoop/* /usr/local/hadoop/etc/hadoop/
RUN mkdir -p $HADOOP_HOME/hadoop_data/hdfs/datanode

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
