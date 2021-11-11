FROM ubuntu:latest
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>

RUN apt-get update && apt-get install --yes \
 build-essential \
 autoconf \
 libtool \
 pkg-config \
 wget \
 git \
 python-pip \
 python-dev \
 python-setuptools \
 python-biopython \
 mercurial \
 perl \
 unzip \
 nano \
 bzip2

RUN mkdir /tools
## install SRA tool kit
WORKDIR /tools
RUN wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
RUN tar xvzf sratoolkit.current-ubuntu64.tar.gz
WORKDIR /tools/sratoolkit.2.9.0-ubuntu64
ENV PATH="/tools/sratoolkit.2.9.0-ubuntu64/bin:${PATH}"

## Install HUMANN2
RUN pip install --upgrade pip 
RUN pip install humann2

## Install metaphlan
WORKDIR /tools
# Install some pre-reqs needed
RUN wget -O /tools/hclust2.zip https://bitbucket.org/nsegata/hclust2/get/tip.zip
RUN unzip -d /tools/hclust2 /tools/hclust2.zip
RUN mv /tools/hclust2/nsegata-hclust2-*/* /tools/hclust2/
RUN rm -rf /tools/hclust2/nsegata-hclust2-*
ENV PATH $PATH:/tools/hclust2

# These have to be done sequentially, as there's a current problem with the dependency order resolution
RUN pip install numpy
RUN pip install matplotlib scipy biom-format h5py

RUN wget -O /tools/metaphlan2.zip https://bitbucket.org/biobakery/metaphlan2/get/default.zip
RUN unzip -d /tools/ /tools/metaphlan2.zip
WORKDIR /tools
RUN mv biobakery-metaphlan2* metaphlan2
ENV PATH $PATH:/tools/metaphlan2/:/tools/metaphlan2/utils
ENV MPA_DIR /tools/metaphlan2/

## Install BowTie2
WORKDIR /tools
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.1/bowtie2-2.3.4.1-linux-x86_64.zip
RUN unzip bowtie2-2.3.4.1-linux-x86_64.zip

## Install Aspera
RUN wget https://download.asperasoft.com/download/sw/cli/3.7.7/aspera-cli-3.7.7.608.927cce8-linux-64-release.sh
RUN bash aspera-cli-3.7.7.608.927cce8-linux-64-release.sh
ENV PATH="/root/.aspera/cli/bin:${PATH}"

WORKDIR /
#RUN git clone https://github.com/waldronlab/curatedMetagenomicDataHighLoad.git
#RUN git clone https://github.com/stevetsa/curatedMetagenomicDataHighLoad.git

RUN pip install awscli --upgrade --user
ENV PATH="~/.local/bin:${PATH}"
