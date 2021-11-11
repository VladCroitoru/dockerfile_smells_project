FROM ubuntu:16.04

LABEL ubuntu.version="16.04" python.version="3.5.1" cython.version="0.23.4" wheel.version="0.29.0" networkx.version="1.11" sqlalchemy.version="1.0.14" biopython.version="1.67" scikit-learn.version="0.17.1" magic.version="0.4.12" frozendict.version="1.0" tabulate.version="0.7.5" scipy.version="0.18.0" numpy.version="1.11.0" blast.version="2.2.31" transdecoder.version="2.0.1"

MAINTAINER Alice Minotto @ Earlham Institute

ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 BLASTDB=/data/blastdatabases
ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN     mkdir /data/ && cd /data && mkdir blastdatabases && \
        apt-get -y update && apt-get install -yy language-pack-en-base python3 python3-dev python3-pip cython3 ncbi-blast+ transdecoder snakemake git gridengine-drmaa-dev && \
        pip3 install mikado==1.2

WORKDIR /data/

