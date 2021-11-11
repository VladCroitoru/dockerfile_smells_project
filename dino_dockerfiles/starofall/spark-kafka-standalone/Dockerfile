FROM starofall/spark-standalone

RUN curl -s http://www-eu.apache.org/dist/kafka/0.8.2.2/kafka_2.10-0.8.2.2.tgz | tar -xz -C /tmp/
RUN ln -s /tmp/kafka_2.10-0.8.2.2 /kafka

# Expose ZooKeeper and Kafka
EXPOSE 2181 9092

# Start everything
CMD /spark/sbin/start-master.sh -h ${HOSTNAME} && \
	/spark/sbin/start-slave.sh -h ${HOSTNAME} -d /spark/work -p 9001 --webui-port 8081 spark://${HOSTNAME}:7077 && \
	/kafka/bin/zookeeper-server-start.sh /kafka/config/zookeeper.properties & \
	/kafka/bin/kafka-server-start.sh /kafka/config/server.properties
