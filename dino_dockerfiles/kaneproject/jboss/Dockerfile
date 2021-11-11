FROM frolvlad/alpine-oraclejdk8
ENV WILDFLY_VERSION 10.1.0.CR1
ENV JBOSS_HOME /opt/jboss/wildfly
RUN apk add --update curl && \
    rm -rf /var/cache/apk/*
RUN addgroup -g 1000 -S jboss && \
    mkdir -p /opt/jboss && \
    adduser -h /opt/jboss -s /sbin/nologin -G jboss -S -u 1000 jboss && \
    chown jboss:jboss /opt/jboss
WORKDIR /opt/jboss
USER jboss
RUN cd $HOME && \
    curl http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz | tar zx && \
    mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly
RUN /opt/jboss/wildfly/bin/add-user.sh jboss jboss --silent
EXPOSE 8080 9990
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0","-bmanagement","0.0.0.0"]
