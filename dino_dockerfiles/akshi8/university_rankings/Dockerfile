# Docker file for university_Rankings
# Akshi Chaudhary, 16-12-2017

# use rocker:r-base as base image
FROM rocker/tidyverse

# install the package dependecies
RUN Rscript -e "install.packages('packrat', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('dplyr', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"
RUN Rscript -e "install.packages('forcats', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('stringr', repos = 'http://cran.us.r-project.org')"
