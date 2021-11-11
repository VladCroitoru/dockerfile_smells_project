# syntax=docker/dockerfile:1
FROM maven:3-openjdk-16 as resolve_maven_dependencies
WORKDIR /app

# Copying and initializing Maven
COPY pom.xml .
RUN mvn dependency:go-offline

FROM resolve_maven_dependencies as build
WORKDIR /app

COPY ./src ./src
RUN mvn clean package

FROM openjdk:16-alpine as run
WORKDIR /app

COPY --from=build /app/target/*.jar ./app.jar

ENV JAVA_OPTS ""
ENTRYPOINT ["java", "-jar", "app.jar"]