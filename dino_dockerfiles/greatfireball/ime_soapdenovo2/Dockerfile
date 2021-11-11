FROM ubuntu:xenial

LABEL maintainer="frank.foerster@ime.fraunhofer.de"
LABEL description="Dockerfile providing the soapdenovo assembly software software"

RUN apt-get update && \
    apt-get install --yes build-essential git && \
    cd /opt && \
    git clone https://github.com/aquaskyline/SOAPdenovo2.git && \
    cd SOAPdenovo2 && \
    git checkout r241 && \
    rm -rf .git && \
    make && \
    apt purge --yes build-essential git

ENV PATH=/opt/SOAPdenovo2/:"$PATH"

VOLUME /data

WORKDIR /data

