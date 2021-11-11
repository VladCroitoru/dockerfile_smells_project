FROM gettyimages/spark:latest
ADD requirements.txt ${SPARK_HOME}
ADD direct_stream.py ${SPARK_HOME}/python
ADD kafka_producer.py ${SPARK_HOME}/python
ADD log4j.properties ${SPARK_HOME}/conf
ADD lib ${SPARK_HOME}/jars
RUN pip install -r requirements.txt

#./bin/spark-submit --jars ./jars/spark-streaming-kafka-0-8-assembly_2.11-2.1.0-SNAPSHOT.jar python/direct_stream.py kafka:9092 provesense.inbound
