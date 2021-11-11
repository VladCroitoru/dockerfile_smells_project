FROM debian:jessie
MAINTAINER Jan Garaj info@monitoringartist.com

RUN \
    apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install python-pip && \
    pip install purestorage && \
    pip install requests && \
    pip install certifi && \
    apt-get clean
