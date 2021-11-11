# copyright 2017-2018 Regents of the University of California and the Broad Institute. All rights reserved.
FROM python:3.8-buster

MAINTAINER Anthony S. Castanza <acastanza@cloud.ucsd.edu>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN mkdir /src

# install system dependencies
RUN apt-get update --yes
RUN apt-get install build-essential --yes
RUN apt-get install libcurl4-gnutls-dev --yes
RUN apt-get install libhdf5-serial-dev --yes
# RUN apt-get install libigraph0-dev --yes #This should install automatically with python-igraph as the repo version fails
RUN apt-get install libxml2-dev --yes
RUN apt-get install libtool --yes
RUN apt-get install flex bison --yes

# install python with conda
RUN mkdir /conda && \
    cd /conda && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh && \
    bash Miniconda3-py38_4.10.3-Linux-x86_64.sh -b -p /opt/conda
ENV PATH="/opt/conda/bin:${PATH}"

# install R dependencies


# install python dependencies
RUN pip install Cython==0.29.24
RUN pip install joblib==1.0.1
RUN pip install numba==0.52.0
RUN pip install numpy==1.20.3
RUN pip install pandas==1.2.2
RUN pip install scipy==1.7.1
RUN pip install anndata==0.7.6
RUN pip install python-igraph==0.9.6
RUN pip install louvain==0.7.0
RUN pip install scanpy==1.8.1
RUN pip install cmake==3.18.2
RUN pip install MulticoreTSNE==0.1
RUN pip install loompy==3.0.6
RUN pip install scvelo==0.2.4
RUN pip install scikit-misc==0.1.4
RUN pip install pybind11==2.6.2
RUN pip install hnswlib==0.5.2
RUN pip install leidenalg==0.8.7

# copy module files
COPY module/* /build/
RUN chmod a+x /build/compute_scvelo.py

# display software versions
RUN python --version
RUN pip --version

# default command
CMD ["python", "--version"]
