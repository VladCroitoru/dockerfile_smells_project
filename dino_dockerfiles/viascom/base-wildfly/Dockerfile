FROM viascom/base-java:10

LABEL maintainer="technical@viascom.ch"

ENV WILDFLY_VERSION 12.0.0.Final
ENV WILDFLY_HOME /opt/wildfly

# Default username and password for the management user
ENV MANAGEMENT_USERNAME admin
ENV MANAGEMENT_PASSWORD admin

RUN apk add --no-cache curl tar bash

RUN mkdir -p /opt/wildfly
RUN adduser -D -h /opt/wildfly wildfly

USER wildfly

WORKDIR /opt/wildfly

# Installs WILDFLY
RUN curl -O -sSL http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz && \
    tar -xzf wildfly-$WILDFLY_VERSION.tar.gz && \
    mv wildfly-$WILDFLY_VERSION/* $WILDFLY_HOME && \
    rm wildfly-$WILDFLY_VERSION.tar.gz && \
    rm -rf wildfly-$WILDFLY_VERSION

# Expose the ports we're interested in
EXPOSE 8080 9990

# Add management user
RUN $WILDFLY_HOME/bin/add-user.sh ${MANAGEMENT_USERNAME} ${MANAGEMENT_PASSWORD} --silent

CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
