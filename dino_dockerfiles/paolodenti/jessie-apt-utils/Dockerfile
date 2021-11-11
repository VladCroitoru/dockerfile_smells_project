FROM debian:8.7

MAINTAINER Paolo Denti "paolo.denti@gmail.com"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils

# cleanup
RUN rm -rf /var/lib/apt/lists/*
