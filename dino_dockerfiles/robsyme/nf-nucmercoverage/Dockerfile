FROM ubuntu:18.04

MAINTAINER Rob Syme <rob.syme@gmail.com>

# Install Nucmer and R
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -qqy mummer r-base samtools

# Install R libraries
RUN Rscript -e "install.packages(c('readr', 'ggplot2', 'dplyr', 'magrittr'))"
