ARG APP_VERSION=0.0.1-SNAPSHOT

FROM openjdk:18-jdk-alpine as builder
ARG APP_VERSION

ENV GRADLE_USER_HOME /app/.gradle
ENV GRADLE_OPTS "-Dorg.gradle.parallel=true -Dorg.gradle.daemon=false"

COPY . /app
WORKDIR /app
RUN ./gradlew clean shadowJar -Dversion=${APP_VERSION}

FROM gcr.io/distroless/java:11
ARG APP_VERSION

COPY --from=builder /app/build/libs/ktor-playground-${APP_VERSION}-all.jar /app.jar

USER nonroot
EXPOSE 8080

CMD [ "app.jar" ]
