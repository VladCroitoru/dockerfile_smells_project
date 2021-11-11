# Based on the official maven Dockerfile, add the "rpm" package so we can build
# RPMs.
# https://hub.docker.com/_/maven/
FROM maven:3-jdk-8
MAINTAINER Mike Kasberg <kasberg.mike@gmail.com>

# CentOS needs Overlayfs plugin so we don't have problems with yum in Docker.
RUN apt-get -q update &&\
    apt-get -q install -y --no-install-recommends rpm &&\
    apt-get -q autoremove &&\
    apt-get -q clean -y

