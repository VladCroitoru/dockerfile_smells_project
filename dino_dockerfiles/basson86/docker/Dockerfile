FROM sequenceiq/hadoop-docker:2.5.1
MAINTAINER Yanif Ahmad <yanif@jhu.edu>

### Spark setup
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.1.0-bin-hadoop2.4.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-1.1.0-bin-hadoop2.4 spark
RUN mkdir /usr/local/spark/yarn-remote-client
ADD yarn-remote-client /home/bdslss-tyr/spark/yarn-remote-client

RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put /home/bdslss-tyr/spark-1.1.0-bin-hadoop2.4/lib /spark

ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV SPARK_JAR hdfs:///spark/spark-assembly-1.1.0-hadoop2.4.0.jar
ENV SPARK_HOME /home/bdslss-tyr/spark
#ENV HADOOP_USER_NAME hdfs
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin

### Python and utilities setup
ENV PATH $PATH:/opt/anaconda/bin
RUN yum update -y && yum install -y wget bzip2 screen
RUN echo 'export PATH=/opt/anaconda/bin:$PATH' > /etc/profile.d/conda.sh
RUN ( echo "=======================" ) && \
    ( echo "Installing Python      " ) && \
    ( echo "=======================" ) && \
    wget --quiet http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh && \
    /bin/bash /Miniconda-latest-Linux-x86_64.sh -b -p /opt/anaconda && \
    rm Miniconda-latest-Linux-x86_64.sh && \
    test -f /opt/anaconda/bin/conda && \
    conda install --yes pip
    conda install --yes numpy
    conda install --yes scipy
    conda install --yes matplotlib
    conda install --yes ipython
    conda install --yes scikit-learn
    conda install --yes scikit-imag	
    conda install --yes pandas
    conda install --yes requests
    conda install --yes h5py

CMD ["/etc/bootstrap.sh", "-d"]
