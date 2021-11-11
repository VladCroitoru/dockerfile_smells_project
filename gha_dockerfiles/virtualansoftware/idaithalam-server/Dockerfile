#
# Build stage
#
FROM maven:3.6.0-jdk-11-slim AS build
#FROM adoptopenjdk/openjdk11:alpine
LABEL maintainer="info@virtualan.io"
COPY . /home/app/
RUN mvn -f /home/app/pom.xml clean install

#
# Package stage
#
FROM openjdk:17-ea-22-jdk-oracle
COPY --from=build /home/app/target/idaiserver.jar /openapi/virtualan/idaiserver.jar
ENTRYPOINT ["java", "-jar", "/openapi/virtualan/idaiserver.jar"] 
