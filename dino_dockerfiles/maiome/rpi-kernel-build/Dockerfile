FROM ubuntu:trusty
MAINTAINER Sean Johnson <pirogoeth@maio.me>

VOLUME ["/config", "/kern"]

ADD build /build
RUN run-parts --report --exit-on-error /build/parts && rm -rf /build

WORKDIR /data
ENTRYPOINT ["/data/build.sh"]
