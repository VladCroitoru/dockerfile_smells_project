#################################################################
# Dockerfile
#
# Software:         VEP
# Software Version: 86
# Description:      Variant Effect Predictor
# Website:          http://uswest.ensembl.org/info/docs/tools/vep/index.html
# Base Image:       ubuntu 14.04
# Run Cmd:          docker run vep perl variant_effect_predictor.pl
#################################################################
FROM ubuntu:14.04

MAINTAINER Adam Struck <strucka@ohsu.edu>

ENV HOME /home
ENV VEP_PATH /home/vep
ENV PATH $VEP_PATH/htslib:$PATH
ENV PERL5LIB $VEP_PATH:/opt/lib/perl5:$PERL5LIB

# Install compiler and other dependencies
RUN apt-get update && \
    apt-get install --yes \
    build-essential \
    libarchive-zip-perl \
    libdbd-mysql-perl \
    libjson-perl \
    libwww-perl \
    cpanminus \
    zlib1g-dev \
    git \
    curl \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# set up variable for install
ENV ENSEMBL_TOOLS_VERSION=86

WORKDIR /opt/

# download vep
RUN curl -LO https://github.com/Ensembl/ensembl-tools/archive/release/${ENSEMBL_TOOLS_VERSION}.tar.gz && \
    tar -zxvf ${ENSEMBL_TOOLS_VERSION}.tar.gz && \
    mkdir $VEP_PATH && \
    mv ensembl-tools-release-${ENSEMBL_TOOLS_VERSION}/scripts/variant_effect_predictor/* $VEP_PATH && \
    ln -s $VEP_PATH/variant_effect_predictor.pl /usr/local/bin/ && \
    rm -rf *

# install perl dependencies
RUN cpanm --mirror http://cpan.metacpan.org -l /opt/ File::Copy::Recursive Module::Build && \
    rm -rf ~/.cpanm

# install VEP and plugins
RUN cd $VEP_PATH && \
    perl INSTALL.pl --AUTO ap --SPECIES homo_sapiens --ASSEMBLY GRCh37,GrCh38 --PLUGINS all -c /vep-cache

WORKDIR /tmp/

CMD ["variant_effect_predictor.pl"]
