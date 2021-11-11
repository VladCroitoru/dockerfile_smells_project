FROM gliderlabs/alpine:3.6
# Ensure the freshest base image, update the RPM content associated with the base image. This reduces the exposed attack surface
RUN apk --update add --no-cache  \
# https://stackoverflow.com/questions/44576787/apache-spark-startup-error-on-alpine-linux-docker/44577216#44577216
        coreutils \
        bash \        
# https://github.com/gliderlabs/docker-alpine/issues/292
        wget \
        tar \
        procps \
        # Java Open JDK 8
        openjdk8
                                                                             
# Apache Spark version 2.2.0
ENV SPARKVERSION spark-2.2.0-bin-hadoop2.7

RUN mkdir /spark-jobs && mkdir /opt \
    && wget http://d3kbcqa49mib13.cloudfront.net/${SPARKVERSION}.tgz \
    # Untar Spark, in /opt default to hadoop 2.4 version, and remove extracted file
    && tar -xzf ${SPARKVERSION}.tgz -C /opt/ && rm ${SPARKVERSION}.tgz \   
    # Soft link to version of Spark                                                                          
    && ln -s /opt/${SPARKVERSION} /opt/spark 

# Set up Spark environment
# Options for Standalone Spark Cluster
RUN echo "SPARK_WORKER_MEMORY=2g" >> /opt/spark/conf/spark-env.sh \
    && echo "SPARK_EXECUTOR_INSTANCES=1" >> /opt/spark/conf/spark-env.sh

COPY bin/start-two-nodes-cluster.sh /opt/start-two-nodes-cluster.sh

RUN chmod +x /opt/start-two-nodes-cluster.sh

COPY ["spark-jobs/spark-jobs-poc-1.0.jar","spark-jobs/words-example.txt","/spark-jobs/"]

RUN chmod +x /spark-jobs/spark-jobs-poc-1.0.jar

COPY bin/dropbear-setup-startup.sh /opt/dropbear-setup-startup.sh

RUN chmod +x /opt/dropbear-setup-startup.sh

# Single node cluster
# CMD ["/opt/start-two-nodes-cluster.sh"]

# Multi-node cluster with Dropbear server (SSH) running on master node 
CMD echo $(hostname) && if [[ $(hostname) = "scale1.docker" ]] ; then /opt/spark/sbin/start-master.sh && /opt/dropbear-setup-startup.sh && tail -f /opt/spark/logs/spark* ; else ping -c 2 scale1.docker && /opt/spark/sbin/start-slave.sh spark://scale1.docker:7077 && tail -f /opt/spark/logs/spark*  ;  fi
