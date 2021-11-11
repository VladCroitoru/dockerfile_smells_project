# Dockerfile

FROM debian:stretch

RUN apt-get clean && apt-get update && apt-get install -y \
    cython \
    git \
    g++ \
    gmsh \
    ipython \
    libcgal-dev \
    libeigen3-dev \
    libgmp-dev \
    libmpfr-dev \
    libopenmpi-dev \
    python-matplotlib \
    python-numpy \
    python-pip \
    python-scipy \
    python-sphinx \
    python-sphinx-rtd-theme \
    python-tifffile \
    r-base \
    r-cran-randomfields \
    swig

COPY requirements.txt /root

RUN pip install -r /root/requirements.txt

