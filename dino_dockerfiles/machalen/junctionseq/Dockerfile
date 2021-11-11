#################################################################
# Dockerfile
# Software:         R
# Description:      R and necessary packages to use JunctionSeq
# Base Image:       R-base:3.4.0
#################################################################
#R image to be the base in order to build our new image
FROM r-base:3.3.3

#Maintainer and author
MAINTAINER Magdalena Arnal <marnal@imim.es>

#Install Ubuntu extensions in order to run r
#Bug detectat!: https://stat.ethz.ch/pipermail/r-sig-debian/2017-March/002660.html
RUN apt-get update && apt-get install -y \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    build-essential \
    curl \
    zlib1g-dev \
    gfortran \
    libncurses5-dev
    
ENV PATH=pkg-config:$PATH

#Install packages from CRAN and bioconductor:
RUN Rscript -e 'install.packages(c("acepack","Rcpp","RcppArmadillo","statmod","Hmisc","plotrix","stringr","locfit"))'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("BiocGenerics","biomaRt","Rsamtools","geneplotter","genefilter"));'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("BiocParallel","Biobase","SummarizedExperiment","IRanges","GenomicRanges","DESeq2","AnnotationDbi","S4Vectors"));'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("GenomicFeatures","pasilla","parathyroidSE","BiocStyle","S4Vectors"));'
RUN Rscript -e 'install.packages(c("hwriter","stringr", "statmod","RColorBrewer","knitr"))'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("DEXSeq","JunctionSeq"));'
