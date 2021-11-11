FROM cineca/hadoop:2.5.2
MAINTAINER www.hpc.cineca.it

USER root

# Spark
RUN curl -s http://apache.stu.edu.tw/spark/spark-1.4.1/spark-1.4.1-bin-hadoop2.4.tgz | tar -xz -C /usr/local/
RUN cd /usr/local \
    && ln -s spark-1.4.1-bin-hadoop2.4 spark
RUN mkdir /usr/local/spark/yarn-remote-client
ADD yarn-remote-client /usr/local/spark/yarn-remote-client

RUN service ssh start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && $HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put /usr/local/spark-1.4.1-bin-hadoop2.4/lib /spark

ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV SPARK_JAR hdfs:///spark/spark-assembly-1.4.1-hadoop2.4.0.jar
ENV SPARK_HOME /usr/local/spark
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin
ENV PYTHONPATH $SPARK_HOME/python/:$PYTHONPATH
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip:$PYTHONPATH

RUN pip install pip --upgrade
#RUN pip install "ipython[notebook]"
RUN apt-get install -y python-tk
RUN pip install -U "ipython[notebook]"
RUN pip install -U nltk
RUN pip install pandas

#RUN mkdir /exercises && cd /exercises && git clone https://github.com/gfiameni/course-exercises

RUN mkdir /notebooks
#RUN cp -r /exercises/course-exercises/spark/2015_April/* /notebooks

VOLUME /notebooks
WORKDIR /notebooks


EXPOSE 8888
EXPOSE 8080

CMD /etc/bootstrap.sh && /usr/local/spark/sbin/start-master.sh && IPYTHON_OPTS="notebook --no-browser --ip=0.0.0.0 --port 8888" /usr/local/spark/bin/pyspark