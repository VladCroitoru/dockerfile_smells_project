FROM ubuntu:16.04
MAINTAINER Shota Kawabuchi <shota.kawabuchi+github@gmail.com>

RUN set -x && \
  apt-get update && \
  apt-get install -y \
    build-essential \
    cmake \
    git \
    python \
    python-pip \
    wget \
    vim && \
  apt-get clean && \
  wget https://raw.github.com/karies/cling-all-in-one/master/clone.sh && \
  chmod u+x clone.sh

RUN set -x && \
  ./clone.sh

RUN set -x && \
  pip install jupyter && \
  cd /inst/share/cling/Jupyter/kernel && \
  pip install -e . && \
  jupyter-kernelspec install cling-c++17 && \
  jupyter-kernelspec install cling-c++14 && \
  jupyter-kernelspec install cling-c++11
ENV PATH /inst/bin:$PATH
COPY jupyter_notebook_config.py /root/.jupyter/
EXPOSE 8888 

RUN mkdir /workspace
VOLUME /workspace
VOLUME /mnt
WORKDIR /workspace

