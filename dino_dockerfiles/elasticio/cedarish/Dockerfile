FROM ubuntu:20.04
MAINTAINER zubairov "info@elastic.io"

ADD ./stack/setup.sh /tmp/build.sh
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive /tmp/build.sh
