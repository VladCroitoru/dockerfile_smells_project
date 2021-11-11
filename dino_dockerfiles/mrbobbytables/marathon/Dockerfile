################################################################################
# marathon: 1.3.0
# Date: 1/27/2016
# Marathon Version: 0.14.1-1.0.455.ubuntu1404
# Mesos Version: 0.26.0-0.2.145.ubuntu1404
#
# Description:
# Marathon Mesos framework. Made for executing long running processes
################################################################################

FROM mrbobbytables/mesos-base:1.2.0

MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables


ENV VERSION_MARATHON=0.14.1-1.0.455.ubuntu1404

RUN apt-get -y update                   \
 && apt-get -y install                  \
    marathon=$VERSION_MARATHON          \
 && mkdir -p /etc/marathon/conf         \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
   
COPY ./skel /

RUN chmod +x init.sh  \
 && chown -R logstash-forwarder:logstash-forwarder /opt/logstash-forwarder                                             \
 && wget -P /usr/share/java http://central.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.5/groovy-all-2.4.5.jar  \
 && wget -P /usr/share/java http://central.maven.org/maven2/net/logstash/logback/logstash-logback-encoder/4.5.1/logstash-logback-encoder-4.5.1.jar

ENV JSONLOGBACK=$JAVACPROOT/logstash-logback-encoder-4.5.1.jar:$JAVACPROOT/groovy-all-2.4.5.jar

#marathon web and LIBPROCESS_PORT
EXPOSE 8080 9000

CMD ["./init.sh"]
