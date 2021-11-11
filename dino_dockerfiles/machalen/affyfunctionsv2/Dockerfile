#################################################################
# Dockerfile
# Description:      R and necessary packages for the analysis of Affymetrix microarrays   
# Base Image:       r-base:3.3.1
#################################################################

#R image to be the base in order to build our new image
FROM r-base:3.3.1

#Install Ubuntu extensions in order to run r
RUN apt-get update && apt-get install -y \
    r-cran-xml \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev
    
ENV PATH=pkg-config:$PATH

#Install Bioconductor packages first
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("sva","Biobase","limma", "BiocGenerics","affxparser","affy", "affyPLM", "aroma.light", "gcrma", "oligo", "oligoClasses", "pdInfoBuilder", "preprocessCore", "AffymetrixDataTestFiles", "DNAcopy", "RBGL","graph"))'

#Install packages from CRAN
RUN Rscript -e 'install.packages(c("R.utils","aroma.affymetrix","data.table", "gtools", "Rcpp","RColorBrewer", "gplots","scatterplot3d"))'

#Vennerable has to be installed from a website repo
RUN Rscript -e 'install.packages("devtools");library(devtools);install_github("js229/Vennerable")'
