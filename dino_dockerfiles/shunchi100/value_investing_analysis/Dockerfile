# Docker file for value_investing project
# Shun CHI, Dec, 2017
# image can be found in https://hub.docker.com/r/shunchi100/value_investing_analysis/

# use rocker/tidyverse as the base image
FROM rocker/tidyverse:latest

# Make ~/.R
RUN mkdir -p $HOME/.R

# install XLConnect
# Note: libaries liblzma, libbz2, and java is missing in the rocker/tidyverse.
RUN apt-get update -qq \
    && apt-get -y --no-install-recommends install \
    liblzma-dev \
    libbz2-dev \
    clang  \
    ccache \
    default-jdk \
    default-jre \
    && R CMD javareconf \
    && install2.r --error \
        XLConnect \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
&& rm -rf /var/lib/apt/lists/*

# install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"

# install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# get python package dependencies
RUN apt-get install -y python3-tk

# install numpy & matplotlib
RUN pip3 install pandas
RUN pip3 install requests
RUN pip3 install argparse
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*
