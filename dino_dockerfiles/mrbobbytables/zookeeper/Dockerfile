################################################################################
# zookeeper: 1.2.1
# Date: 5/13/2016
# Mesos Version: 0.26.0-0.2.145.ubuntu1404
#
# Description:
# Zookeeper container for use with Mesos deployment. Version is tied to 
# mesos-base container image.
################################################################################


FROM mrbobbytables/mesos-base:1.2.0

MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables

COPY ./skel /

RUN chmod +x init.sh    \
 && chown -R logstash-forwarder:logstash-forwarder /opt/logstash-forwarder                                                      \
 && wget -P /usr/share/java http://central.maven.org/maven2/net/logstash/log4j/jsonevent-layout/1.7/jsonevent-layout-1.7.jar    \
 && wget -P /usr/share/java http://central.maven.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar                  \
 && wget -P /usr/share/java http://central.maven.org/maven2/junit/junit/4.12/junit-4.12.jar                                     \
 && wget -P /usr/share/java https://json-smart.googlecode.com/files/json-smart-1.2.jar

ENV JSONLOG4JCP=$JAVACPROOT/jsonevent-layout-1.7.jar:$JAVACPROOT/junit-4.12.jar/:$JAVACPROOT/commons-lang-2.6.jar:$JAVACPROOT/json-smart-1.2.jar

EXPOSE 2181 2888 3888

CMD ["./init.sh"]
