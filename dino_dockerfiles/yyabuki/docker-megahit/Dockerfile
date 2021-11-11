FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
# Modified an attached file (run) created by Michael Barton.

ENV PACKAGES wget make python g++ zlib1g-dev bc
ENV MEGAHIT_DIR /megahit
ENV MEGAHIT_TAR https://github.com/voutcn/megahit/archive/v0.1.2.tar.gz

RUN apt-get clean && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends ${PACKAGES} && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir ${MEGAHIT_DIR} && \
    cd ${MEGAHIT_DIR} &&\
    wget --no-check-certificate ${MEGAHIT_TAR} --output-document - |\
    tar xzf - --directory . --strip-components=1 &&\
    make

ADD Procfile /
ADD run /usr/local/bin/

ENTRYPOINT ["run"]
