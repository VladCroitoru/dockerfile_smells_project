# Use the official maven/Java 8 image to create a build artifact.
# https://hub.docker.com/_/maven
FROM gradle:6.7.1-jdk11 as builder

# Copy local code to the container image.
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src

# Build a release artifact.
RUN gradle clean build -x test

# Use AdoptOpenJDK for base image.
# It's important to use OpenJDK 8u191 or above that has container support enabled.
# https://hub.docker.com/r/adoptopenjdk/openjdk8
# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
FROM adoptopenjdk/openjdk11:alpine-slim

# Copy the jar to the production image from the builder stage.
COPY --from=builder /home/gradle/src/build/libs/*.jar /app/SpringBootBackSample.jar

# Run the web service on container startup.
CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/SpringBootBackSample.jar"]