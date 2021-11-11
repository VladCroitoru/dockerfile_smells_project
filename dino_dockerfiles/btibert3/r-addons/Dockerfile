FROM rocker/tidyverse
MAINTAINER "Brock Tibert" btibert3@gmail.com

## Some setup for things we need
RUN apt-get update && apt-get install -y \
    libssl-dev \
    libsasl2-dev

## Manually install (useful packages from) the SUGGESTS list of the above packages.
## (because --deps TRUE can fail when packages are added/removed from CRAN)
RUN install2.r --error \
    -r "https://cran.rstudio.com" \
    -r "http://www.bioconductor.org/packages/release/bioc" \
  && r -e 'source("https://raw.githubusercontent.com/MangoTheCat/remotes/master/install-github.R")$value("mangothecat/remotes")' \
  && r -e 'install.packages("tidyverse")' \
  && r -e 'install.packages("neo4r")' \	
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds
