FROM rocker/shiny

MAINTAINER "Federico Marini" marinif@uni-mainz.de

USER root

# unix additional dependencies
RUN apt-get update && apt-get install -y --force-yes\
    libglu1-mesa-dev \
    libjpeg-dev \
    libtiff5-dev \
    libX11-dev \
    libcairo2-dev \
    libfftw3-dev 

# install correspondent version of biocLite, shiny and flowcatchR with dependencies
ADD intoTheFlow_shiny.R /tmp/
RUN R -f /tmp/intoTheFlow_shiny.R 

# copy shinyFlow shiny app from package to destination directory
RUN echo "cat(system.file('shiny', package='flowcatchR'))" \
  > /home/docker/pathToShinyflow.R \
  && loc=$(Rscript /home/docker/pathToShinyflow.R) \
  && cp -R $loc /srv/shiny-server/shinyFlow \
  && rm /home/docker/pathToShinyflow.R
