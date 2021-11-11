FROM centos:7
MAINTAINER cjonesy

#-------------------------------------------------------------------------------
# Install dependencies
#-------------------------------------------------------------------------------
RUN yum install -y \
        python-setuptools python-devel gcc wget libiffi-devel openssl-devel \
        postgresql-devel libxml2 libxml2-devel libxslt libxslt-devel which zip && \
    yum clean all && \
    easy_install pip && \
    pip install --upgrade setuptools pip && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/America/Chicago /etc/localtime


#-------------------------------------------------------------------------------
# Install Java
#-------------------------------------------------------------------------------
ENV JAVA_URL="http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.rpm"
ENV JAVA_HOME=/usr/java/default

RUN wget --no-cookies --no-check-certificate \
         --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" \
         "$JAVA_URL" \
         -O /tmp/jdk-linux-x64.rpm && \
         yum localinstall -y /tmp/jdk-linux-x64.rpm && \
         rm /tmp/jdk-linux-x64.rpm


#-------------------------------------------------------------------------------
# Install Hadoop
#-------------------------------------------------------------------------------
ENV HADOOP_VERSION=2.6.5
ENV HADOOP_HOME=/usr/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

RUN curl -L --retry 3 \
    "http://apache.mirrors.lucidnetworks.net/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz" | \
    gunzip | tar x -C /usr/ && \
    ln -s /usr/hadoop-$HADOOP_VERSION $HADOOP_HOME && \
    rm -rf $HADOOP_HOME/share/doc


#-------------------------------------------------------------------------------
# Install Spark
#-------------------------------------------------------------------------------
ENV SPARK_VERSION=2.3.1
ENV SPARK_HOME=/usr/spark
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$SPARK_HOME/python/lib/
ENV PYSPARK_PYTHON=/usr/bin/python

RUN curl -L --retry 3 \
    "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-without-hadoop.tgz" | \
    gunzip | tar x -C /usr/ && \
    ln -s /usr/spark-$SPARK_VERSION-bin-without-hadoop $SPARK_HOME && \
    rm -rf $SPARK_HOME/examples


#-------------------------------------------------------------------------------
# Entry
#-------------------------------------------------------------------------------
COPY ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["sh"]
