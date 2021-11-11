FROM rocker/shiny:3.6.3
MAINTAINER Markus List <markus.list@wzw.tum.de>

#install system packages
RUN apt-get update && apt-get install -y \
libxml2-dev \ 
redis-server \
libcurl4-gnutls-dev \
libssl-dev \
libgmp3-dev \
libmpfr-dev \
libjpeg-dev \
libhiredis-dev

#copy shiny app to work-dir
WORKDIR /srv/
RUN mkdir hitseekr
ADD . hitseekr

#update shiny server conf and configure it to run hitseekr in single app mode
RUN sed -i 's/site_dir \/srv\/shiny-server;/app_dir \/srv\/hitseekr;/g' /etc/shiny-server/shiny-server.conf

# go to project directory
WORKDIR /srv/hitseekr/

#install R packages
ENV RENV_VERSION 0.9.3-86
RUN R -e "install.packages('remotes', repos = c(CRAN = 'https://cloud.r-project.org')); \
  remotes::install_github('rstudio/renv@${RENV_VERSION}'); \
  renv::restore()"
  
#download additional data
RUN wget -r -nd -P data https://exbio.wzw.tum.de/hitseekr-files/ && \
  chown -R shiny data
