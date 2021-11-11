FROM rocker/rstudio
MAINTAINER "Christian Diener <mail[at]cdiener.com>"

RUN apt-get update && apt-get install -y libxml2-dev python3 python3-pip wget && apt-get clean
RUN pip3 install -U pip
RUN pip install python-libsbml numpy scipy lxml cobra pandas && rm -rf /tmp/*

RUN mkdir /data && chown rstudio:rstudio /data

USER rstudio

RUN git clone https://github.com/cdiener/proliferation /data/proliferation
WORKDIR /data/proliferation
USER root
RUN Rscript -e "source('http://bioconductor.org/biocLite.R'); \
    biocLite('BiocInstaller'); setRepositories(ind=1:2); \
    install.packages(c('devtools', 'rmarkdown')); \
    devtools::install_deps('prtools', dependencies=TRUE); \
    devtools::install('prtools')"
USER rstudio
RUN wget https://zenodo.org/record/61980/files/regprob.csv && \
    wget https://zenodo.org/record/61982/files/tcga.rds

USER root
