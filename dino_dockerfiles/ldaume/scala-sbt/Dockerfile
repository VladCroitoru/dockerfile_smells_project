#
# Scala and sbt Dockerfile
#
# https://github.com/spikerlabs/scala-sbt (based on https://github.com/hseeberger/scala-sbt)
# 

#FROM  debian:stretch-slim
FROM ubuntu:rolling

ARG SCALA_VERSION
ARG SBT_VERSION
ARG JAVA_VERSION

ENV SCALA_VERSION ${SCALA_VERSION:-2.12.10}
ENV SBT_VERSION ${SBT_VERSION:-1.3.2}
ENV JAVA_VERSION ${JAVA_VERSION:-13.0.0-open}

RUN \
  apt-get update -y && apt-get upgrade -y \
  && apt-get install -y bash \
  curl \
  openssh-client \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg2 \
  tzdata \
  bzip2 \
  zip \
  unzip \
  xz-utils \
  software-properties-common

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN \
  curl -s "https://get.sdkman.io" > sdk.sh \
  && chmod +x sdk.sh \
  && ./sdk.sh

RUN \
  . "$HOME/.sdkman/bin/sdkman-init.sh" \
  && sdk i java "$JAVA_VERSION" \
  && sdk i sbt "$SBT_VERSION" \
  && sdk i scala "$SCALA_VERSION"

RUN rm -rf "$HOME/.sdkman/archives"

ENV PATH "/root/.sdkman/candidates/scala/current/bin/:/root/.sdkman/candidates/java/current/bin/:/root/.sdkman/candidates/sbt/current/bin/:$PATH"

RUN java -version && sbt sbtVersion && sbt scalaVersion

RUN \
  curl -fsSL get.docker.com -o get-docker.sh && \
  sh get-docker.sh
  
ENTRYPOINT ["/etc/init.d/docker","start"]
