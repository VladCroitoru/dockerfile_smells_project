FROM walkingdevs/alpine:3.4

RUN apk update && \
    apk upgrade && \
    apk add openjdk8-jre-base && \
    rm -rf /var/cache/apk/*

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
