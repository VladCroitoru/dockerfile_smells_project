FROM rocker/hadleyverse

MAINTAINER "Federico Marini" marinif@uni-mainz.de

USER root

# unix additional dependencies
RUN apt-get update && apt-get install -y --force-yes \
    libjpeg-dev \
    libtiff5-dev \
    libfftw3-dev

# install correspondent version of biocLite and flowcatchR with dependencies
ADD intoTheFlow_studio.R /tmp/
RUN R -f /tmp/intoTheFlow_studio.R 

# provide a sample script to be ready for trying when opening RStudio
ADD demo_fullRun.R /home/rstudio/

