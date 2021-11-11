FROM openjdk:11-jre
LABEL maintainer = "Derrick.Oswald@9code.ch"

# Hadoop

# Version
ENV HADOOP_VERSION=3.2.1

# Set home
ENV HADOOP_HOME=/usr/local/hadoop-$HADOOP_VERSION

# Install dependencies
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install --yes --quiet --no-install-recommends apt-utils netcat procps \
  && apt-get clean \
  && rm --recursive --force /var/lib/apt/lists/*

# Install Hadoop
RUN mkdir --parents "${HADOOP_HOME}" \
  && export ARCHIVE=hadoop-$HADOOP_VERSION.tar.gz \
  && export DOWNLOAD_PATH=hadoop-$HADOOP_VERSION/$ARCHIVE \
  && curl --silent --show-error --location https://archive.apache.org/dist/hadoop/common/$DOWNLOAD_PATH | \
    tar --extract --gunzip --directory=$HADOOP_HOME --strip-components 1 \
  && rm --recursive --force $ARCHIVE

# HDFS volume
VOLUME /opt/hdfs

# Set paths
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop \
  HADOOP_LIBEXEC_DIR=$HADOOP_HOME/libexec \
  PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Copy and fix configuration files
COPY /conf/*.xml $HADOOP_CONF_DIR/
RUN sed --in-place "s/hadoop-daemons.sh/hadoop-daemon.sh/g" $HADOOP_HOME/sbin/start-dfs.sh \
  && sed --in-place "s/hadoop-daemons.sh/hadoop-daemon.sh/g" $HADOOP_HOME/sbin/stop-dfs.sh \
  && sed --in-place "s/# export JAVA_HOME=/export JAVA_HOME=\/usr\/local\/openjdk-11/g" $HADOOP_CONF_DIR/hadoop-env.sh

# Hapdoop ports 3.0.0, see http://hadoop.apache.org/docs/r3.0.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml
# nfs.server.port
EXPOSE 2049
# nfs.mountd.port
EXPOSE 4242
# dfs.federation.router.admin-address
EXPOSE 8111
# dfs.journalnode.rpc-address
EXPOSE 8485
# dfs.journalnode.http-address
EXPOSE 8480
# dfs.journalnode.https-address
EXPOSE 8481
# dfs.federation.router.rpc-address
EXPOSE 8888
# dfs.namenode.rpc-address
EXPOSE 9820
# dfs.namenode.http-address
EXPOSE 9870
# dfs.namenode.https-address
EXPOSE 9871
# dfs.datanode.http.address
EXPOSE 9864
# dfs.datanode.https.address
EXPOSE 9865
# dfs.datanode.address
EXPOSE 9866
# dfs.datanode.ipc.address
EXPOSE 9867
# dfs.namenode.secondary.http-address
EXPOSE 9868
# dfs.namenode.secondary.https-address
EXPOSE 9869
# dfs.federation.router.http-address
EXPOSE 50071
# dfs.federation.router.https-address
EXPOSE 50072
# dfs.namenode.backup.address
EXPOSE 50100
# dfs.namenode.backup.http-address
EXPOSE 50105
# datanode.https.port
EXPOSE 50475

# Mapreduce ports, see https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml
# mapreduce.jobhistory.address
EXPOSE 10020
# mapreduce.shuffle.port
EXPOSE 13562
# mapreduce.jobhistory.webapp.address
EXPOSE 19888
# mapreduce.jobhistory.webapp.https.address
EXPOSE 19890

# Fix environment for other users
RUN echo "export HADOOP_HOME=$HADOOP_HOME" >> /etc/bash.bashrc \
  && echo 'export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:/opt/util/bin'>> /etc/bash.bashrc

# Spark

# Version
ENV SPARK_VERSION=3.0.1

# set up TTY
ENV TERM=xterm-256color

# Set home
ENV SPARK_HOME=/usr/local/spark-$SPARK_VERSION

# Install dependencies
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install --yes --quiet --no-install-recommends \
    python python3 vim sqlite3 r-base p7zip net-tools ftp libncurses5 libtinfo5 ssh \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install GridLAB-D
COPY gridlabd_4.0.0-1_amd64.deb /opt/util/gridlabd_4.0.0-1_amd64.deb
RUN dpkg --install /opt/util/gridlabd_4.0.0-1_amd64.deb \
  && rm /opt/util/gridlabd_4.0.0-1_amd64.deb

# Install Spark
RUN mkdir --parents "${SPARK_HOME}" \
  && export ARCHIVE=spark-$SPARK_VERSION-bin-hadoop3.2.tgz \
  && export DOWNLOAD_PATH=dist/spark/spark-$SPARK_VERSION/$ARCHIVE \
  && curl --silent --show-error --location https://www-eu.apache.org/$DOWNLOAD_PATH | \
    tar --extract --gzip --directory=$SPARK_HOME --strip-components 1 \
  && sed 's/log4j.rootCategory=INFO/log4j.rootCategory=WARN/g' $SPARK_HOME/conf/log4j.properties.template >$SPARK_HOME/conf/log4j.properties \
  && echo '' >> $SPARK_HOME/conf/log4j.properties \
  && echo '# quiet the apache logs' >> $SPARK_HOME/conf/log4j.properties \
  && echo 'log4j.logger.org.apache=ERROR' >> $SPARK_HOME/conf/log4j.properties \
  && rm --recursive --force $ARCHIVE
COPY spark-env.sh $SPARK_HOME/conf/spark-env.sh
ENV PATH=$PATH:$SPARK_HOME/bin

# Remove duplicate SLF4J bindings
RUN mv /usr/local/spark-$SPARK_VERSION/jars/slf4j-log4j12-1.7.30.jar /usr/local/spark-$SPARK_VERSION/jars/slf4j-log4j12-1.7.30.jar.hide

# fix missing ps command
RUN apt-get update \
&& apt-get install -yq --reinstall procps

# Spark ports, see https://spark.apache.org/docs/latest/security.html#configuring-ports-for-network-security
# Cluster Manager Web UI
EXPOSE 4040
# Standalone Master REST port (spark.master.rest.port)
EXPOSE 6066
# Driver to Standalone Master
EXPOSE 7077
# Standalone Master Web UI
EXPOSE 8080
# Standalone Worker Web UI
EXPOSE 8081
# Yarn Resource Manager
EXPOSE 8088
# Rstudio
EXPOSE 8787
# History Server
EXPOSE 18080

# Hadoop ports 2.x, see https://hadoop.apache.org/docs/r2.7.6/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml
# ToDo: are these still needed?
# DFS Namenode IPC
EXPOSE 8020
# DFS Datanode data transfer
EXPOSE 50010
# DFS Datanode IPC
EXPOSE 50020
# DFS Namenode Web UI
EXPOSE 50070
# DFS Datanode Web UI
EXPOSE 50075
# DFS Secondary Namenode Web UI
EXPOSE 50090
# DFS Backup Node data transfer
EXPOSE 50100
# DFS Backup Node Web UI
EXPOSE 50105

# Copy start scripts
COPY start-hadoop /opt/util/bin/start-hadoop
COPY start-hadoop-namenode /opt/util/bin/start-hadoop-namenode
COPY start-hadoop-datanode /opt/util/bin/start-hadoop-datanode
COPY start-spark /opt/util/bin/start-spark
ENV PATH=$PATH:/opt/util/bin

# Set up keys
RUN cat /dev/zero | ssh-keygen -q -N ""
RUN ln -s /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

# Fix Java native library path
# avoid WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
COPY spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf
RUN ldconfig

# Fix environment for other users
RUN echo "export SPARK_HOME=$SPARK_HOME" >> /etc/bash.bashrc \
  && echo "export JAVA_HOME=/usr/local/openjdk-11" >> /etc/bash.bashrc \
  && echo "export PATH=$PATH:$SPARK_HOME/bin" >> /etc/bash.bashrc \
  && echo "alias ll='ls -alF --color=auto'" >> /etc/bash.bashrc

# Fix vim's stupid and really annoying "visual mode"
RUN echo "set mouse-=a" > /root/.vimrc
