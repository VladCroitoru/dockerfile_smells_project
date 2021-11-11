FROM r-base:3.5.1
#FROM rocker/r-devel:latest
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
   libfftw3-dev \
   gcc \
   git-all \
   file \
   libapparmor1 \
   libcurl4-openssl-dev \
   libedit2 \
   libssl-dev \
   lsb-release \
   psmisc \
   procps \
   libxml2-dev \
   pkg-config \
   libcairo2-dev \
   libmagick++-dev \
   postgresql postgresql-contrib libpq-dev libudunits2-dev libx11-dev mesa-common-dev libglu1-mesa-dev libhdf5-dev gfortran && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY install.packages.R /opt/.
RUN Rscript /opt/install.packages.R
WORKDIR /opt
RUN git clone https://github.com/stevetsa/BISCUIT_SingleCell_IMM_ICML_2016
COPY Dockerfile /opt/Dockerfile

## Add Example 
WORKDIR /opt/BISCUIT_SingleCell_IMM_ICML_2016/
RUN wget https://storage.googleapis.com/linnarsson-lab-www-blobs/blobs/cortex/expression_mRNA_17-Aug-2014.txt

ENV PATH="$PATH:/opt"
