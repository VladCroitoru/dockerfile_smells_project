FROM openjdk:8u92-jre-alpine

ENV HZ_VERSION 2.5.1
ENV JETTY_VERSION 9.3.0.M2
ENV HZ_HOME /opt/hazelcast/
WORKDIR $HZ_HOME

RUN apk --update add supervisor \
    curl && \
    mkdir -p $HZ_HOME && \
    curl "https://download.hazelcast.com/download.jsp?version=hazelcast-$HZ_VERSION&type=tar&p=" | tar zx && \
    cp $HZ_HOME/hazelcast-$HZ_VERSION/mancenter-2.5.war . && \
    cp $HZ_HOME/hazelcast-$HZ_VERSION/lib/hazelcast-$HZ_VERSION.jar . && \
    rm -fr hazelcast-$HZ_VERSION && \
    mkdir -p /var/log/supervisord &&  \
    rm -rf /var/cache/apk/*

ADD customize $HZ_HOME
ADD http://central.maven.org/maven2/org/eclipse/jetty/jetty-runner/$JETTY_VERSION/jetty-runner-$JETTY_VERSION.jar $HZ_HOME

EXPOSE 5701 8080 9001

CMD /usr/bin/supervisord -c $HZ_HOME/supervisord.conf