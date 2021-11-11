##NCBI Hackathon Product
FROM ubuntu:latest
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>

RUN apt-get update && apt-get install --yes \
 build-essential \
 gcc-multilib \
 apt-utils \
 zlib1g-dev \
 vim-common \
 wget \
 libncurses5-dev \
 autotools-dev \
 autoconf \
 git \
 perl \
# r-base \
# python \
 libbz2-dev \
 liblzma-dev \
 apt-utils \
 libz-dev \
 ncurses-dev \
 zlib1g-dev \
 libcurl3 \
 libcurl4-openssl-dev \
 libxml2-dev \
 zip \
 default-jre \
 default-jdk \
 libssl-dev

WORKDIR /opt/
RUN wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
RUN tar xvzf sratoolkit.current-ubuntu64.tar.gz
WORKDIR /opt/sratoolkit.2.9.0-ubuntu64
ENV PATH "$PATH: /opt/sratoolkit.2.9.0-ubuntu64/bin/"
RUN apt-get install -y unzip

WORKDIR /opt/
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/1.3.0/ncbi-magicblast-1.3.0-x64-linux.tar.gz
RUN tar xvzf ncbi-magicblast-1.3.0-x64-linux.tar.gz
WORKDIR /opt/ncbi-magicblast-1.3.0
ENV PATH "$PATH:/opt/ncbi-magicblast-1.3.0/bin/"

WORKDIR /opt
RUN git clone https://github.com/samtools/htslib.git
WORKDIR /opt/htslib
RUN autoheader
RUN autoconf
RUN ./configure
RUN make
RUN make install
ENV PATH "$PATH:/opt/htslib/"

WORKDIR /opt
RUN git clone https://github.com/samtools/samtools.git
WORKDIR /opt/samtools
RUN autoheader
RUN autoconf -Wno-syntax
RUN ./configure    # Optional, needed for choosing optional functionality
RUN make
RUN make install
ENV PATH "$PATH:/opt/samtools/"

WORKDIR /opt/
RUN wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
RUN tar xvzf sratoolkit.current-ubuntu64.tar.gz
WORKDIR /opt/sratoolkit.2.9.0-ubuntu64
ENV PATH "$PATH: /opt/sratoolkit.2.9.0-ubuntu64/bin/"
RUN apt-get install -y unzip

WORKDIR /opt/
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/1.3.0/ncbi-magicblast-1.3.0-x64-linux.tar.gz
RUN tar xvzf ncbi-magicblast-1.3.0-x64-linux.tar.gz
WORKDIR /opt/ncbi-magicblast-1.3.0
ENV PATH "$PATH:/opt/ncbi-magicblast-1.3.0/bin/"

WORKDIR /opt
RUN wget https://sourceforge.net/projects/subread/files/subread-1.6.0/subread-1.6.0-Linux-x86_64.tar.gz
RUN tar xvzf subread-1.6.0-Linux-x86_64.tar.gz
ENV PATH "$PATH:/opt/subread-1.6.0-Linux-x86_64/bin/"

WORKDIR /opt
RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip
RUN unzip fastqc_v0.11.7.zip
WORKDIR FastQC
RUN chmod 755 fastqc
WORKDIR /opt
RUN ln -s /opt/FastQC/fastqc /usr/local/bin/fastqc

WORKDIR /opt
RUN wget ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
RUN tar xvzf edirect.tar.gz
WORKDIR /opt/edirect
RUN sh setup.sh
RUN cpan LWP::Protocol::https
ENV PATH "$PATH:/opt/edirect/"

#WORKDIR /opt
#RUN git clone https://github.com/lh3/seqtk.git  
#WORKDIR /opt/seqtk
#RUN make
#ENV PATH "$PATH:/opt/seqtk/"
