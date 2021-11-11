FROM ubuntu:16.04

LABEL ubuntu.version="16.04" bedtools.version="2.25.0" maintainer="Alice Minotto, @Earlham Institute"

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get -y update && apt-get install -yy bedtools

WORKDIR /data/

#ENTRYPOINT []
