FROM rocker/r-base
LABEL org.label-schema.license="GPL-2.0" \
      org.label-schema.vcs-url="https://github.com/vtdrfuka" \
      maintainer="Daniel Fuka <drfuka@vt.edu>"

RUN apt update \
  && apt-get install -y gzip curl wget subversion jags
RUN apt-get -y --fix-missing install vim libxml2-dev libz-dev gdal-bin libudunits2-dev libxt6 libgdal-dev mpich mdbtools
RUN apt-get clean
RUN mkdir /mintswat/

RUN Rscript -e 'if (!require("pacman")) install.packages("pacman"); pacman::p_load(operators, topmodel, DEoptim, XML,data.table,RSQLite,argparse,stringi); system("svn checkout svn://scm.r-forge.r-project.org/svnroot/ecohydrology/"); install.packages(c("ecohydrology/pkg/EcoHydRology/","ecohydrology/pkg/SWATmodel/"),repos = NULL)' 
WORKDIR /mintswat
