FROM java:jre
MAINTAINER Vlad Dimitriu <vladimitriu@gmail.com>

ENV JBOSS_HOME /opt/jboss/wildfly
ENV WILDFLY_VERSION 10.0.0.Final
ENV MODESHAPE_VERSION 4.6.0.Final

RUN mkdir /opt/jboss && \
    cd /opt/jboss && \
    curl http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz | tar zx && \
    mv /opt/jboss/wildfly-$WILDFLY_VERSION /opt/jboss/wildfly

RUN cd $JBOSS_HOME && \
    curl -o modeshape.zip http://downloads.jboss.org/modeshape/$MODESHAPE_VERSION/modeshape-$MODESHAPE_VERSION-jboss-wf9-dist.zip && \
    unzip -q modeshape.zip && \
    rm modeshape.zip

RUN /opt/jboss/wildfly/bin/add-user.sh -a -u admin -p admin -g admin,readwrite,read,connect --silent

EXPOSE 8080 9990

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-c", "standalone-modeshape.xml", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]

