# Set the base image to debian jessie
FROM debian:jessie

# File Author / Maintainer
MAINTAINER Clement Goubert <goubert.clement@gmail.com>

# install base programs
RUN apt-get update && apt-get install --yes --no-install-recommends \
    wget \
    curl \
    ca-certificates \
    locales \
    vim-tiny \
    nano \
    git \
    make \
    cmake \
    build-essential \
    gcc-multilib \
    perl \
    bioperl \
    cpanminus \
    expat \
    libexpat1-dev \
    python \
    parallel \
    tabix \
    autoconf \
    libbz2-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    liblzma-dev

# install bedtools 2.29.1 (bedtools must be this version for compatibility)
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.30.0/bedtools.static.binary \
&& mv bedtools.static.binary bedtools \
&& chmod a+x bedtools \
&& mv bedtools /usr/bin/

# install perl modules
RUN cpanm --force XML::Parser \
	XML::DOM \
	XML::Twig \
	String::Approx \
	List::MoreUtils

# Update/Upgrade pip and install pysam
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py \
&&  python get-pip.py \
&&  pip install pysam

# install htslib

RUN cd /usr/bin \
&&  wget https://github.com/samtools/htslib/releases/download/1.10.2/htslib-1.10.2.tar.bz2 \
&&  tar -vxjf htslib-1.10.2.tar.bz2 \
&&  cd htslib-1.10.2 \
&&  make

# install samtools
RUN cd /usr/bin \
&&  wget https://github.com/samtools/samtools/releases/download/1.10/samtools-1.10.tar.bz2 \
&&  tar -vxjf samtools-1.10.tar.bz2 \
&&  cd samtools-1.10 \
&&  make

# install bwa 
RUN git clone https://github.com/lh3/bwa.git \
&&  cd bwa \
&&  make


# install autotools
RUN apt-get install --yes --no-install-recommends \
    pkg-config \
    autotools-dev \
    automake

# install vcftools 0.1.16
RUN wget https://github.com/vcftools/vcftools/archive/refs/tags/v0.1.16.tar.gz \
&& tar -zxvf v0.1.16.tar.gz \
&& cd vcftools-0.1.16/ \
&& ./autogen.sh \
&& ./configure \
&& make \
&& make install

#Export paths
ENV PATH=/usr/bin/samtools-1.10:$PATH
ENV PATH=/usr/bin/htslib-1.10.2:$PATH
ENV PATH=/bwa:$PATH
