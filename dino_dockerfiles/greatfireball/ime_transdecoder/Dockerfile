FROM ubuntu:xenial

RUN apt update && apt install --yes \
      wget \
      build-essential \
      liburi-escape-xs-perl \
      cpanminus \
      ncbi-blast+ \
      hmmer

RUN cpanm URI::Escape

WORKDIR /opt
RUN wget -O TD.tar.gz https://github.com/TransDecoder/TransDecoder/archive/TransDecoder-v5.0.2.tar.gz && \
    tar xzf TD.tar.gz && \
    rm TD.tar.gz && \
    ln -s TransDecoder-TransDecoder-v5.0.2 TransDecoder

ENV PATH=/opt/TransDecoder:/opt/TransDecoder/util:"$PATH"

WORKDIR TransDecoder
RUN make test

VOLUME /data
WORKDIR /data