FROM sequenceiq/hadoop-ubuntu:2.6.0
MAINTAINER anant.asty@gmail.com

RUN apt-get update && apt-get install -y libncurses-dev \
                       python-pip \
                       python-software-properties \
                       python-lxml \
                       python-dev

RUN pip install "jupyter"
RUN pip install supervisor

ADD requirements.pip requirements.pip
RUN pip install -r requirements.pip

# RUN apt-get install -y software-properties-common
# RUN add-apt-repository -y ppa:webupd8team/java && apt-get update
# RUN apt-get install -y oracle-java8-installer
RUN wget http://www.scala-lang.org/files/archive/scala-2.10.4.deb
RUN  dpkg -i scala-2.10.4.deb ||  apt-get -f install -y &&  dpkg -i scala-2.10.4.deb

RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.6.1-bin-hadoop2.6.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-1.6.1-bin-hadoop2.6 spark
ENV SPARK_HOME /usr/local/spark
RUN mkdir $SPARK_HOME/yarn-remote-client
ADD yarn-remote-client $SPARK_HOME/yarn-remote-client

RUN apt-get install -y openssh-server \
                       supervisor
                       
ADD supervisord.conf /etc/supervisor/supervisord.conf
COPY bootstrap.sh /etc/bootstrap.sh
RUN chown root.root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh
RUN mkdir -p /home/root
ADD kafka_assembly.jar /usr/local/spark/lib/kafka_assembly.jar
ADD spark-mongodb_2.10-0.11.2.jar /usr/local/spark/lib/mongo_spark.jar
ADD elasticsearch-hadoop-2.3.2.jar /usr/local/spark/lib/elasticsearch-hadoop-2.3.2.jar
ADD pyspark-elastic-0.4.2.jar /usr/local/spark/lib/pyspark-elastic-0.4.2.jar
ADD pyspark_elastic-0.2.0-py2.7.egg /usr/local/spark/lib/pyspark_elastic-0.2.0-py2.7.egg
ADD start_ipython.sh /var/start_ipython.sh
RUN pip install pymongo

RUN echo "BOOTSTRAP IS $BOOTSTRAP HADOOP_PREFIX :: $HADOOP_PREFIX"
# RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put $SPARK_HOME-1.6.1-bin-hadoop2.6/lib /spark
# ENV=YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
# ENV=PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin

ENTRYPOINT ["/etc/bootstrap.sh"]


