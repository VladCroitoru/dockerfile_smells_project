## Adds ffmpeg and ghostscript to rocker/geospatial

FROM rocker/geospatial:3.5.1

MAINTAINER Kyle Bocinsky <bocinsky@gmail.com>

RUN apt-get update

## ffmpeg
RUN apt-get install -y --no-install-recommends \
  git \
  libx264-dev \
  yasm \
  && git clone --depth 1 git://source.ffmpeg.org/ffmpeg \
  && cd ffmpeg \
  && ./configure --enable-gpl --enable-libx264 \
  && make -j4 \
  && make install \
  && cd .. \
  rm -rf ffmpeg

## ghostscript
RUN apt-get install -y --no-install-recommends \
    ghostscript \
    apt-transport-https \
    ca-certificates \
    gnupg \
    curl \
    software-properties-common

## Install R package dependencies from stable MRAN repo
RUN install2.r --error \
    ## Packages for Python-like command-line parsing
    devtools \
    optparse \
    ## Package for data aquisition
    FedData \
    ## Packages offering general utilities
    R.utils \
    Hmisc \
    zoo \
    abind \
    mgcv \
    rgbif \
    fields \
    ## Packages for tidy code
    ggthemes \
    purrrlyr \
    ## Plotting
    htmlwidgets \
    plotly \
    bibtex \
    knitcitations

## Update ggplot2 to development version (need 2.2.1.9000 for geom_sf function)
RUN r -e 'devtools::install_github("tidyverse/ggplot2")'
