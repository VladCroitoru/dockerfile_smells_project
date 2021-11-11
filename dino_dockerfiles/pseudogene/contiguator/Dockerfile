FROM ubuntu:16.10

MAINTAINER Michael Bekaert <michael.bekaert@stir.ac.uk>

LABEL description="CONTIGuator Docker" version="2.7.5" Vendor="Institute of Aquaculture, University of Stirling"
ENV CONTIGUATOR=2.7.5

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget --no-install-recommends

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y primer3 mummer python python-biopython abacas ncbi-blast+ --no-install-recommends

RUN wget --no-check-certificate https://github.com/combogenomics/CONTIGuator/archive/v2.7.5.tar.gz && \
    tar xfz v2.7.5.tar.gz && \
    cp CONTIGuator-2.7.5/CONTIGuator.py /usr/local/bin/CONTIGuator.py && \
    rm -rf v2.7.5.tar.gz CONTIGuator-2.7.5

RUN mkdir /data
WORKDIR /data
