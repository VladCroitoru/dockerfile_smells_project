FROM debian:latest

MAINTAINER nyxgear <dev@nyxgear.com>

# dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y curl apt-transport-https gnupg2

# Google Cloud SDK
RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-"$(grep "VERSION=" /etc/os-release | sed 's/.*(//; s/).*//')" main" \
    | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update &&  \
    apt-get install -y google-cloud-sdk

# Python App Engine component
RUN apt-get install -y google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-python-extras google-cloud-sdk-datastore-emulator

# Additianal python modules
RUN apt-get install -y python-pil

# cleanup build tools to save image footprint
RUN apt-get remove -y curl apt-transport-https && \
    apt-get autoremove -y && \
    apt-get clean
