#
# This docker image is just for development and testing purpose - please do NOT use on production
#

# Pull Base Image
FROM ubuntu:16.04

# Set Maintainer Details
MAINTAINER Dustin Hiatt <dustin.hiatt@workiva.com>

RUN apt-get update \
    && apt-get -y install software-properties-common \
    && add-apt-repository -y ppa:webupd8team/java \
    && echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
    && echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections \
    && apt-get update \
    && apt-get -y install oracle-java8-installer

# Set Environment Variables
ENV PRESTO_VERSION=0.189 PRESTO_HOME=/presto BASE_URL=https://repo1.maven.org/maven2/com/facebook/presto CONFIG_HOME=/presto-server-0.189/etc CATALOG_HOME=/presto-server-0.189/etc/catalog

# Download Presto
RUN apt-get update \
	&& apt-get install -y python \
	&& wget ${BASE_URL}/presto-server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz \
		${BASE_URL}/presto-cli/${PRESTO_VERSION}/presto-cli-${PRESTO_VERSION}-executable.jar \
		${BASE_URL}/presto-jdbc/${PRESTO_VERSION}/presto-jdbc-${PRESTO_VERSION}.jar \
		${BASE_URL}/presto-verifier/${PRESTO_VERSION}/presto-verifier-${PRESTO_VERSION}-executable.jar \
		${BASE_URL}/presto-benchmark-driver/${PRESTO_VERSION}/presto-benchmark-driver-${PRESTO_VERSION}-executable.jar \
	&& rm -rf /var/lib/apt/lists/*

# Install Presto
RUN chmod +x presto-*executable.jar \
	&& tar zxvf presto-server-${PRESTO_VERSION}.tar.gz \
	&& ln -s presto-server-${PRESTO_VERSION} presto \
	&& mv *.jar presto/. \
	&& cd presto \
	&& ln -s presto-cli-${PRESTO_VERSION}-executable.jar presto \
	&& ln -s presto-verifier-${PRESTO_VERSION}-executable.jar verifier \
	&& ln -s presto-benchmark-driver-${PRESTO_VERSION}-executable.jar benchmark-driver \
	&& wget -P plugin/hive-hadoop2/ https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/hive-json-serde/hive-json-serde-0.2.jar \
	&& cd -

# Setup config
RUN mkdir -p $CONFIG_HOME \
    && echo "coordinator=true" > $CONFIG_HOME/config.properties \
    && echo "node-scheduler.include-coordinator=true" \
    && echo "query.max-memory=5GB" >> $CONFIG_HOME/config.properties \
    && echo "query.max-memory-per-node=1GB" >> $CONFIG_HOME/config.properties \
    && echo "http-server.http.port=8080" >> $CONFIG_HOME/config.properties \
    && echo "discover-server.enabled=true" \
    && echo "discovery.uri=http://localhost:8080" >> $CONFIG_HOME/config.properties

RUN echo "-server" > $CONFIG_HOME/jvm.config \
    && echo "-Xmx2G" >> $CONFIG_HOME/jvm.config \
    && echo "-XX:+UseG1GC" >> $CONFIG_HOME/jvm.config \
    && echo "-XX:G1HeapRegionSize=32M" >> $CONFIG_HOME/jvm.config \
    && echo "-XX:+UseGCOverheadLimit" >> $CONFIG_HOME/jvm.config \
    && echo "-XX:+ExplicitGCInvokesConcurrent" >> $CONFIG_HOME/jvm.config \
    && echo "-XX:+HeapDumpOnOutOfMemoryError" >> $CONFIG_HOME/jvm.config \
    && echo "-XX:OnOutOfMemoryError=kill -9 0" >> $CONFIG_HOME/jvm.config

RUN echo "node.environment=production" > $CONFIG_HOME/node.properties \
    && echo "node.id=7fb47073-3398-42f2-b51a-ddce39550739" >> $CONFIG_HOME/node.properties \
    && echo "node.data-dir=/presto/data" >> $CONFIG_HOME/node.properties

RUN echo "com.facebook.presto=INFO" > $CONFIG_HOME/log.properties

RUN mkdir -p $CATALOG_HOME \
    && echo "connector.name=jmx" > $CATALOG_HOME/jmx.properties \
    && echo "connector.name=memory" > $CATALOG_HOME/memory.properties \
    && echo "memory.max-data-per-node=128MB" >> $CATALOG_HOME/memory.properties

WORKDIR $PRESTO_HOME
VOLUME ["$PRESTO_HOME/etc", "$PRESTO_HOME/data"]

EXPOSE 8080

ENTRYPOINT ["./bin/launcher", "run"]
