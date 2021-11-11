FROM centos:7

#-------------------------------------------------------------------------------
# Install dependencies
#-------------------------------------------------------------------------------
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y \
    python36u \
    python36u-pip \
    python36u-devel \
    python2-pip \
    python-devel \
    gcc \
    wget \
    libiffi-devel \
    openssl-devel \
    postgresql-devel \
    libxml2 \
    libxml2-devel \
    libxslt \
    libxslt-devel \
    zip && \
    yum clean all && \
    /usr/bin/pip2 install --upgrade setuptools pip && \
    /usr/bin/pip3.6 install --upgrade setuptools pip && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/America/Chicago /etc/localtime

#-------------------------------------------------------------------------------
# Install Java
#-------------------------------------------------------------------------------
ARG JAVA_VERSION=1.8.0
RUN yum -y install java-${JAVA_VERSION}-openjdk

#-------------------------------------------------------------------------------
# Install Spark
#-------------------------------------------------------------------------------
ARG SPARK_VERSION=2.4.6
ARG HADOOP_VERSION=2.7
ENV SPARK_HOME=/usr/spark
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$SPARK_HOME/python/lib/
ENV PYSPARK_PYTHON=/usr/bin/python

RUN curl -L --retry 3 \
    "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" | \
    gunzip | tar x -C /usr/ && \
    ln -s /usr/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION $SPARK_HOME && \
    rm -rf $SPARK_HOME/examples

COPY spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf

#-------------------------------------------------------------------------------
# Entry
#-------------------------------------------------------------------------------
COPY ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["sh"]

EXPOSE 8080
EXPOSE 8081
EXPOSE 7077
