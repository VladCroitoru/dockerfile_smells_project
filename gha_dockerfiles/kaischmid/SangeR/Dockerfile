ARG baseimage_version=v1.0
FROM r-base

ARG SangeR=1.0

LABEL   maintainer="kai.schmid@patho.uni-giessen,de" \
        description="Container for SangeR" \
        version=${SangeR_version}

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
apt-get install --yes --no-install-recommends wget r-base r-base-dev r-cran-rcurl libcurl4-openssl-dev libxml2-dev libssl-dev g++ make gfortran git && \
R -e "install.packages('BiocManager',repos = 'http://cran.us.r-project.org')" && \
R -e "install.packages('stringr',repos = 'http://cran.us.r-project.org')" && \
R -e "install.packages('ggplot2',repos = 'http://cran.us.r-project.org')" && \
R -e "install.packages('reshape2',repos = 'http://cran.us.r-project.org')" && \
R -e "install.packages('seqinr',repos = 'http://cran.us.r-project.org')" && \
R -e "BiocManager::install(c('biomaRt','sangerseqR'))" \
R -e "BiocManager::install(c('CrispRVariants','Biostrings'))"
