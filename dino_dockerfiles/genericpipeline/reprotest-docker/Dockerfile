FROM debian:unstable

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install eatmydata -y && rm -rf /var/lib/apt

RUN apt-get update && eatmydata apt-get install reprotest -y && rm -rf /var/lib/apt

COPY patch/build.patch /tmp/build.patch
RUN patch /usr/lib/python3/dist-packages/reprotest/build.py /tmp/build.patch
