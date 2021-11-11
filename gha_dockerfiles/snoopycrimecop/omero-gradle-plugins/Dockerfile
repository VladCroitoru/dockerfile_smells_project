# Gradle plugins super project
# ----------------------------
# This dockerfile can be used to build
# the gradle plugins necessary for building
# the omero-build super project. This is mostly
# used by travis to test that the plugins are
# all functioning.

# By default, building this dockerfile will use
# the IMAGE argument below for the runtime image.
ARG IMAGE=openjdk:8-jre-alpine

# To install the built distribution into other runtimes
# pass a build argument, e.g.:
#
#   docker build --build-arg IMAGE=openjdk:9 ...
#

# Similarly, the BUILD_IMAGE argument can be overwritten
# but this is generally not needed.
ARG BUILD_IMAGE=gradle:5.1.1-jdk8

#
# Build phase: Use the gradle image for building.
#
FROM ${BUILD_IMAGE} as build
USER root
RUN apt-get update && apt-get install -y zeroc-ice-all-dev
RUN mkdir /src && chown 1000:1000 /src

USER 1000

# Initialize submodules
WORKDIR /src
COPY --chown=1000:1000 .git /src/.git
COPY --chown=1000:1000 .gitmodules /src/.gitmodules
RUN git submodule update --init

# Build all
COPY --chown=1000:1000 build.sh /src/build.sh
RUN ./build.sh
