#Copyright (C) 2016 by Ewan Barr
# Licensed under the Academic Free License version 3.0
# This program comes with ABSOLUTELY NO WARRANTY.
# You are free to modify and redistribute this code as long
# as you do not remove the above attribution and reasonably
# inform receipients that you have modified the original work.

FROM ubuntu:16.04

MAINTAINER Ewan Barr "ebarr@mpifr-bonn.mpg.de"

# Suppress debconf warnings
ENV DEBIAN_FRONTEND noninteractive


#Update and upgrade

RUN apt-get -y check && \
    apt-get -y update && \
    apt-get install -y apt-utils apt-transport-https software-properties-common python-software-properties && \
    apt-get -y update --fix-missing && \
    apt-get -y upgrade


# Install dependencies
RUN apt-get --no-install-recommends -y install \
    build-essential \
    autoconf \
    autotools-dev \
    automake \
    pkg-config \
    csh \
    gcc \
    gfortran \
    wget \
    git \
    libcfitsio-dev \
    pgplot5 \
    swig2.0 \
    python \
    python-dev \
    python-pip \
    libfftw3-3 \
    libfftw3-bin \
    libfftw3-dev \
    libfftw3-single3 \
    libx11-dev \
    libpng12-dev \
    libpng3 \
    libpnglite-dev \
    libglib2.0-0 \
    libglib2.0-dev \
    xorg \
    openbox \
    vim \
    python-tk \
    libblas-dev \
    imagemagick \ 
    && rm -rf /var/lib/apt/lists/*

RUN apt-get -y clean

# Install python packages
RUN pip install pip -U && \
    pip install setuptools -U && \
    pip install numpy -U && \
    pip install scipy==0.19.0 -U && \
    pip install matplotlib -U && \
    easy_install scikit-learn==0.12.1 && \
    easy_install theano==0.7 
   

# Define home, psrhome, OSTYPE and create the directory
ENV HOME /home/psr
ENV PSRHOME $HOME/software
ENV OSTYPE linux
RUN mkdir -p $PSRHOME

# PGPLOT
ENV PGPLOT_DIR /usr/lib/pgplot5
ENV PGPLOT_FONT /usr/lib/pgplot5/grfont.dat
ENV PGPLOT_INCLUDES /usr/include
ENV PGPLOT_BACKGROUND white
ENV PGPLOT_FOREGROUND black
ENV PGPLOT_DEV /xs
WORKDIR $PSRHOME

# Pull all repos
RUN wget http://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz && \
    tar -xvf psrcat_pkg.tar.gz -C $PSRHOME && \
    git clone git://git.code.sf.net/p/tempo/tempo && \
    git clone https://github.com/scottransom/presto.git && \
    git clone https://github.com/scottransom/pyslalib.git

# Psrcat
ENV PSRCAT_FILE $PSRHOME/psrcat_tar/psrcat.db
ENV PATH $PATH:$PSRHOME/psrcat_tar
WORKDIR $PSRHOME/psrcat_tar
RUN /bin/bash makeit && \
    rm -f ../psrcat_pkg.tar.gz

# Tempo
ENV TEMPO $PSRHOME/tempo
ENV PATH $PATH:$PSRHOME/tempo/bin
WORKDIR $TEMPO
RUN ls -lrt
RUN ./prepare && \
    ./configure --prefix=$PSRHOME/tempo && \
    make && \
    make install && \
    rm -rf .git

# pyslalib
ENV PYSLALIB $PSRHOME/pyslalib
ENV PYTHONPATH PYSLALIB/install
WORKDIR $PYSLALIB
RUN python setup.py install --record list.txt --prefix=$PYSLALIB/install && \
    python setup.py clean --all && \
    rm -rf .git

# Presto
ENV PRESTO $PSRHOME/presto
ENV PATH $PATH:$PRESTO/bin
ENV LD_LIBRARY_PATH $PRESTO/lib
ENV PYTHONPATH $PYTHONPATH:$PRESTO/lib/python
WORKDIR $PRESTO/src
RUN rm -rf ../.git
#RUN make makewisdom
RUN make prep && \
    make
WORKDIR $PRESTO/python/ppgplot_src
#RUN mv _ppgplot.c _ppgplot.c_ORIGINAL && \
#    wget https://raw.githubusercontent.com/mserylak/pulsar_docker/master/ppgplot/_ppgplot.c
WORKDIR $PRESTO/python
RUN make && \
    echo "export PYTHONPATH=$PYTHONPATH:$PRESTO/lib/python" >> ~/.bashrc

RUN env | awk '{print "export ",$0}' >> $HOME/.profile
WORKDIR $HOME
RUN git clone https://github.com/zhuww/ubc_AI.git
WORKDIR $HOME/ubc_AI
RUN echo sys.path.append\(\'/home/psr\'\) | cat - quickclf.py > temp && mv temp quickclf.py
RUN echo 'import sys' | cat - quickclf.py > temp && mv temp quickclf.py
COPY J1857+0943_PSR_1857+0943.pfd $HOME/ubc_AI
WORKDIR $HOME 
USER root

