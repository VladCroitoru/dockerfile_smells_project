FROM ubuntu:16.04

MAINTAINER Suilong Liang <suilong.liang@worktogether.io>

ENV JAVA_MAJOR 8
ENV JAVA_VERSION 8u151-b12
ENV JAVA_VERSION_MINOR 0ubuntu0.16.04.2
ENV DEBIAN_FRONTEND noninteractive

RUN set -ex; \
    apt-get update; \
    apt-get install -V -y --no-install-recommends -o Dpkg::Options::="--force-overwrite" \
	openjdk-${JAVA_MAJOR}-jre-headless=${JAVA_VERSION}-${JAVA_VERSION_MINOR}; \
    rm -rf /var/lib/apt/lists/* 


ENV JAVA_HOME /usr/lib/jvm/java-${JAVA_MAJOR}-openjdk-amd64
