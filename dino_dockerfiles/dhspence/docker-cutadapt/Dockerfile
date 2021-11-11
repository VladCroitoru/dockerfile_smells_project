FROM ubuntu:xenial
MAINTAINER David H. Spencer <dspencer@wustl.edu>

LABEL \
  description="cutadapt image for read trimming"

RUN apt-get update -y && apt-get install -y \
    python \
    python-dev \
    build-essential \
    virtualenv \
    python-pip

RUN mkdir /opt/cutadapt

RUN pip install --install-option="--prefix=/opt/cutadapt" --upgrade cutadapt && \
    cp /opt/cutadapt/bin/cutadapt /usr/bin/cutadapt

RUN export PYTHONPATH=/opt/cutadapt/lib/python2.7/site-packages/
