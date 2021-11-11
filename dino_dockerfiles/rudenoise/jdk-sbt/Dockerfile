# Pull base image
FROM openjdk:8u151-jdk-alpine3.7

RUN apk update && \
    apk upgrade

# Env variables
ENV SBT_VERSION 1.0.2
ENV SBT_HOME /usr/local/sbt

# Install sbt
RUN apk add --no-cache --update bash wget && \
    mkdir -p "$SBT_HOME" && \
    wget -qO - --no-check-certificate "https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz" | tar xz -C $SBT_HOME --strip-components=1 && \
    apk del wget && \
    echo "export PATH=$SBT_HOME/bin/:$PATH" >> /root/.bashrc && \
    source /root/.bashrc && \
    sbt sbtVersion

#RUN sbt sbtVersion

# Define working directory
WORKDIR /root
