# Base image https://hub.docker.com/u/rocker/
FROM rocker/rstudio:latest

# Instalaciones sistema
RUN apt-get update && yes | apt-get install libssl-dev \ 
	libfontconfig1-dev \ 
	libudunits2-dev \ 
	libxml2-dev \
	libcurl4-openssl-dev \ 
	libgdal-dev \
	libproj-dev \
	libgeos-dev
	
## install R-packages
RUN mkdir -p /project_1
COPY install_packages.R /project_1/install_packages.R
RUN Rscript /project_1/install_packages.R

## create directories
RUN mkdir -p /project_1/estados
RUN mkdir -p /project_1/www

## copy files
COPY /estados/* /project_1/estados/
COPY /www/* /project_1/www/
COPY refugios_nayarit.xlsx /project_1/refugios_nayarit.xlsx
COPY exec_.R /project_1/exec.R
COPY proyecto1_etl_.R /project_1/proyecto1_etl.R
COPY proyecto_1_eda_.Rmd /project_1/proyecto_1_eda.Rmd
COPY app_.R /project_1/app.R



CMD Rscript /project_1/exec.R



