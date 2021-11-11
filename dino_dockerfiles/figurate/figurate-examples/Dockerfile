# Starting from the Openjdk-8 container
FROM java:openjdk-8-jdk

EXPOSE 8080 8443

# Set the WORKDIR. All following commands will be run in this directory.
WORKDIR /app

# initialise gradle..
COPY gradle gradle
COPY gradlew ./

# Copying all gradle files necessary to install gradle with gradlew
COPY build.gradle gradle.properties settings.gradle ./
COPY feed-aggregator/build.gradle ./feed-aggregator/

ENTRYPOINT ["/app/gradlew"]

CMD ["-q", "tasks", "--all"]
