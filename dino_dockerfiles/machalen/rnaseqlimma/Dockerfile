#################################################################
# Dockerfile
# Software:         R
# Description:      R and required packages to use DEXSeq
# Base Image:       R-base:3.4.0
#################################################################
#R image to be the base in order to build our new image
FROM r-base:3.4.0

#Maintainer and author
MAINTAINER Magdalena Arnal <marnal@imim.es>

#Install Ubuntu extensions in order to run r
RUN apt-get update && apt-get install -y \
    r-cran-xml \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    build-essential \
    curl \
    zlib1g-dev \
    gfortran \
    libncurses5-dev
   
RUN rm -rf /var/lib/apt/lists/*
ENV PATH=pkg-config:$PATH

#Install packages from CRAN and bioconductor:
RUN Rscript -e 'install.packages(c("acepack", "RcppArmadillo", "statmod"))'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("sva","BiocGenerics","biomaRt","Rsamtools","geneplotter","genefilter","DNAcopy"));'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("BiocParallel","Biobase","SummarizedExperiment","IRanges","GenomicRanges","DESeq2","AnnotationDbi","S4Vectors"));'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("GenomicFeatures","pasilla","parathyroidSE","BiocStyle"));'
RUN Rscript -e 'install.packages(c("hwriter","stringr", "statmod","RColorBrewer","knitr"))'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("DEXSeq");'
RUN Rscript -e 'install.packages(c("R.utils","data.table", "gtools", "Rcpp", "gplots","scatterplot3d"))'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=c("limma","edgeR","Rsubread"));'
