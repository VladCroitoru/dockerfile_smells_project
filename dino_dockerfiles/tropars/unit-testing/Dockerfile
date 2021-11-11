FROM ubuntu:18.04

RUN apt-get update && apt-get install -y maven openjdk-8-jre openjdk-8-jdk

WORKDIR /tmp/

run mkdir src

COPY src ./src/
COPY pom.xml ./

CMD mvn package
