FROM anapsix/alpine-java:8_jdk-dcevm_unlimited

ENV WILDFLY_VERSION 10.1.0.Final
ENV WILDFLY_SHA1 9ee3c0255e2e6007d502223916cefad2a1a5e333
ENV JBOSS_HOME /opt/jboss/wildfly

RUN echo "ipv6" >> /etc/modules
RUN apk upgrade --update
RUN apk add curl

RUN mkdir -p /opt/HotswapAgent/ \
    && curl -s -L -o /opt/HotswapAgent/HotswapAgent-1.0.0.jar https://github.com/HotswapProjects/HotswapAgent/releases/download/1.0/hotswap-agent-1.0.jar

RUN cd $HOME \
    && curl -O https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz \
    && sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \
    && tar xf wildfly-$WILDFLY_VERSION.tar.gz \
    && mkdir -p /opt/jboss \
    && mv $HOME/wildfly-$WILDFLY_VERSION $JBOSS_HOME \
    && rm wildfly-$WILDFLY_VERSION.tar.gz;

ENV LAUNCH_JBOSS_IN_BACKGROUND true

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]