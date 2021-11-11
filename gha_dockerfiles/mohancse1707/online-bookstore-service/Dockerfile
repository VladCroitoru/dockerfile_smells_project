# For Java 8, try this
FROM openjdk:8-jdk-alpine

# For Java 11, try this
# FROM adoptopenjdk/openjdk11:alpine-jre

# Refer to Maven build -> finalName
ARG JAR_FILE=target/online-bookstore-service-0.0.1-SNAPSHOT.jar

# cd /opt/app
WORKDIR /opt/app

COPY ${JAR_FILE} online-bookstore-service.jar

ENTRYPOINT ["java","-jar", "online-bookstore-service.jar"]