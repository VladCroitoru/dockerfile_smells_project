FROM openjdk:8-jdk-alpine

ENV GRADLE_VERSION 3.2

# get gradle and supporting libs
RUN apk -U add --no-cache curl; \
    curl https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip > gradle.zip; \
    unzip gradle.zip; \
    rm gradle.zip; \
    apk del curl; \
    apk update && apk add --no-cache libstdc++ && rm -rf /var/cache/apk/*

ENV PATH=${PATH}:/gradle-${GRADLE_VERSION}/bin

RUN mkdir -p /work
RUN mkdir -p /GRADLE_CACHE

# Gradle work directory
VOLUME work

# Gradle cache directory
VOLUME GRADLE_CACHE

WORKDIR /work

ENTRYPOINT ["gradle", "-g", "/GRADLE_CACHE", "--no-daemon"]
