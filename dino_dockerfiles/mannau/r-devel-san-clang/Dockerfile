## Emacs, make this -*- mode: sh; -*-

## start with the Docker 'base R' Debian-based image
FROM rocker/r-devel-ubsan-clang:latest

MAINTAINER "Mario Annau" mario.annau@gmail.com

ENV LD_LIBRARY_PATH=/usr/local/lib
ENV ASAN_OPTIONS=detect_leaks=0

# Install apt dependencies
RUN apt-get update -qq \
	&& apt-get install -t unstable -y --no-install-recommends libxml2-dev pandoc

# Use HDF5 Release version 1.10.1 with ASAN fixes
RUN git clone -b hdf5_1_10_1 https://github.com/mannau/hdf5.git

# Install HFD5 from source
RUN cd hdf5 \
    && ./configure --prefix=/usr/local \
    && make install \
    && cd ..

# Install R dependencies
RUN ASAN_OPTIONS=detect_leaks=0 RD --slave -e "install.packages(c('Rcpp', 'testthat', 'roxygen2', 'highlight', 'zoo', 'microbenchmark', 'nycflights13', 'bit64', 'knitr', 'rmarkdown', 'stringi', 'formatR', 'reshape2'))"
