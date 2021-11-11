FROM tomcat:8-jre8

MAINTAINER vadyalex <vadyalex at google mail>

ENV SLF4J_VERSION 1.7.12
ENV LOGBACK_VERSION 1.1.3
ENV LOGSTASH_LOGBACK_ENCODER_VERSION 4.4

# logstash-logback-encoder depends on jackson-databind, jackson-annotation and jackson-core libraries
ENV JACKSON_DATABIND_VERSION 2.5.4
ENV JACKSON_ANNOTATIONS_VERSION 2.5.0

ENV CATALINA_HOME /usr/local/tomcat

WORKDIR $CATALINA_HOME/lib

RUN set -x \
	&& cd $CATALINA_HOME/lib \
	&& wget -nv http://central.maven.org/maven2/org/slf4j/jul-to-slf4j/$SLF4J_VERSION/jul-to-slf4j-$SLF4J_VERSION.jar \
	&& wget -nv http://central.maven.org/maven2/org/slf4j/slf4j-api/$SLF4J_VERSION/slf4j-api-$SLF4J_VERSION.jar \
	&& wget -nv http://central.maven.org/maven2/ch/qos/logback/logback-core/$LOGBACK_VERSION/logback-core-$LOGBACK_VERSION.jar \
	&& wget -nv http://central.maven.org/maven2/ch/qos/logback/logback-classic/$LOGBACK_VERSION/logback-classic-$LOGBACK_VERSION.jar \
	&& wget -nv http://central.maven.org/maven2/net/logstash/logback/logstash-logback-encoder/$LOGSTASH_LOGBACK_ENCODER_VERSION/logstash-logback-encoder-$LOGSTASH_LOGBACK_ENCODER_VERSION.jar \
	&& wget -nv http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/$JACKSON_DATABIND_VERSION/jackson-databind-$JACKSON_DATABIND_VERSION.jar \
	&& wget -nv http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/$JACKSON_DATABIND_VERSION/jackson-core-$JACKSON_DATABIND_VERSION.jar \
	&& wget -nv http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/$JACKSON_ANNOTATIONS_VERSION/jackson-annotations-$JACKSON_ANNOTATIONS_VERSION.jar \
	&& echo "export CLASSPATH=$CATALINA_HOME/lib/jul-to-slf4j-$SLF4J_VERSION.jar:$CATALINA_HOME/lib/slf4j-api-$SLF4J_VERSION.jar:$CATALINA_HOME/lib/logback-classic-$LOGBACK_VERSION.jar:$CATALINA_HOME/lib/logback-core-$LOGBACK_VERSION.jar:$CATALINA_HOME/conf/logback/:$CATALINA_HOME/lib/logstash-logback-encoder-$LOGSTASH_LOGBACK_ENCODER_VERSION.jar:$CATALINA_HOME/lib/jackson-annotations-$JACKSON_ANNOTATIONS_VERSION.jar::$CATALINA_HOME/lib/jackson-databind-$JACKSON_DATABIND_VERSION.jar:$CATALINA_HOME/lib/jackson-core-$JACKSON_DATABIND_VERSION.jar" >> $CATALINA_HOME/bin/setenv.sh \
	&& chmod +x $CATALINA_HOME/bin/setenv.sh \
	&& echo "handlers = org.slf4j.bridge.SLF4JBridgeHandler" > $CATALINA_HOME/conf/logging.properties

ADD logback.xml $CATALINA_HOME/conf/logback/

EXPOSE 8080

WORKDIR $CATALINA_HOME/bin

CMD ["catalina.sh", "run"]
