FROM ubuntu:20.04
MAINTAINER David Spencer <dspencer@wustl.edu>

LABEL Image for basic ad-hoc bioinformatic analyses

ENV DEBIAN_FRONTEND=noninteractive

#some basic tools
RUN apt-get update && apt-get install -y --no-install-recommends locales && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    LC_ALL=en_US.UTF-8 && \
    LANG=en_US.UTF-8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8 && \
    TERM=xterm

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
    bzip2 \
    curl \
    default-jdk \
    default-jre \
    emacs \
    emacs-goodies-el \
    g++ \
    git \
    less \
    libcurl4-openssl-dev \
    libpng-dev \
    libssl-dev \
    libxml2-dev \
    make \
    ncurses-dev \
    nodejs \
    pkg-config \
    python3.6 \
    python3-pip \
    python3-dev \
    rsync \
    unzip \
    wget \
    zip \
    libbz2-dev \
    bash-completion \
    ca-certificates \
    file \
    fonts-texgyre \
    g++ \
    gfortran \
    gsfonts \
    libbz2-1.0 \
    libjpeg-turbo8 \
    libopenblas-dev \
    libpangocairo-1.0-0 \
    libpcre3 \
    libtiff5 \
    liblzma5 \
    locales \
    zlib1g \
    libbz2-dev \
    libcairo2-dev \
    libcurl4-openssl-dev \
    libpango1.0-dev \
    libjpeg-dev \
    libicu-dev \
    libpcre3-dev \
    libpng-dev \
    libreadline-dev \
    libtiff5-dev \
    liblzma-dev \
    libx11-dev \
    libxt-dev \
    perl \
    texinfo \
    texlive-extra-utils \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-recommended \
    x11proto-core-dev \
    xauth \
    xfonts-base \
    xvfb \
    zlib1g-dev \
    bc \
    bedtools

##############
#HTSlib 1.13#
##############
ENV HTSLIB_INSTALL_DIR=/opt/htslib

WORKDIR /tmp
RUN wget https://github.com/samtools/htslib/releases/download/1.13/htslib-1.13.tar.bz2 && \
    tar --bzip2 -xvf htslib-1.13.tar.bz2 && \
    cd /tmp/htslib-1.13 && \
    ./configure  --enable-plugins --prefix=$HTSLIB_INSTALL_DIR && \
    make && \
    make install && \
    cp $HTSLIB_INSTALL_DIR/lib/libhts.so* /usr/lib/ && \
    ln -s $HTSLIB_INSTALL_DIR/bin/tabix /usr/bin/tabix && \
    ln -s $HTSLIB_INSTALL_DIR/bin/bgzip /usr/bin/bgzip && \
    rm -Rf /tmp/htslib-1.13

################
#Samtools 1.13#
################
ENV SAMTOOLS_INSTALL_DIR=/opt/samtools

WORKDIR /tmp
RUN wget https://github.com/samtools/samtools/releases/download/1.13/samtools-1.13.tar.bz2 && \
    tar --bzip2 -xf samtools-1.13.tar.bz2 && \
    cd /tmp/samtools-1.13 && \
    ./configure --with-htslib=$HTSLIB_INSTALL_DIR --prefix=$SAMTOOLS_INSTALL_DIR && \
    make && \
    make install && \
    ln -s /opt/samtools/bin/* /usr/local/bin/ && \
    cd / && \
    rm -rf /tmp/samtools-1.13

################
#bcftools 1.13#
################
ENV BCFTOOLS_INSTALL_DIR=/opt/bcftools
WORKDIR /tmp
RUN wget https://github.com/samtools/bcftools/releases/download/1.13/bcftools-1.13.tar.bz2 && \
    tar --bzip2 -xf bcftools-1.13.tar.bz2 && \
    cd /tmp/bcftools-1.13 && \
    make prefix=$BCFTOOLS_INSTALL_DIR && \
    make prefix=$BCFTOOLS_INSTALL_DIR install && \
    ln -s /opt/bcftools/bin/* /usr/local/bin/ && \
    cd / && \
    rm -rf /tmp/bcftools-1.13


##############
#Picard 2.21.6#
##############
ENV picard_version 2.21.6

# Assumes Dockerfile lives in root of the git repo. Pull source files into
# container
RUN apt-get update && apt-get install ant --no-install-recommends -y && \
    cd /usr/ && \
    git config --global http.sslVerify false && \
    git clone --recursive https://github.com/broadinstitute/picard.git && \
    cd /usr/picard && \
    git checkout tags/${picard_version} && \
    ./gradlew shadowJar && \
    cp ./build/libs/picard.jar . && \
    echo '#!/bin/bash'"\n"'java -Xmx16g -jar /usr/picard/picard.jar $@' > /usr/local/bin/picard && \
    chmod a+x /usr/local/bin/picard
    

##############
## vcftools ##
ENV ZIP=vcftools-0.1.14.tar.gz
ENV URL=https://github.com/vcftools/vcftools/releases/download/v0.1.14/
ENV FOLDER=vcftools-0.1.14
ENV DST=/tmp

RUN wget $URL/$ZIP -O $DST/$ZIP && \
    tar xvf $DST/$ZIP -C $DST && \
    rm $DST/$ZIP && \
    cd $DST/$FOLDER && \
    ./configure && \
    make && \
    make install && \
    cd / && \
    rm -rf $DST/$FOLDER


##################
# ucsc utilities #
RUN mkdir -p /tmp/ucsc && \
    cd /tmp/ucsc && \
    wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedToBigBed http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bigBedToBed http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bigWigAverageOverBed http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bigWigToBedGraph http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/wigToBigWig && \
    chmod ugo+x * && \
    mv * /usr/bin/

############################
# R, bioconductor packages #
RUN apt-get install -y r-base

## install r packages, bioconductor, etc ##
ADD rpackages.R /tmp/
RUN R -f /tmp/rpackages.R 
   
RUN apt-get autoremove -y && \
    apt-get autoclean -y && \
    apt-get clean

#################################
# Python 3, plus packages

# Configure environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

# Install conda
RUN cd /tmp && \
    mkdir -p $CONDA_DIR && \
    curl -s https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh && \
    /bin/bash miniconda.sh -f -b -p $CONDA_DIR && \
    rm miniconda.sh && \
    $CONDA_DIR/bin/conda config --system --add channels conda-forge && \
    $CONDA_DIR/bin/conda config --system --set auto_update_conda false && \
    conda clean -tipsy

# Install Python 3 packages available through pip 
RUN conda install --yes 'pip' && \
    conda clean -tipsy && \
    pip install numpy && \
    pip install cruzdb && \
    pip install cython && \
    pip install pyensembl && \
    pip install pyfaidx && \
    pip install pybedtools && \
    pip install cyvcf2 && \
    pip install intervaltree_bio && \
    pip install pandas && \
    pip install scipy && \
    pip install scikit-learn && \
    pip install pysam && \
    pip install statsmodels && \
    pip install pyranges && \
    pip install pyyaml
    
RUN ln -s $(which python3) /usr/local/bin/python

# needed for MGI data mounts
RUN apt-get update && apt-get install -y libnss-sss && apt-get clean all

#set timezone to CDT
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime
#LSF: Java bug that need to change the /etc/timezone.
#     The above /etc/localtime is not enough.
RUN echo "America/Chicago" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# some other utils
RUN apt-get update && apt-get install -y --no-install-recommends gawk openssh-client grep evince && apt-get clean all

RUN cpan install Statistics::Basic && cpan install JSON && cpan install List::Util && cpan install YAML::Tiny

RUN pip install hic2cool && pip install cooler

RUN pip install biopython

RUN conda install gh --channel conda-forge

RUN mkdir /tmp/bin
ENV PATH=/bin:/usr/bin:/usr/local/bin:/opt/conda/bin/:${PATH}

