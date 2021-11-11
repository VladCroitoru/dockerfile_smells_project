
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
RUN Rscript -e 'install.packages(c("shiny", "shinydashboard"))'

Run Rscript -e 'install.packages(c("tibble", "dplyr", "tidyr", "ggplot2"))'

RUN Rscript -e 'install.packages(c("DT", "rmarkdown", "plotly", "deSolve"))'

ADD . home/intro_to_tb_models

EXPOSE 3838

CMD Rscript -e 'shiny::runApp("home/intro_to_tb_models", port = 3838, host = "0.0.0.0")'

