# syntax=docker/dockerfile:1

FROM openjdk:16-alpine3.13
WORKDIR /home/runner/work/Adelheid/Adelheid
ARG JAR_FILE=*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
