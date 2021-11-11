FROM debian:jessie

LABEL maintainer="frank.foerster@ime.fraunhofer.de"
LABEL description="Dockerfile providing the Piranha CLIP-seq peak detection tool"
RUN apt update && apt install --yes build-essential wget tar gzip

RUN apt install --yes libbamtools-dev python libgsl0-dev

WORKDIR /
RUN wget http://smithlabresearch.org/downloads/piranha-1.2.1.tar.gz && tar xzf piranha-1.2.1.tar.gz && rm piranha-1.2.1.tar.gz

WORKDIR /piranha-1.2.1
RUN ./configure && make && make test && make install

ENV PATH=/piranha-1.2.1/bin:$PATH

VOLUME /data
WORKDIR /data