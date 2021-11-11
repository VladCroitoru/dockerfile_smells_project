FROM python:3.5

# http://blog.stuart.axelbrooke.com/python-3-on-spark-return-of-the-pythonhashseed
ENV PYTHONHASHSEED 0
ENV PYTHONIOENCODING UTF-8
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# JAVA
ARG JAVA_MAJOR_VERSION=8
ARG JAVA_UPDATE_VERSION=112
ARG JAVA_BUILD_NUMBER=15
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}

ENV PATH $PATH:$JAVA_HOME/bin
RUN curl -sL --retry 3 --insecure \
  --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
  "http://download.oracle.com/otn-pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/server-jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \
  | gunzip \
  | tar x -C /usr/ \
  && ln -s $JAVA_HOME /usr/java \
  && rm -rf $JAVA_HOME/man

# HADOOP
ENV HADOOP_VERSION 2.7.3
ENV HADOOP_HOME /usr/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH $PATH:$HADOOP_HOME/bin
RUN curl -sL --retry 3 \
  "http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz" \
  | gunzip \
  | tar -x -C /usr/ \
 && rm -rf $HADOOP_HOME/share/doc \
 && chown -R root:root $HADOOP_HOME

# SPARK
ENV SPARK_VERSION 2.1.1
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
ENV PATH $PATH:${SPARK_HOME}/bin
RUN curl -sL --retry 3 \
  "http://d3kbcqa49mib13.cloudfront.net/${SPARK_PACKAGE}.tgz" \
  | gunzip \
  | tar x -C /usr/ \
 && mv /usr/$SPARK_PACKAGE $SPARK_HOME \
 && chown -R root:root $SPARK_HOME

# ANACONDA 3

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH /opt/conda/bin:$PATH

# Install XGBoost library
RUN apt-get update --fix-missing && apt-get install -y gfortran libatlas-base-dev gfortran pkg-config \
            libfreetype6-dev libxft-dev libpng-dev libhdf5-serial-dev g++ \
            make patch lib32ncurses5-dev

USER root

# install gcc with openmp support in conda
RUN conda install -y gcc

# Install Graphframes
ENV GRAPH_FRAMES_VERSION 0.4.0-spark2.1-s_2.11
ADD ./graphframes-dist/graphframes-${GRAPH_FRAMES_VERSION} $SPARK_HOME/graphframes
RUN cd $SPARK_HOME/graphframes && \
    ./build/sbt "set test in assembly := {}" clean assembly && \
    mv $SPARK_HOME/graphframes/python/graphframes $SPARK_HOME/python/pyspark

# Install Mongo-spark-connector
ENV MONGO_SPARK_CONNECTOR_VERSION 2.0.0
ENV MONGO_SPARK_VERSION 2.10
ADD ./mongo-spark-connector/mongo-spark-connector_${MONGO_SPARK_VERSION}_${MONGO_SPARK_CONNECTOR_VERSION} $SPARK_HOME/org.mongodb.spark
RUN cd $SPARK_HOME/org.mongodb.spark && \
    ./sbt "set test in assembly := {}" clean assembly

# download and build xgboost
RUN cd /opt && \
  git clone --recursive https://github.com/dmlc/xgboost && \
  cd xgboost && \
  make -j4

# set environment var to python package for both python2 and python3
ENV PYTHONPATH /opt/xgboost/python-package
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$SPARK_HOME/python/:$PYTHONPATH

USER $NB_USER

# Install spark-sklearn

RUN pip install spark-sklearn

ENV PYSPARK_SUBMIT_ARGS "--packages graphframes:graphframes:${GRAPH_FRAMES_VERSION},org.mongodb.spark:mongo-spark-connector_${MONGO_SPARK_VERSION}:${MONGO_SPARK_CONNECTOR_VERSION} pyspark-shell"

WORKDIR $SPARK_HOME
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]