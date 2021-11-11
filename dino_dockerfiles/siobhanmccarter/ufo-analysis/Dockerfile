# Docker file for ufo_analysis
# Siobhan McCarter, Dec 2017

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install the ezknitr package
RUN Rscript -e "install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"

# install the readr package
RUN Rscript -e "install.packages('readr', repos = 'http://cran.us.r-project.org')"

# install the knitr package
RUN Rscript -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')"

# install the stringr package
RUN Rscript -e "install.packages('stringr', repos = 'http://cran.us.r-project.org')"

# Install packrat
RUN Rscript -e "install.packages('packrat', repos = 'http://cran.us.r-project.org')"
