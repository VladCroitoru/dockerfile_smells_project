FROM maven:3.6.0-jdk-11-slim AS build

WORKDIR /app

COPY ./ ./

RUN mvn clean package

FROM openjdk:11-jre-slim

COPY --from=build /app/target/*.jar /app.jar

CMD ["java", "-jar", "/app.jar"]