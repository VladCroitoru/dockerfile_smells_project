FROM openjdk:8-jdk-alpine

MAINTAINER Martin Ford <ford.j.martin@gmail.com>

ARG NEWRELIC_AGENT_VERSION=3.33.0

RUN apk --no-cache add curl unzip && \
    mkdir -p /tmp /opt/newrelic/logs && \
    curl -o /tmp/newrelic-java.zip -fSL \
      https://oss.sonatype.org/content/repositories/releases/com/newrelic/agent/java/newrelic-java/$NEWRELIC_AGENT_VERSION/newrelic-java-$NEWRELIC_AGENT_VERSION.zip && \
    unzip /tmp/newrelic-java.zip newrelic/newrelic.jar -d /opt && \
    rm /tmp/newrelic-java.zip && \
    chmod a+r /opt/newrelic/newrelic.jar && \
    chmod a+rw /opt/newrelic/logs && \
    apk del curl unzip
