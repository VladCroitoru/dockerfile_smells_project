FROM paladintyrion/mesos-java:latest

# Update the base ubuntu image with dependencies needed for Spark
RUN apt-get install -y python libnss3 curl && \
    apt-get autoremove -y

RUN mkdir /opt/spark && \
    curl http://archive.apache.org/dist/spark/spark-2.0.1/spark-2.0.1-bin-hadoop2.7.tgz \
    | tar --strip-components=1 -xzC /opt/spark && \
    rm -rf /opt/spark/examples

ENV SPARK_HOME /opt/spark
ENV PATH $PATH:/opt/spark/bin
ENV MESOS_NATIVE_JAVA_LIBRARY /usr/local/lib/libmesos.so
ENV SPARK_EXECUTOR_URI http://archive.apache.org/dist/spark/spark-2.0.1/spark-2.0.1-bin-hadoop2.7.tgz

EXPOSE 4040 8080
