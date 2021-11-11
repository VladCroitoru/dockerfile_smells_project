# Docker file for data_analysis_pipeline_eg
# Duong Vu
# December 2017


# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# Install devtools
RUN Rscript -e "install.packages('devtools', repos = 'https://cloud.r-project.org')"

# Install packrat
RUN Rscript -e "devtools::install_github('rstudio/packrat')"

# then install the GGally packages
RUN Rscript -e "install.packages('GGally', repos = 'https://cloud.r-project.org')"

# then install the mgcv packages
RUN Rscript -e "install.packages('mgcv', repos = 'https://cloud.r-project.org')"

# Last install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"
