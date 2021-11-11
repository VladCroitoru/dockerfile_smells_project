################################################################################
##################### Set Inital Image to work from ############################
FROM griffithlab/regtools:latest

################################################################################
##################### Add Container Labels #####################################
LABEL "Description"="This is a docker image to aid in the regtools cwl workflow"

################################################################################
##################### Install System Dependencies ##############################
RUN apt-get update -y && apt-get install -y \
    r-base

RUN Rscript -e 'install.packages("data.table", repos="http://cran.us.r-project.org")'
