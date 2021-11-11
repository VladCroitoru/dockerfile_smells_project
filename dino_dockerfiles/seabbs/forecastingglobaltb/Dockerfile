## Start with the shiny docker image
FROM rocker/tidyverse:latest

MAINTAINER "Sam Abbott" contact@samabbott.co.uk

RUN apt-get update -qq \
  && apt-get -y --no-install-recommends install \
    default-jdk \
    default-jre \
  && R CMD javareconf \
  && install2.r --error \
    --repos 'http://cran.rstudio.com' \
    h2o

EXPOSE 54321

ADD . /home/rstudio/ForecastingGlobalTB

RUN Rscript -e 'install.packages(c("getTBinR", "h2o"))'