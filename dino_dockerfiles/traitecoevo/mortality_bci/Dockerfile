FROM rocker/tidyverse:3.5.1
LABEL maintainer="James Camac"
LABEL email="james.camac@gmail.com"

# Install latex, git and clang then clean up tmp files
RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
         clang \
         zip \
         unzip \
         gdal-bin \
         libomp-dev \
         libudunits2-dev \
         libgdal-dev \
         libproj-dev \
         libglu1-mesa-dev \
         mesa-common-dev \
         python-dev \
         python-gdal \
         python-numpy \
         default-jdk \
         ghostscript \
         libbz2-dev \
         libicu-dev \
         liblzma-dev \
         libhunspell-dev \
         libmagick++-dev \
         librdf0-dev \
         libv8-dev \
         qpdf \
         lmodern \
         texlive-fonts-recommended \
         texlive-generic-recommended \
         texlive-humanities \
         texlive-latex-extra \
         texlive-science \
         texinfo

# Global site-wide config
RUN mkdir -p $HOME/.R/ \
    && echo "\nCXXFLAGS=-O3 -mtune=native -march=native -Wno-unused-variable -Wno-unused-function\n" >> $HOME/.R/Makevars \
    && echo "\nCXX=clang++ -ftemplate-depth-256\n" >> $HOME/.R/Makevars \
    && echo "CC=clang\n" >> $HOME/.R/Makevars

# Install other dependent R packages (installed in batches to overcome dependency issues)

RUN . /etc/environment \
  && install2.r --error --repos $MRAN --deps TRUE \
 R6 yaml digest crayon getopt optparse downloader raster Hmisc rstan pbmcapply pROC
  
RUN . /etc/environment \
  && install2.r --error --repos $MRAN --deps FALSE \
  cowplot gridBase png reshape progress GGally

# Install remake
RUN installGithub.r \
    --deps "TRUE" \
    richfitz/storr \
    richfitz/remake

# Remove unnecesarry tmp files
RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds

# Set working directory
WORKDIR /home/mortality_bci/