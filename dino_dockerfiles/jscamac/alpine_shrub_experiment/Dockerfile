FROM rocker/tidyverse:3.5.3
MAINTAINER James Camac <james.camac@gmail.com>

# Install latex, git and clang then clean up tmp files
RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
         libcurl4-openssl-dev \
         texlive-latex-recommended \
         texlive-latex-extra \
         texlive-humanities \
         texlive-fonts-recommended \
         texlive-science \
         lmodern \
         libomp-dev \
         git \
         clang \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf var/lib/apt/lists/*

# Global site-wide config
RUN mkdir -p $HOME/.R/ \
    && echo "\nCXXFLAGS=-O3 -mtune=native -march=native -Wno-unused-variable -Wno-unused-function\n" >> $HOME/.R/Makevars \
    && echo "\nCXX=clang++ -ftemplate-depth-256\n" >> $HOME/.R/Makevars \
    && echo "CC=clang\n" >> $HOME/.R/Makevars

# Install other dependent R packages
RUN install2.r -r "https://mran.revolutionanalytics.com/snapshot/2019-04-01/" --error \
    --deps "FALSE" \
    Rcpp RcppEigen BH matrixStats backports checkmate loo inline gridExtra StanHeaders rstan plyr stringr reshape2 cowplot lubridate

# Install remake
RUN installGithub.r \
    --deps "TRUE" \
    richfitz/remake

# Remove unnecesarry tmp files
RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds

# Set working directory
WORKDIR /home/Alpine_Shrub_Experiment