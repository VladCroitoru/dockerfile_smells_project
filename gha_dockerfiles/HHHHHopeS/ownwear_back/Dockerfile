FROM maven:3.6.3-openjdk-11-slim as builder

WORKDIR /app
COPY pom.xml .
# Use this optimization to cache the local dependencies. Works as long as the POM doesn't change
COPY keystore.p12 /app/target/
COPY src/ /app/src/
RUN mvn package

# Use AdoptOpenJDK for base image.
FROM adoptopenjdk/openjdk11:latest

# Copy the jar to the production image from the builder stage.
COPY --from=builder /app/target/*.jar /app.jar

# Run the web service on container startup.
CMD ["java", "-jar", "/app.jar"]