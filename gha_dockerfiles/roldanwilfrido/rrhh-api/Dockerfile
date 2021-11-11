FROM openjdk:11-jre-slim

COPY build/libs/rrhh-api-1.0.jar rrhh-api-1.0.jar

ENV APP_NAME=rrhh-api

ENTRYPOINT ["java","-jar","/rrhh-api-1.0.jar"]