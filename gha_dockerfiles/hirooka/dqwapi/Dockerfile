FROM openjdk:11-slim as builder
WORKDIR /app
COPY . .
RUN ./gradlew build

FROM openjdk:11-jre-slim
COPY --from=builder /app/build/libs/dqwapi-1.0.0-SNAPSHOT.jar /app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-XX:MaxRAMPercentage=75", "-Djava.security.egd=file:/dev/./urandom", "-Dserver.port=8080", "-jar", "/app.jar"]
