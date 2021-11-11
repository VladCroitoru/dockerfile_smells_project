FROM maven:3.6.0-jdk-11-slim AS base
WORKDIR /demo

COPY src ./src
COPY pom.xml ./

FROM base AS test
RUN mvn test

FROM base AS build
RUN mvn package

FROM openjdk:11-jre-slim AS prod
EXPOSE 8080

COPY --from=build /demo/target/demo-*.jar /demo.jar

CMD ["java","-jar","/demo.jar"]