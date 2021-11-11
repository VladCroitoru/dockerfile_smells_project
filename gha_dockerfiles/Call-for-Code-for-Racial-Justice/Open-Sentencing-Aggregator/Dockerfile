# IBM Java SDK UBI is not available on public docker yet. Use regular
# base as builder until this is ready. For reference:
# https://github.com/ibmruntimes/ci.docker/tree/master/ibmjava/8/sdk/ubi-min

FROM adoptopenjdk:14-jdk-hotspot AS builder
LABEL maintainer="IBM Java Engineering at IBM Cloud"

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y maven
RUN mvn -N io.takari:maven:wrapper -Dmaven=3.5.0
RUN ./mvnw install

# Multi-stage build. New build stage that uses the UBI as the base image.
FROM ibmcom/websphere-liberty:20.0.0.6-full-java11-openj9-ubi
LABEL maintainer="IBM Java Engineering at IBM Cloud"
ENV PATH /project/target/liberty/wlp/bin/:$PATH

COPY --from=builder /app/target/liberty/wlp/usr/servers/defaultServer /config/

# Grant write access to apps folder, this is to support old and new docker versions.
# Liberty document reference : https://hub.docker.com/_/websphere-liberty/
USER root
RUN chmod g+w /config/apps
USER 1001
# install any missing features required by server config
RUN installUtility install --acceptLicense defaultServer
