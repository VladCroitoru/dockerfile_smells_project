FROM ubuntu:15.04

MAINTAINER Federico Gimenez <fgimenez@canonical.com>

# Install packages
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:nviennot/tmate
RUN apt-get update && \
    apt-get install --no-install-recommends -y tmate openssh-client vim emacs24-nox sudo && \
    apt-get clean
