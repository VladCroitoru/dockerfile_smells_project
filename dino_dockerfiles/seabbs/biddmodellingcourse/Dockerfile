## Start with the tidyverse docker image
FROM rocker/tidyverse:latest

MAINTAINER "Sam Abbott" contact@samabbott.co.uk

RUN apt-get update -y && \
    apt-get install -y \
    texlive-latex-recommended \
    texlive-fonts-extra \
    texinfo \
    libqpdf-dev \
    libmagick++-dev \
    && apt-get clean
    
ADD . /home/rstudio/biddmodellingcourse

RUN Rscript -e 'devtools::install_deps("/home/rstudio/biddmodellingcourse", dependencies = TRUE, upgrade = TRUE)'

RUN Rscript -e 'devtools::install_github("r-lib/pkgdown")'

RUN Rscript -e 'devtools::install_github("bristolmathmodellers/biddmodellingcourse")'


