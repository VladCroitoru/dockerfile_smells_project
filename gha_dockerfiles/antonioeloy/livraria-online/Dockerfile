FROM maven:3.6.1-jdk-8-alpine AS MAVEN_BUILD

MAINTAINER Antonio Eloy

COPY pom.xml /build/
COPY src /build/src/

WORKDIR /build/
RUN mvn clean package

FROM tomcat:8-jre8-alpine

COPY --from=MAVEN_BUILD /build/target/livraria.war /usr/local/tomcat/webapps