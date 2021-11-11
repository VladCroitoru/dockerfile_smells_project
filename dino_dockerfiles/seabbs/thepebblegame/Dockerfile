
## Start rocker r image
FROM rocker/r-ver:3.4.4

MAINTAINER "Sam Abbott" contact@samabbott.co.uk

## Get libs required by packages
RUN apt-get update && \
	apt-get install -y \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    && apt-get clean

## Install R packages - MRAN
RUN Rscript -e 'install.packages(c("shiny", "shinydashboard", "shinyBS", "rmarkdown"))'

RUN Rscript -e 'install.packages(c("dplyr", "tidyr", "tibble", "ggplot2"))'

RUN Rscript -e 'install.packages(c("purrr"))'

ADD . home/thepebblegame

EXPOSE 3838

CMD Rscript -e 'shiny::runApp("home/thepebblegame", port = 3838, host = "0.0.0.0")'
