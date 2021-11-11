FROM python:3.6
MAINTAINER James Endicott <james.endicott@colorado.edu>
WORKDIR /app
ENTRYPOINT ["/bin/bash", "-c", "source /app/sh/entrypoint.sh"]

RUN pip install \
        cython \
        gensim \
        numpy \
        nltk \
        pandas \
        pyyaml \
        tables \
        scipy \
    && python -m nltk.downloader -d /usr/share/nltk_data punkt wordnet stopwords

RUN apt-get update \
    && apt-get install -y \
        hdf5-tools \
        hdf5-helpers \
        libhdf5-openmpi-dev \
        openmpi-bin \
    && pip install mpi4py \
    && CC=mpicc HDF5_MPI="ON" pip install --no-binary=h5py h5py \
    && rm -rf /var/lib/apt/lists/*

RUN pip install sklearn
COPY ./ /app/