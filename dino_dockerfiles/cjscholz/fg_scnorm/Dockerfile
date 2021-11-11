############################################################ 
# Dockerfile to run the SCnorm preprocessing
# of single-cell RNA-seq data in FAST Genomics format
############################################################ 

# base image of Bioconductor
FROM bioconductor/release_core2

# File Author / Maintainer 
MAINTAINER Claus J. Scholz <cscholz@uni-bonn.de>

# start the installation
ADD ./install_scripts /opt/install_scripts
RUN apt-get update
RUN Rscript /opt/install_scripts/install_SCnorm.R

# run the command to start the SCnorm preprocessing
ADD ./analysis_scripts /opt/analysis_scripts
ADD ./config /opt/config
CMD ["Rscript", "--default-packages=base,utils,grDevices,graphics,stats,methods", "/opt/analysis_scripts/run_FG_SCnorm.R"]

RUN apt-get clean
