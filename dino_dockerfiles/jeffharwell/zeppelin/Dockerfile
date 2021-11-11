FROM gcr.io/google-containers/zeppelin:v0.5.6_v1
MAINTAINER Jeff Harwell <jeff.harwell@gmail.com>

## This is, of course, non-ideal.
## If I had the dockerfile for the GCR image I would do this differently
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

## Get the new version of Zeppelin
## untar it
## back up the GCR config
## delete the old version
## install the new version
## copy the config into the new version
## cleanup
RUN wget http://ftp.wayne.edu/apache/zeppelin/zeppelin-0.8.0/zeppelin-0.8.0-bin-all.tgz && \
    tar -xvf ./zeppelin-0.8.0-bin-all.tgz && \
    mkdir /config_backup && \
    cp /opt/zeppelin/conf/* /config_backup && \
    mkdir /run_backup && \
    cp /opt/zeppelin/bin/* /run_backup && \
    rm -fr /opt/zeppelin && \
    mv ./zeppelin-0.8.0-bin-all /opt/zeppelin && \
    ls /config_backup/ && \
    cp /config_backup/zeppelin-env.sh /opt/zeppelin/conf/ && \
    cp /config_backup/log4j.properties /opt/zeppelin/conf/ && \
    cp /run_backup/docker-zeppelin.sh /opt/zeppelin/bin/ && \
    rm -fr /config_backup && \
    rm -fr /run_backup && \
    rm ./zeppelin-0.8.0-bin-all.tgz && \
    rm -rf /tmp/* /var/tmp/*
RUN wget http://ftp.wayne.edu/apache/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz && \
##RUN wget https://archive.apache.org/dist/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz && \
    tar -xvf ./spark-2.3.2-bin-hadoop2.7.tgz && \
    mkdir /config_backup && \
    cp /opt/spark/conf/* /config_backup && \
    cp /opt/spark/lib/gcs-connector-latest-hadoop2.jar /config_backup && \
    rm -fr /opt/spark-1.5.2-bin-hadoop2.6 && \
    rm /opt/spark && \
    mv ./spark-2.3.2-bin-hadoop2.7 /opt/ && \
    ln -s /opt/spark-2.3.2-bin-hadoop2.7 /opt/spark && \
    cp /config_backup/core-site.xml /opt/spark/conf && \
    cp /config_backup/log4j.properties /opt/spark/conf && \
    cp /config_backup/spark-defaults.conf /opt/spark/conf && \
    cp /config_backup/gcs-connector-latest-hadoop2.jar /opt/spark/lib && \
    rm -fr /config_backup && \
    rm ./spark-2.3.2-bin-hadoop2.7.tgz
