# Docker file for BC-motor-vehicle-incidents
# Bradley Pick, Dec. 2017
#
# this dockerfile is used in the automated build of the docker image
# that can be used for easy replication of the BC-motor-vehicle-incidents p
# project

# Use rocker/tidyverse as a base image
FROM rocker/tidyverse

# Install ezknitr
RUN Rscript -e "install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"

# Install cowplot
RUN Rscript -e "install.packages('cowplot', repos = 'http://cran.us.r-project.org')"

# Install packrat
RUN Rscript -e "install.packages('packrat', repos = 'http://cran.us.r-project.org')"
