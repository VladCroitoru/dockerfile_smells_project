FROM rocker/verse:latest
## Installs R, Rstudio, tidyverse, tex, pandoc and other markdown dependencies

## Add lines from bioc

RUN apt-get update && \
    apt-get -y  install --fix-missing gdb libxml2-dev python-pip libmariadb-client-lgpl-dev

# R matrix requires gfortran
RUN apt-get update && apt-get -y install gfortran gfortran-6

# R XVector requires zlib.h
RUN apt-get update && apt-get -y install libz-dev


# Install r1001genomes package dependencies
RUN R -e 'install.packages("cowplot")'

RUN R -e 'install.packages("devtools")'

RUN R -e 'install.packages("ggmap")'

RUN R -e 'install.packages("ggthemes")'

RUN R -e 'install.packages("ggpmisc")

RUN R -e 'install.packages("ggrepel")'

RUN R -e 'install.packages("ggseqlogo")'

RUN R -e 'install.packages("leaflet")'

RUN R -e 'install.packages("magrittr")'

RUN R -e 'install.packages("msaR")'

RUN R -e 'install.packages("plyr")'

RUN R -e 'install.packages("RColorBrewer")'

RUN R -e 'install.packages("reshape2")'

RUN R -e 'install.packages("shiny")'

RUN R -e 'install.packages("shinyBS")'

RUN R -e 'install.packages("shinycssloaders")'

RUN R -e 'install.packages("shinythemes")'

RUN R -e 'install.packages("stringr")'

# Setup an R script to install bioconductor packages
ADD install.R /tmp/

# invalidates cache every 24 hours
ADD http://master.bioconductor.org/todays-date /tmp/

# Install bioMart, VariantAnnotation and vcfR
RUN R -f /tmp/install.R

# Install r1001genomes from github repo
RUN R -e 'devtools::install_github("wrightrc/r1001genomes", ref = "docker-stable")'

# Add files to the image
#ADD . /home/rstudio/




