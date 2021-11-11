# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.9.22
MAINTAINER harry.kurniawan@bridestory.com

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install java
RUN echo "[+] INSTALLING JAVA, GIT AND DEPENDENCIES" && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer git

# Set environment Variable
ENV PIO_VERSION 0.12.0
ENV SCALA_VERSION 2.11.11
ENV SPARK_VERSION 2.1.1
ENV ELASTICSEARCH_VERSION 5.5.2
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV PIO_HOME /pio-${PIO_VERSION}
ENV SPARK_HOME /spark-${SPARK_VERSION}
ENV PATH ${PIO_HOME}/bin:${PATH}


# Install prediction IO
RUN echo "[+] PULLING PREDICTIONIO VER ${PIO_VERSION} FROM GITHUB AND INSTALL IT TO ${PIO_HOME}" && \
    cd /tmp && git clone https://github.com/apache/incubator-predictionio.git pio && \
    cd pio && git checkout release/${PIO_VERSION} && \
    echo "COMMAND: ./make-distribution.sh -Dscala.version=${SCALA_VERSION} -Dspark.version=${SPARK_VERSION} -Delasticsearch.version=${ELASTICSEARCH_VERSION}" && \
    ./make-distribution.sh -Dscala.version=${SCALA_VERSION} -Dspark.version=${SPARK_VERSION} -Delasticsearch.version=${ELASTICSEARCH_VERSION} && \
    tar xvzf PredictionIO-${PIO_VERSION}-incubating.tar.gz && \
    mv PredictionIO-${PIO_VERSION}-incubating ${PIO_HOME}

# Get mysql Connector
RUN echo "[+] DOWNLOAD MYSQL CONNECTOR JAR AND MOVE IT TO ${PIO_HOME}/lib" && \
    cd /tmp && curl -O http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.41/mysql-connector-java-5.1.41.jar && \
    mv mysql-connector-java-5.1.41.jar $PIO_HOME/lib

# Install spark
RUN echo "[+] DOWNLOAD SPARK VER ${SPARK_VERSION} AND INSTALL IT TO ${SPARK_HOME}" && \
    cd /tmp && curl -O https://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz && \
    tar xvzf spark-${SPARK_VERSION}-bin-hadoop2.7.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop2.7 ${SPARK_HOME}

# Add pio-env.sh
ADD files/pio-env.sh ${PIO_HOME}/conf/pio-env.sh

# clean up apt
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* /var/tmp/* && \
    rm -rf /var/cache/oracle-jdk8-installer


# Define default command.
CMD ["bash"]