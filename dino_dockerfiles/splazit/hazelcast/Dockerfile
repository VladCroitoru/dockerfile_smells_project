FROM frolvlad/alpine-oraclejdk8:slim
MAINTAINER Hieu Nguyen <hieu.nguyen@ssosol.com>

ENV HZ_VERSION=3.5 \
    HZ_HOME=/hazelcast
    
RUN mkdir $HZ_HOME &&\
    wget -P $HZ_HOME http://repo1.maven.org/maven2/com/hazelcast/hazelcast/$HZ_VERSION/hazelcast-$HZ_VERSION.jar

WORKDIR $HZ_HOME
EXPOSE 5701

# Start hazelcast standalone server.
ENTRYPOINT java -server -cp hazelcast-$HZ_VERSION.jar com.hazelcast.core.server.StartServer
