#######################################################
# Dependencies docker image for the GBS Typer pipeline.
#######################################################

FROM ubuntu:20.10
WORKDIR /opt

ARG DEBIAN_FRONTEND=noninteractive

##########################
# Versions
##########################

# Latest freebayes commit [v1.3.3+] (pipeline code specified 0.9.21)
ARG FREEBAYES_VERSION=d7d14dacae4555dcd49daeaf8cf2c41b96e5508c
# Latest srst2 version (pipeline code specified 0.1.7)
ARG SRST2_VERSION=0.2.0
# The following samtools version provides best results for srst2
ARG SAMTOOLS_VERSION=0.1.18
ARG BOWTIE2_VERSION=2.2.9
# Latest prodigal version (as specified in pipeline)
ARG PRODIGAL_VERSION=1:2.6.3-4
# Latest bedtools2 version (pipeline code specified bedtools(1) 2.17.0)
ARG BEDTOOLS_VERSION=2.29.2+dfsg-3build2
# Biopython used by pipleline python scripts
ARG BIOPYTHON_VERSION=1.78
# Python2 for srst2
ARG PYTHON2_VERSION=2.7

##########################
# Installation
##########################

# Base system
RUN apt-get update -y -qq && apt-get install -y -qq \
        locales \
        software-properties-common \
        wget \
        curl \
        unzip \
        meson \
        ninja-build \
        build-essential \
        cmake \
        bzip2 \
        git \
        perl \
        ncbi-blast+ \
        bedtools=${BEDTOOLS_VERSION} \
        prodigal=${PRODIGAL_VERSION} \
        tabix \
        python3-pip \
        vcftools \
        libbz2-dev \
        zlib1g-dev \
        liblzma-dev \
        pkg-config \
        libncurses5-dev \
      && add-apt-repository universe \
      && apt-get update -y -qq \
      && apt-get -y -qq install python${PYTHON2_VERSION} \
      && ln -sf /usr/bin/python${PYTHON2_VERSION} /usr/bin/python \
      && curl https://bootstrap.pypa.io/pip/2.6/get-pip.py --output get-pip.py \
      && python get-pip.py \
      && rm get-pip.py \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/* \
      && sed -i -e 's/# \(en_GB\.UTF-8 .*\)/\1/' /etc/locale.gen \
      && touch /usr/share/locale/locale.alias \
      && locale-gen

# Perl locales
ENV LANG en_GB.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL en_GB.UTF-8

# Python3 libraries
RUN pip3 install pandas

# Biopython
RUN wget -q http://biopython.org/DIST/biopython-${BIOPYTHON_VERSION}.tar.gz \
    && pip3 install biopython-${BIOPYTHON_VERSION}.tar.gz \
    && rm biopython-${BIOPYTHON_VERSION}.tar.gz

# srst2 install
RUN pip install "scipy>=0.12.0" \
    && pip install git+https://github.com/katholt/srst2@v${SRST2_VERSION}

# samtools compatible with srst2
RUN cd /tmp \
    && wget -q https://sourceforge.net/projects/samtools/files/samtools/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2/download \
        -O samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && tar xf samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && cd samtools-${SAMTOOLS_VERSION} \
    && make \
    && mv samtools /usr/local/bin \
    && cd /tmp \
    && rm -rf samtools*

# bowtie compatible with srst2
RUN wget -q https://sourceforge.net/projects/bowtie-bio/files/bowtie2/${BOWTIE2_VERSION}/bowtie2-${BOWTIE2_VERSION}-linux-x86_64.zip/download \
        -O bowtie2-${BOWTIE2_VERSION}-linux-x86_64.zip \
    && unzip bowtie2-${BOWTIE2_VERSION}-linux-x86_64.zip \
    && rm bowtie2-${BOWTIE2_VERSION}-linux-x86_64.zip
ENV PATH="/opt/bowtie2-${BOWTIE2_VERSION}:${PATH}"

# freebayes
RUN cd /tmp \
    && git clone --recursive https://github.com/freebayes/freebayes \
    && cd freebayes \
    && git checkout ${FREEBAYES_VERSION} --recurse-submodules \
    && meson build/ --buildtype debug \
    && cd build \
    && ninja \
    && mv freebayes /usr/local/bin \
    && mv bamleftalign /usr/local/bin \
    && cd /tmp \
    && rm -rf freebayes

# Clean up
RUN apt-get purge -y -qq build-essential wget curl git meson ninja-build cmake pkg-config python3-pip
