FROM openjdk:8-jdk-alpine

ENV TZ='GMT-3'

VOLUME /tmp

EXPOSE 8086

ARG JAR_FILE=target/*.jar

ADD ${JAR_FILE} api-integra-api.jar

ENTRYPOINT ["java","-Xmx4G","-jar","/api-integra-api.jar"]
