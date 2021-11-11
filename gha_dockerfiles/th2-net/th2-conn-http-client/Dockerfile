FROM gradle:6.6-jdk11 AS build
ARG release_version
ARG vcs_url
COPY ./ .
RUN gradle --no-daemon clean build dockerPrepare \
    -Prelease_version=${release_version} \
    -Pvcs_url=${vcs_url}

FROM adoptopenjdk/openjdk11:alpine
WORKDIR /home
COPY --from=build /home/gradle/build/docker .
ENTRYPOINT ["/home/service/bin/service"]