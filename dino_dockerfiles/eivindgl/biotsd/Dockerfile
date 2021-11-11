FROM ubuntu:17.10

MAINTAINER Eivind Gard Lund <gardlund@gmail.com>

RUN apt-get update --fix-missing && apt-get install -y wget ca-certificates python3

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH
RUN conda config --add channels defaults \
    && conda config --add channels conda-forge \
    && conda config --add channels bioconda
RUN conda install -y kallisto=0.43.0
