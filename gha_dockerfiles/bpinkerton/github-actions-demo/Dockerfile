FROM maven:3.6.1-jdk-8-alpine as builder
COPY . .
RUN mvn clean package
FROM gcr.io/distroless/java:8
COPY --from=builder ./target/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
