FROM debian:wheezy
MAINTAINER John Eckhart "jeckhart@yodle.com"

ADD build /build/docker-yodle-base

RUN /build/docker-yodle-base/prepare.sh && /build/docker-yodle-base/cleanup.sh
