FROM maven:3-jdk-8-alpine

COPY src /opt/src
COPY pom.xml /opt/pom.xml

WORKDIR /opt

RUN mvn package
COPY src/main/ressources /opt/target

EXPOSE 5557
EXPOSE 5558

WORKDIR /opt/target
