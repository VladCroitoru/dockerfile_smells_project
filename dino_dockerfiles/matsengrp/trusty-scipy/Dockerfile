from ubuntu:trusty

RUN apt-get update -q && \
    apt-get install -y -q --no-install-recommends \
    build-essential \
    cython \
    gcc \
    gfortran \
    libblas-dev \
    libfreetype6-dev \
    libhdf5-dev \
    liblapack-dev \
    libpng12-dev \
    libxft-dev \
    python-dev \
    python-dev \
    python-pip

RUN pip install \
    numpy \
    pandas \
    scipy \
    seaborn \
    tables

