FROM  ubuntu:latest
MAINTAINER Paul Ingles <paul@oobaloo.co.uk>

RUN apt-get update
RUN apt-get install -y unzip ca-certificates

WORKDIR /tmp

ADD https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip /tmp/consul.zip
RUN unzip consul.zip
RUN chmod +x consul
RUN mv consul /bin/consul
RUN rm consul.zip

EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp
VOLUME ["/data", "/config"]

ENV SHELL /bin/bash

ENTRYPOINT ["/bin/consul", "agent", "-config-dir=/config", "-data-dir=/data", "-client=0.0.0.0"]
CMD []