# https://stackoverflow.com/a/27768965

# just build with `docker-compose build` in the parent directory

# Build stage
FROM maven:3.8.2-openjdk-11 AS build
COPY ./src build/src
COPY ./pom.xml build/
RUN mvn -f build/pom.xml package

# Package stage
FROM openjdk:11
RUN addgroup spring && adduser spring --ingroup spring --gecos "" --disabled-password
USER spring:spring
COPY --from=build ./build/target/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]