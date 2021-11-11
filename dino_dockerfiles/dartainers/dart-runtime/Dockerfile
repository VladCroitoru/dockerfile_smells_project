# This is a base image which only includes Dart SDK.
FROM  ubuntu:12.04.5
MAINTAINER  Anatoly Pulyaevskiy <anatoly.pulyaevskiy@gmail.com>

LABEL Description="Docker image with Dart runtime"

ENV DEBIAN_FRONTEND noninteractive
ENV CHANNEL stable
ENV SDK_VERSION 1.19.1
ENV ARCHIVE_URL https://storage.googleapis.com/dart-archive/channels/$CHANNEL/release/$SDK_VERSION
ENV DART_SDK /usr/local/dart-sdk
ENV PATH $PATH:$DART_SDK/bin
ENV PATH $PATH:$HOME/.pub-cache/bin

RUN apt-get update && apt-get install -y curl unzip

WORKDIR /usr/local
RUN curl $ARCHIVE_URL/sdk/dartsdk-linux-x64-release.zip > dartsdk.zip
RUN unzip dartsdk.zip > /dev/null
RUN rm dartsdk.zip

WORKDIR /root
