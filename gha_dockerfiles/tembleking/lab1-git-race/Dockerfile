FROM openjdk:11 as builder
WORKDIR /app
COPY . .
RUN /app/gradlew bootJar

FROM gcr.io/distroless/java:11
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar /app/lab1-git-race.jar
ENTRYPOINT ["java", "-jar", "/app/lab1-git-race.jar"]
