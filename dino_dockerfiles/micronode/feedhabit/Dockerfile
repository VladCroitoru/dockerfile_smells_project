FROM openjdk:8

# Set the WORKDIR. All following commands will be run in this directory.
WORKDIR /app

# Copying all gradle files necessary to install gradle with gradlew
COPY gradlew build.gradle settings.gradle gradle.properties ./
COPY gradle gradle

COPY feedhabit-app feedhabit-app
COPY feedhabit-content feedhabit-content
COPY feedhabit-config feedhabit-config
COPY feedhabit-api feedhabit-api

ENTRYPOINT ["/app/gradlew"]

CMD ["-q", "tasks", "--all"]
