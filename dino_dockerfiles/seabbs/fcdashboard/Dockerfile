
## Start rocker r image
FROM rocker/r-ver:3.4.4

MAINTAINER "Sam Abbott" contact@samabbott.co.uk

## Get libs required by packages
RUN apt-get update && \
    apt-get install -y \
    libssl-dev \
    libcurl4-openssl-dev \
    libssh2-1-dev \
    libnlopt0 \
    libnlopt-dev \
    libudunits2-dev \
    libxml2-dev \
    libgdal-dev \
    libproj-dev \
    && apt-get clean

## Install R packages - MRAN
RUN Rscript -e 'install.packages(c("pkgconfig", "irlba", "igraph", "shinydashboard"))'

RUN Rscript -e 'install.packages(c("shinyBS", "shinyWidgets", "tidyverse", "DT", "rmarkdown"))'

RUN Rscript -e 'install.packages(c( "e1071", "caret", "ggfortify", "plotly", "lubridate", "wrapr", "stringr"))'

ADD . home/fcdashboard

WORKDIR  home/fcdashboard

EXPOSE 3838

## Create log file
CMD Rscript -e 'shiny::runApp(port = 3838, host = "0.0.0.0")'

