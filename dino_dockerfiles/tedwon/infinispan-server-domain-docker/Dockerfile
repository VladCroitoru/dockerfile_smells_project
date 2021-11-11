FROM alpine:3.3

MAINTAINER gustavonalle

# Set the INFINISPAN_SERVER_HOME env variable
ENV INFINISPAN_SERVER_HOME /opt/jboss/infinispan-server

# Set the INFINISPAN_VERSION env variable
ENV INFINISPAN_VERSION 9.0.0.Alpha2

ENV DOMAIN_USER admin 
ENV DOMAIN_PASS admin

ENV HOME /opt/jboss

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
   && apk add --update curl openjdk8 bash && rm /var/cache/apk/*

RUN mkdir -p $HOME && cd $HOME && curl -o $HOME/infinispan.zip "https://repo1.maven.org/maven2/org/infinispan/server/infinispan-server-build/$INFINISPAN_VERSION/infinispan-server-build-$INFINISPAN_VERSION.zip" && unzip infinispan.zip && mv $HOME/infinispan-server-$INFINISPAN_VERSION $HOME/infinispan-server && rm infinispan.zip

COPY start.sh /opt/jboss/infinispan-server/bin/

USER root

RUN sed -i '/other-server-group/,+6d' /opt/jboss/infinispan-server/domain/configuration/host.xml
RUN sed -i '/other-server-group/,+6d' /opt/jboss/infinispan-server/domain/configuration/host-slave.xml
RUN sed -i '/server-two/,+6d' /opt/jboss/infinispan-server/domain/configuration/host.xml

# Expose Infinispan server  ports 
EXPOSE 57600 7600 8080 8181 9990 11211 11222 

CMD ["/opt/jboss/infinispan-server/bin/start.sh"]
