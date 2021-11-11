FROM rocker/tidyverse:latest

RUN apt-get update -qq \
  && apt-get -y --no-install-recommends install \
    default-jdk \
    default-jre \
  && R CMD javareconf \
  && install2.r --error \
    --repos 'http://cran.rstudio.com' \
    h2o
