FROM gettyimages/spark:2.1.0-hadoop-2.7

# SciPy
RUN set -ex \
 && buildDeps=' \
    libpython3-dev \
    build-essential \
    pkg-config \
    gfortran \
 ' \
 && apt-get update && apt-get install -y --no-install-recommends \
    $buildDeps \
    ca-certificates \
    wget \
    liblapack-dev \
    libopenblas-dev \
 && packages=' \
    numpy \
    pandasql \
    scipy \
 ' \
 && pip3 install $packages \
 && apt-get purge -y --auto-remove $buildDeps \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Zeppelin
ENV ZEPPELIN_PORT 8080
ENV ZEPPELIN_HOME /usr/zeppelin
ENV ZEPPELIN_CONF_DIR $ZEPPELIN_HOME/conf
ENV ZEPPELIN_NOTEBOOK_DIR $ZEPPELIN_HOME/notebook
ENV ZEPPELIN_COMMIT v0.7.0
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN set -ex \
 && buildDeps=' \
    git \
    bzip2 \
    npm \
 ' \
 && apt-get update && apt-get install -y --no-install-recommends $buildDeps \
 && apt-get install vim -y \
 && curl -sL http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz \
   | gunzip \
   | tar x -C /tmp/ \
 && git clone https://github.com/apache/zeppelin.git /usr/src/zeppelin \
 && cd /usr/src/zeppelin \
 && git checkout -q $ZEPPELIN_COMMIT \
 && dev/change_scala_version.sh "2.11" \
 && MAVEN_OPTS="-Xmx2g -XX:MaxPermSize=1024m" /tmp/apache-maven-3.3.9/bin/mvn --batch-mode package -DskipTests -Pscala-2.11 -Pbuild-distr \
  -pl 'zeppelin-interpreter,zeppelin-zengine,zeppelin-display,spark-dependencies,spark,markdown,angular,shell,hbase,postgresql,jdbc,python,elasticsearch,zeppelin-web,zeppelin-server,zeppelin-distribution' \
 && tar xvf /usr/src/zeppelin/zeppelin-distribution/target/zeppelin*.tar.gz -C /usr/ \
 && mv /usr/zeppelin* $ZEPPELIN_HOME \
 && mkdir -p $ZEPPELIN_HOME/logs \
 && mkdir -p $ZEPPELIN_HOME/run \
 && apt-get purge -y --auto-remove $buildDeps \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /usr/src/zeppelin \
 && rm -rf /root/.m2 \
 && rm -rf /root/.npm \
 && rm -rf /tmp/*
ADD about.json $ZEPPELIN_NOTEBOOK_DIR/2BTRWA9EV/note.json

# Google credentials JSON
COPY google-credentials/ /usr/google-credentials/

# Update conf file
COPY conf/core-site.xml ${SPARK_HOME}/conf/core-site.xml

# Copy BigQuery Connector
COPY lib/spark-bigquery-assembly-0.1.4.jar ${SPARK_HOME}/jars/spark-bigquery-assembly-0.1.4.jar

# Copy Jackson related jars
COPY lib/jackson-core-2.8.6.jar ${SPARK_HOME}/jars/jackson-core-2.8.6.jar

# Copy Google Hadoop Connector
COPY lib/gcs-connector-latest-hadoop2.jar ${SPARK_HOME}/jars/gcs-connector-latest-hadoop2.jar

# Copy AWS Jars
COPY lib/aws-java-sdk-1.7.4.jar ${SPARK_HOME}/jars/aws-java-sdk-1.7.4.jar
COPY lib/hadoop-aws-2.7.1.jar ${SPARK_HOME}/jars/hadoop-aws-2.7.1.jar

# Update Guava
COPY lib/guava-18.0.jar ${SPARK_HOME}/jars/guava-18.0.jar
 
WORKDIR $ZEPPELIN_HOME
CMD ["bin/zeppelin.sh"]