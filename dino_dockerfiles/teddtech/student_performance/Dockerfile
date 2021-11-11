# Docker file for student_performance
# Ted Thompson, Dec, 2017

### Code is based on Tiffany Timber's code for the data_analysis_pipeline_eg


# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# then install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"
