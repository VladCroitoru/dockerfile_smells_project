# Dockerfile

FROM docker.io/library/openjdk:8-jre-alpine

# RUN apk add --no-cache bash curl

EXPOSE 8080
EXPOSE 8081

WORKDIR /data

ENTRYPOINT ["/bin/sh", "/data/entrypoint.sh"]

COPY ./entrypoint.sh /data/entrypoint.sh

COPY ./jmx/config.yaml /data/config.yaml
COPY ./jmx/dd-java-agent-0.75.0.jar.zip /data/dd-java-agent.jar
COPY ./jmx/jmx_prometheus_javaagent-0.15.0.jar.zip /data/jmx_javaagent.jar
COPY ./jmx/codeguru-profiler-java-agent-standalone-1.1.1.jar.zip /data/codeguru-profiler-java-agent.jar

COPY target/*.jar /data/ROOT.jar
