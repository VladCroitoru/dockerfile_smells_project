FROM gradle:6.8-jdk11 AS build
ARG release_version
COPY ./ .
RUN gradle --no-daemon clean build dockerPrepare -Prelease_version=${release_version}

FROM adoptopenjdk/openjdk11:alpine
WORKDIR /home
COPY --from=build /home/gradle/build/docker .
ENTRYPOINT ["/home/service/bin/service"]