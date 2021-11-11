FROM rocker/rstudio:3.3.2

MAINTAINER Pathway Commons <https://groups.google.com/forum/#!forum/pathway-commons-help/>

RUN wget http://security.debian.org/debian-security/pool/updates/main/libx/libxml2/libxml2-dev_2.9.1+dfsg1-5+deb8u4_amd64.deb && \
  dpkg -i libxml2-dev_2.9.1+dfsg1-5+deb8u4_amd64.deb

# Install the required R/Bioconductor packages
RUN R -e 'install.packages(c("devtools"), repos="http://cran.us.r-project.org")'
RUN R -e 'source("https://bioconductor.org/biocLite.R"); \
          biocLite(c("TCGAbiolinks", \
                     "SummarizedExperiment", \
                     "GenomicRanges", \
                     "IRanges", \
                     "edgeR", \
                     "biomaRt", \
                     "DEFormats"), \
          suppressUpdates=TRUE, ask=FALSE);'

# Apache ports
EXPOSE 8787
