############################################################
# Dockerfile to build a container that runs SigMat in Jupyter
############################################################

# Set the base image to python v3
FROM jupyter/r-notebook

# File Author / Maintainer
MAINTAINER Jinfeng Xiao <jxiao13@illinois.edu>

# Update the repository sources list
RUN Rscript -e 'install.packages(c("kernlab", "e1071", "doParallel", "foreach", "randomForest", "stringr", "optparse"), repos="http://cran.us.r-project.org", dependencies=TRUE)'
COPY data /home/jovyan/data
COPY R_code /home/jovyan/R_code
