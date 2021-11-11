# Container image that runs your code
FROM openjdk:11-jdk AS build
COPY . /build
WORKDIR /build
RUN ./gradlew shadowJar --no-daemon --info --console=plain

FROM openjdk:11-jdk as runtime
RUN apt-get update && apt-get --no-install-recommends -y install hub
RUN mkdir /app
WORKDIR /app
COPY --from=build /build/build/libs/buildpack-update-action-1.0-SNAPSHOT-all.jar /app

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Executes `entrypoint.sh` when the Docker container starts up
ENTRYPOINT ["/entrypoint.sh"]
