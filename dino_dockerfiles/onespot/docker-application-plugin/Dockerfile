FROM openjdk:8u212-jdk
MAINTAINER OneSpot <dev@onespot.com>

# Create a onespot group and user.
# Install the components common to all apps.
# https://github.com/yelp/dumb-init: lightweight init system
# su-exec: sudo replacement
RUN addgroup onespot && \
    useradd -M -g onespot onespot && \
    mkdir /tmp/kafka-streams && \
    chown onespot:onespot /tmp/kafka-streams && \
    apt-get update && apt-get install dumb-init gosu

VOLUME /tmp/kafka-streams
