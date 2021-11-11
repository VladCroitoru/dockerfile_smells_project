FROM openjdk:8u121-jdk-alpine

RUN apk update && apk add maven

COPY pom.xml /
COPY src /src

RUN mvn clean package

WORKDIR /app

ENTRYPOINT ["java", "-jar", "/target/pdf-jar-with-dependencies.jar"]
