FROM maven:3.6.3-jdk-8 as build-container

USER root

RUN mkdir -p /home/service

COPY . /home/service

WORKDIR /home/service

RUN mvn install -Dmaven.test.skip=true



FROM openjdk:8

RUN mkdir -p /home/service
COPY --from=build-container /home/service/target/study_shop-0.0.1-SNAPSHOT.jar /home/service

