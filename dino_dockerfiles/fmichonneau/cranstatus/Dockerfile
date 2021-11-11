FROM rocker/r-base
MAINTAINER Francois Michonneau <francois.michonneau@gmail.com>

RUN apt-get update -qq \
  && apt-get upgrade -y \
  && apt-get install -y \
       git-core \
       libssl-dev \
       libcurl4-gnutls-dev \
       libxml2-dev

RUN R -e 'install.packages(c("plumber", "dplyr"))'

RUN R -e 'source("http://install-github.me/fmichonneau/foghorn")'

RUN mkdir -p /app

COPY api.R /app/api.R

EXPOSE 8000
