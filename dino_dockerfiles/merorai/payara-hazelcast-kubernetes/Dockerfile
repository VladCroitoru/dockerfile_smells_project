FROM openjdk:8-jdk-alpine

ENV PAYARA_PATH /opt/payara

RUN   apk update \                                                                                                                                                                                                                        
 &&   apk add ca-certificates wget \                                                                                                                                                                                                      
 &&   update-ca-certificates && \
 mkdir -p $PAYARA_PATH/lib && \
 adduser -D -h $PAYARA_PATH payara && echo payara:payara | chpasswd && \
 chown -R payara:payara /opt

ENV PAYARA_PKG https://oss.sonatype.org/service/local/artifact/maven/redirect?r=snapshots&g=fish.payara.extras&a=payara-micro&v=5.0.0.174-SNAPSHOT&p=jar
ENV PAYARA_VERSION prerelease
ENV PKG_FILE_NAME payara-micro.jar
ENV PAYAR_LIB_FOLDER  ${PAYARA_PATH}/lib

RUN wget --quiet -O $PAYARA_PATH/$PKG_FILE_NAME $PAYARA_PKG
RUN wget --quiet -O ${PAYARA_PATH}/rest-jcache.war https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/rest-jcache.war?raw=true
RUN wget --quiet -O ${PAYARA_PATH}/hazelcast.xml https://raw.githubusercontent.com/MeroRai/payara-hazelcast-kubernetes/master/hazelcast.xml

RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/hazelcast-kubernetes.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/hazelcast-kubernetes-1.0.0.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/dnsjava.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/dnsjava-2.1.7.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/jackson-annotations.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/jackson-annotations-2.6.0.jar?raw=true 
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/jackson-core.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/jackson-core-2.6.3.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/jackson-databind.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/jackson-databind-2.6.3.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/jackson-dataformat-yaml.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/jackson-dataformat-yaml-2.6.3.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/jackson-module-jaxb-annotations.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/jackson-module-jaxb-annotations-2.6.3.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/jul-to-slf4j.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/jul-to-slf4j-1.7.12.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/kubernetes-client.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/kubernetes-client-1.3.66.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/kubernetes-model.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/kubernetes-model-1.0.40.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/logging-interceptor.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/logging-interceptor-2.7.0.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/okhttp.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/okhttp-2.7.0.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/okhttp-ws.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/okhttp-ws-2.7.0.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/okio.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/okio-1.6.0.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/slf4j-api.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/slf4j-api-1.7.12.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/snakeyaml.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/snakeyaml-1.15.jar?raw=true
RUN wget --quiet -O ${PAYAR_LIB_FOLDER}/validation-api.jar https://github.com/MeroRai/payara-hazelcast-kubernetes/blob/master/lib/validation-api-1.1.0.Final.jar?raw=true

# Default payara ports to expose
EXPOSE 4848 8009 8080 8181

USER payara
WORKDIR $PAYARA_PATH

ENTRYPOINT ["java", "-jar", "payara-micro.jar","--hzconfigfile", "hazelcast.xml", "--deploy", "rest-jcache.war", "--autobindhttp", "--addjars", "lib/", "--name", "payara-micro"]
