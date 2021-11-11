# Docker file for the project investment_analysis
# Esteban Angel, Dec, 2017
# This script sets up the Docker container with the tools needed for executing the investment analysis project.


# use rocker/tidyverse as the base image
FROM rocker/tidyverse

# install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"

# install the broom package
RUN Rscript -e "install.packages('broom', repos = 'http://cran.us.r-project.org')"

# install the packrat package
RUN Rscript -e "install.packages('packrat', repos = 'http://cran.us.r-project.org')"

# install the forcats package
RUN Rscript -e "install.packages('forcats', repos = 'http://cran.us.r-project.org')"
