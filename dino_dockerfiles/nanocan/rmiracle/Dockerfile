FROM rocker/shiny:latest
MAINTAINER Markus List <mlist@mpi-inf.mpg.de>

#install system packages
RUN apt-get update
RUN apt-get install -y libxml2-dev libcurl4-gnutls-dev libssl-dev 

RUN R -e "source('https://bioconductor.org/biocLite.R');biocLite('limma')"

#copy R code into image
RUN mkdir /rmiracle
ADD . /rmiracle
RUN R -e "install.packages('devtools');install.packages('survival');devtools::install_local('/rmiracle')"

#copy shiny app to work-dir
WORKDIR /srv/
RUN mkdir rmiracle
ADD ./inst/shiny.batch.analysis/ rmiracle/

#update shiny server conf and configure it to run rmiracle in single app mode
RUN chown -R shiny rmiracle/ && \
sed -i 's/site_dir \/srv\/shiny-server;/app_dir \/srv\/rmiracle;/g' /etc/shiny-server/shiny-server.conf

