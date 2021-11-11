#################################################################
# Dockerfile
#
# Version:          1
# Software:         R
# Description:      R and necessary packages for the analysis the classifier for Angela Santonja
# Website:          
# Tags:             None, for the moment
# Base Image:       R
#################################################################

##Image created on a debian
FROM r-base:3.4.0

#xml needed by Rcompression
#curl needed by RCurl
RUN apt-get update && apt-get install -y \
    r-cran-xml \
    #curl \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev #per paquet xml2
    
ENV PATH=pkg-config:$PATH   

## Install the R packages, some of those are necessary for the bioconductor's packages.  NOTE: failure to install a package doesn't throw an image build error.
#Rcompression needed by RCurl
RUN install2.r -r http://www.omegahat.net/R --deps TRUE \
    Rcompression \
    && rm -rf /tmp/downloaded_packages/

#  devtools necessita BiocInstaller
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("BiocInstaller")'

RUN install2.r --error --deps TRUE \
    RCurl \
    plyr \
    devtools \
    xml2 \
    xgboost \
    sda \
    class \
    e1071 \
    pamr \
    randomForest \
    rpart \
    partDSA \
    && rm -rf /tmp/downloaded_packages/


## Add biocLite to install Biobase
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("genefilter"); biocLite("limma")'
RUN Rscript -e 'library(devtools); install_github("romainkp/modelUtils"); install_github("romainkp/DSA")'


##That's all for the moment
