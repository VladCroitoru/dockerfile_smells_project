FROM maven:3-jdk-11-slim as build

COPY ./src ./src
COPY ./pom.xml ./pom.xml

RUN mvn clean install -U

FROM openjdk:11-jre-slim

WORKDIR /devops_projects

COPY --from=build target/ScriptedPipeline-*.jar ./apps/ScriptedPipeline-*.jar
CMD ["java", "-jar", "./apps/ScriptedPipeline-*.jar"]
