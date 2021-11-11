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
    apt-get install -y oracle-java8-installer git unzip && \
    mkdir /pdi

# Set environment Variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV KETTLE_HOME /opt/data-integration
ENV PDI_VERSION 7.1
ENV PDI_BUILD 7.1.0.0-12

# Install pdi 7.1 https://nchc.dl.sourceforge.net/project/pentaho/Data%20Integration/7.1/pdi-ce-7.1.0.0-12.zip
RUN echo "[+] PULLING PENTAHO DATA INTEGRATION 7.1" && \
    cd /tmp && wget http://downloads.sourceforge.net/project/pentaho/Data%20Integration/${PDI_VERSION}/pdi-ce-${PDI_BUILD}.zip && \
    unzip pdi-ce-${PDI_BUILD}.zip && rm -rf pdi-ce-${PDI_BUILD}.zip && \
    mv data-integration /opt/ && \
    mkdir -p /opt/data-integration/libext

# Get mysql Connector
RUN echo "[+] DOWNLOAD MYSQL CONNECTOR JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.37/mysql-connector-java-5.1.37.jar && \
    mv mysql-connector-java-5.1.37.jar $KETTLE_HOME/libext

# Get amqp client
RUN echo "[+] DOWNLOAD RABBITMQ JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/com/rabbitmq/amqp-client/4.1.0/amqp-client-4.1.0.jar && \
    mv amqp-client-4.1.0.jar $KETTLE_HOME/libext

# Get jedis client
RUN echo "[+] DOWNLOAD JEDIS JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/redis/clients/jedis/2.9.0/jedis-2.9.0.jar && \
    mv jedis-2.9.0.jar $KETTLE_HOME/libext

# Get geoIP
RUN echo "[+] DOWNLOAD GEOIP JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/com/maxmind/geoip2/geoip2/2.5.0/geoip2-2.5.0.jar && \
    mv geoip2-2.5.0.jar $KETTLE_HOME/libext

# Get Google HTTP Client
RUN echo "[+] DOWNLOAD GOOGLE HTTP CLIENT JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/com/google/http-client/google-http-client/1.21.0/google-http-client-1.21.0.jar && \
    mv google-http-client-1.21.0.jar $KETTLE_HOME/libext

# Get httpclient
RUN echo "[+] DOWNLOAD HTTPCLIENT JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/org/apache/httpcomponents/httpclient/4.0.1/httpclient-4.0.1.jar && \
    mv httpclient-4.0.1.jar $KETTLE_HOME/libext

# Get httpcore
RUN echo "[+] DOWNLOAD HTTPCORE JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.jar && \
    mv httpcore-4.0.1.jar $KETTLE_HOME/libext

# Get JSR
RUN echo "[+] DOWNLOAD JSR JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/com/google/code/findbugs/jsr305/1.3.9/jsr305-1.3.9.jar && \
    mv jsr305-1.3.9.jar $KETTLE_HOME/libext

# Get maxmindDB
RUN echo "[+] DOWNLOAD MAXMIND DB JAR AND MOVE IT TO ${KETTLE_HOME}/libext" && \
    cd /tmp && curl -O http://central.maven.org/maven2/com/maxmind/db/maxmind-db/1.1.0/maxmind-db-1.1.0.jar && \
    mv maxmind-db-1.1.0.jar $KETTLE_HOME/libext

# Get kafka-consumer plugins
RUN echo "[+] DOWNLOAD KAFKA CONSUMER PLUGINS AND MOVE IT TO ${KETTLE_HOME}/plugins" && \
    cd /tmp && curl -L -O https://github.com/RuckusWirelessIL/pentaho-kafka-consumer/releases/download/v1.7/pentaho-kafka-consumer-v1.7.zip && \
    unzip pentaho-kafka-consumer-v1.7.zip && mv pentaho-kafka-consumer $KETTLE_HOME/plugins

# Get kafka-producer plugins
RUN echo "[+] DOWNLOAD KAFKA PRODUCER PLUGINS AND MOVE IT TO ${KETTLE_HOME}/plugins" && \
    cd /tmp && curl -L -O https://github.com/RuckusWirelessIL/pentaho-kafka-producer/releases/download/v1.9/pentaho-kafka-producer-v1.9.zip && \
    unzip pentaho-kafka-producer-v1.9.zip && mv pentaho-kafka-producer $KETTLE_HOME/plugins


# Add launcher properties
ADD files/launcher.properties ${KETTLE_HOME}/launcher/launcher.properties

# clean up apt
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* /var/tmp/* && \
    rm -rf /var/cache/oracle-jdk8-installer


# Define default command.
CMD ["bash"]