# copyright 2017-2018 Regents of the University of California and the Broad Institute. All rights reserved.
FROM python:3.6

MAINTAINER Ted Liefeld <jliefeld@cloud.ucsd.edu>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && \
   apt-get install zip --yes

RUN mkdir /build

RUN mkdir /conda && \
    cd /conda && \
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda

ENV PATH="/opt/conda/bin:${PATH}"

RUN   apt-get install libhdf5-serial-dev --yes


ADD requirements.txt /build/requirements.txt
RUN pip install -r /build/requirements.txt

COPY module/run_scanpy_module.py /usr/local/build/run_scanpy_module.py



CMD [ "python --version"]
