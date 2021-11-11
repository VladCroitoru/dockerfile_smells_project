# docker build -t fast-maven:1.5 .
FROM mvnd:0.6.0 as build

COPY .mvn .mvn
COPY mvnw .
COPY pom.xml .
COPY src src

RUN /opt/mvnd/bin/mvnd -B package

FROM openjdk:11-jre-slim-buster

COPY --from=build target/fast-maven-builds-1.5.jar .

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "fast-maven-builds-1.5.jar"]
