FROM ubuntu:16.04


MAINTAINER Prajwal Padmanabh "prajwalvp@mpifr-bonn.mpg.de"

RUN apt-get -y check && \
    apt-get -y update && \
    apt-get install -y apt-utils apt-transport-https software-properties-common python-software-properties && \
    apt-get -y update --fix-missing && \
    apt-get -y upgrade

ENV DEBIAN_FRONTEND noninteractive

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
    libgsl0-dev	\ 
    && rm -rf /var/lib/apt/lists/*


ENV HOME /home/psr
ENV PSRHOME /home/psr/software
ENV OSTYPE linux
RUN mkdir -p /home/psr/software
WORKDIR $PSRHOME


#PGPLOT
#WORKDIR /usr/local/src/
#RUN tar zxvf pgplot5.2.tar.gz && \
#    mkdir /usr/local/pgplot && \
#    cd /usr/local/pgplot && \
#    cp /usr/local/src/drivers.list . &&\
#    /usr/local/src/pgplot/makemake /usr/local/src/pgplot linux g77_gcc_aout && \
#    cat makefile | sed "s;g77;gfortran;g" > makefile.new &&\
#    rm makefile && \
#    mv makefile.new makefile && \
#    make && \
#    make cpg && \
#    make clean && \
#    echo "export PGPLOT_DIR=/usr/local/pgplot" >> ~/.bashrc && \
#    echo "export PGPLOT_DEV=/Xserve" >> ~/.bashrc

#RUN apt-get install libgsl0-dev

WORKDIR $PSRHOME

RUN git clone https://git.code.sf.net/p/pulsareace/code pulsareace-code

RUN rm $PSRHOME/pulsareace-code/makefile

COPY makefile $PSRHOME/pulsareace-code/

WORKDIR $PSRHOME/pulsareace-code

RUN mkdir bin

RUN make 

COPY score.py $PSRHOME/pulsareace-code


