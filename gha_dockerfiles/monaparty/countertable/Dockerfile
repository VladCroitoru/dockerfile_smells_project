FROM maven:3.8.2-adoptopenjdk-11 as builder

WORKDIR /build
COPY . .
RUN mvn clean package spring-boot:repackage

FROM openjdk:11-jdk-slim

COPY --from=builder /build/target/countertable-*.jar app.jar

ENTRYPOINT [ "java", "-jar", "app.jar" ]
