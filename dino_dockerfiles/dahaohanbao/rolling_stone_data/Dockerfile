
# Docker file for rolling_stone_data
# Fang Yang, Dec, 2017

# use rocker/tidyverse as the base image
FROM rocker/tidyverse

# install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"

# install the knitr packages
RUN Rscript -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')"
