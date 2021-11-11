FROM agileops/centos-javapython:latest

ENV HADOOP_VERSION=2.7.6 \
    HADOOP_HOME=/opt/hadoop \
    SPARK_VERSION=2.3.0 \
    SPARK_HOME=/opt/spark \
    PYTHON_VERSION=3.6 \
    PYSPARK_PYTHON=python${PYTHON_VERSION} \
    BIND_ADDRESS="127.0.0.1" \
    PYSPARK_DRIVER_PYTHON=jupyter \
    PYSPARK_DRIVER_PYTHON_OPTS="notebook --port=8888 --no-browser --ip=*"

# Download and install hadoop+yarn+hdfs
RUN yum install -y which && \
    yum clean all && rm -rf /var/cache/yum && \
    curl http://apache.mirror.iweb.ca/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz > /opt/hadoop-${HADOOP_VERSION}.tar.gz && \
    mkdir ${HADOOP_HOME} && \
    tar xvfp /opt/hadoop-${HADOOP_VERSION}.tar.gz -C ${HADOOP_HOME} --strip-components=1 && \
    rm -fr /opt/hadoop/share/doc/ && \
    rm /opt/hadoop-${HADOOP_VERSION}.tar.gz

# needed to start yarn
RUN yum install -y rsync openssh-server openssh-clients  && \
    yum clean all && rm -rf /var/cache/yum

ADD http://central.maven.org/maven2/org/apache/hadoop/hadoop-streaming/${HADOOP_VERSION}/hadoop-streaming-${HADOOP_VERSION}.jar ${HADOOP_HOME}/hadoop-streaming.jar

# Download and install spark
RUN curl https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-without-hadoop.tgz > /opt/spark-$SPARK_VERSION-bin-without-hadoop.tgz && \
    mkdir ${SPARK_HOME} && \
    tar xvfp ${SPARK_HOME}-${SPARK_VERSION}-bin-without-hadoop.tgz -C ${SPARK_HOME} --strip-components=1 && \
    rm /opt/spark-$SPARK_VERSION-bin-without-hadoop.tgz

# sbins dir of spark and hadoop isn't include in PATH because thereis conflict on excutables names
ENV PATH=${SPARK_HOME}/bin:${PATH}
ENV PATH=${HADOOP_HOME}/bin:${PATH}


# https://spark.apache.org/docs/latest/hadoop-provided.html
RUN echo 'export SPARK_DIST_CLASSPATH=$(hadoop classpath)' >> ${SPARK_HOME}/conf/spark-env.sh && chmod +x ${SPARK_HOME}/conf/spark-env.sh

# ENV PYTHONPATH=${SPARK_HOME}/python:${PYTHONPATH}

# configure pyspark
RUN cd $SPARK_HOME/python &&  python setup.py install

# Set jupyter path
ENV JUPYTER_DATA_DIR=/usr/local/share/jupyter

# requirements for pytrade and flayers
RUN yum install -y --setopt=tsflags=nodocs blas atlas gcc-gfortran swig gcc-c++ mercurial && \
    yum clean all && rm -rf /var/cache/yum

# Install python libraries
COPY requirements.txt /opt/spark/

# RUN # pip install --no-cache-dir pipenv && \
RUN  pip install --no-cache-dir -r ${SPARK_HOME}/requirements.txt
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

RUN mkdir -p $HOME/.config/matplotlib && \
echo 'backend      : Agg' >>  $HOME/.config/matplotlib/matplotlibrc

# As suggested for BigDL tutorials, install ipykernel
# https://github.com/intel-analytics/BigDL/blob/master/docker/BigDL/Dockerfile
RUN python3 -m ipykernel install && \
    jupyter toree install --spark_home=${SPARK_HOME} --interpreters=Scala,SQL --python="ipython3"

# custom dirs :
# /work-dir - working directory
# /work-dir/hadoop - hadoop+hdfs datas like configurations, index, storage blocks
# /work-dir/sparks - hadoop+hdfs datas
RUN mkdir /work-dir /work-dir/hadoop /work-dir/spark
WORKDIR /work-dir

# Install mlboost
RUN cd /work-dir && hg clone https://fraka6@bitbucket.org/fraka6/mlboost
# Configure mlboost paths
ENV PATH=/work-dir/mlboost/mlboost/util:${PATH} \
    PYTHONPATH=/work-dir/mlboost:${PYTHONPATH}

# Volumes are used to persist data
# Path on the local filesystem where the NameNode stores the namespace and transactions logs persistently.
VOLUME /work-dir/hadoop/dfs.name
# Comma separated list of paths on the local filesystem of a DataNode where it should store its blocks.
VOLUME /work-dir/hadoop/dfs.data

# Copy hadoop configs
COPY ./etc/hadoop/*  /opt/hadoop/etc/hadoop/

# HADOOP_OPTS is an env. var. used to configure hadoop's specific java options
ENV NAMENODE_DATA=/work-dir/hadoop/dfs.name \
    DFS_DATA=/work-dir/hadoop/dfs.data
ENV HADOOP_OPTS="-Ddfs.name.dir=${NAMENODE_DATA} -Ddfs.data.dir=${DFS_DATA}"
ENV YARN_CONF_DIR=${HADOOP_HOME}/conf/etc

# Install official hbase lib for python 3
RUN cd /tmp/ && \
    curl http://apache.forsale.plus/hbase/2.0.0/hbase-2.0.0-src.tar.gz > hbase-2.0.0-src.tar.gz && \
    mkdir /tmp/hbase &&  \
    tar xvfp hbase-2.0.0-src.tar.gz --strip-components=1 -C /tmp/hbase  && \
    curl http://apache.mirror.globo.tech/thrift/0.11.0/thrift-0.11.0.tar.gz > thrift-0.11.0.tar.gz && \
    mkdir /tmp/thrift && \
    tar xvfp thrift-0.11.0.tar.gz --strip-components=1 -C /tmp/thrift && \
    yum install -y make && \
    cd /tmp/thrift && \
    ./configure && make install && \
    cd lib/py && python3 setup.py install && \
    mkdir /opt/hbase-python && \
    cd /tmp/hbase && \
    thrift --out /opt/hbase-python --gen py ./hbase-thrift/src/main/resources/org/apache/hadoop/hbase/thrift2/hbase.thrift && \
    rm -R /tmp/hbase /tmp/thrift && \
    rm /tmp/hbase-2.0.0-src.tar.gz /tmp/thrift-0.11.0.tar.gz

ENV PYTHONPATH=/opt/hbase-python:$PYTHONPATH

RUN pip install happybase==1.1.*

COPY ./bin/* /usr/bin/

# Hdfs ports
EXPOSE 50010 50020 50070 50075 50090 8020 9000
# Mapred ports
EXPOSE 10020 19888
# Yarn ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088
# ^-- taken from https://github.com/sequenceiq/hadoop-docker/blob/master/Dockerfile
# Jupyter port
EXPOSE 8888

# https://jupyter-notebook.readthedocs.io/en/latest/public_server.html#docker-cmd
ENTRYPOINT ["/usr/bin/tini", "-g", "--"]

CMD jupyter notebook --port=8888 --no-browser --ip=0.0.0.0
