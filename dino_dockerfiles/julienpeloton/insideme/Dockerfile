FROM debian:jessie

MAINTAINER Julien Peloton <j.peloton@sussex.ac.uk>

ENV PATH miniconda/bin:/usr/local/bin:$PATH

ENV PYTHON_VERSION 2.7.13

WORKDIR /home

ADD . /home/

RUN apt-get update \
    && apt-get install -y wget bzip2 python libgl1-mesa-swx11 ssh \
    && wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh \
    && bash miniconda.sh -b -p /home/miniconda \
    && export PATH="/home/miniconda/bin:$PATH" \
    && /home/miniconda/bin/conda update --yes conda \
    && /home/miniconda/bin/conda install --yes python=2.7 pip numpy matplotlib mpi4py \
    && python setup.py install \
    && python tests/test.py \
    && AnalyzeMe --output test_docker
