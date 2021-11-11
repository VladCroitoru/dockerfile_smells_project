# syntax=docker/dockerfile:1

FROM ubuntu:18.04

LABEL maintainer="Alex Moshniaha  <ivanmoshnyaga@gmail.com>"

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -qy git && \
# Install JDK
    apt install -qy default-jre && \
    apt install -qy default-jdk && \
# Install maven
    apt-get install -qy maven

WORKDIR /app

COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./mvnw dependency:go-offline

COPY src ./src

CMD ["./mvnw", "spring-boot:run"]