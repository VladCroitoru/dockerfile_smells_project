# Docker file for Titanic survivorship
# Ying Dong, Dec 2017

# use rocker/tidyverse as the base image
FROM rocker/tidyverse

# install the ezknitr package
RUN Rscript -e "install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"

# install the ggplot2 package
RUN Rscript -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')"

# install the packrat package
RUN Rscript -e "install.packages('packrat', repos = 'http://cran.us.r-project.org')"
