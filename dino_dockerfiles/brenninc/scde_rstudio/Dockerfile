FROM rocker/rstudio

MAINTAINER Christian Brenninkmeijer <Christian.Brenninkmeijer@manchester.ac.uk>

# See https://cran.r-project.org/bin/linux/ubuntu/README
RUN echo "deb http://mirrors.ebi.ac.uk/CRAN/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list

#Install curl, R, and R packages
RUN apt-get update  && apt-get install -y --force-yes \
    curl

#Install R packages
RUN apt-get install -y --force-yes \
    libx11-dev \
    libxext-dev \
    libxcb1=1.10-3+b1 \
    libxcb1-dev=1.10-3+b1 \
    libxcb-render0=1.10-3+b1 \
    libxcb-render0-dev \
    libxcb-shm0=1.10-3+b1 \
    libxcb-shm0-dev \   
    libx11-dev \
    libcairo2-dev \
    libxt-dev \
    r-cran-colorspace \
    r-cran-dichromat \
    r-cran-digest \
    r-cran-Formula \
    r-cran-ggplot2 \
    r-cran-gtable \
    r-cran-Hmisc \
    r-cran-labeling \
    r-cran-latticeExtra \
    r-cran-munsell \
    r-cran-plyr \
    r-cran-proto \
    r-cran-Rcpp \
    r-cran-RColorBrewer \
    r-cran-reshape \
    r-cran-rjson \
    r-cran-scales \
    r-cran-snow \
    r-cran-SparseM \
    r-cran-XML \
    r-cran-xtable 

RUN \   
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/modeltools_0.2-21.tar.gz > modeltools_0.2-21.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/flexmix_2.3-13.tar.gz > flexmix_2.3-13.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/brew_1.0-6.tar.gz > brew_1.0-6.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/Rook_1.1-1.tar.gz > Rook_1.1-1.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/Cairo_1.5-9.tar.gz > Cairo_1.5-9.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/MatrixModels_0.4-1.tar.gz > MatrixModels_0.4-1.tar.gz  && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/quantreg_5.19.tar.gz > quantreg_5.19.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/stringi_0.5-5.tar.gz > stringi_0.5-5.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/magrittr_1.5.tar.gz > magrittr_1.5.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/RMTstat_0.3.tar.gz > RMTstat_0.3.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/Lmoments_1.1-6.tar.gz > Lmoments_1.1-6.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/distillery_1.0-2.tar.gz > distillery_1.0-2.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/RcppEigen_0.3.2.5.1.tar.gz > RcppEigen_0.3.2.5.1.tar.gz &&\
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/minqa_1.2.4.tar.gz > minqa_1.2.4.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/nloptr_1.0.4.tar.gz > nloptr_1.0.4.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/lme4_1.1-10.tar.gz > lme4_1.1-10.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/pbkrtest_0.4-2.tar.gz > pbkrtest_0.4-2.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/car_2.1-0.tar.gz > car_2.1-0.tar.gz && \ 
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/extRemes_2.0-6.tar.gz > extRemes_2.0-6.tar.gz && \ 
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/RcppArmadillo_0.6.100.0.0.tar.gz > RcppArmadillo_0.6.100.0.0.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/rjson_0.2.15.tar.gz > rjson_0.2.15.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/stringr_1.0.0.tar.gz > stringr_1.0.0.tar.gz 

RUN \   
    R CMD INSTALL \ 
        modeltools_0.2-21.tar.gz \
        flexmix_2.3-13.tar.gz \
        brew_1.0-6.tar.gz \
        Rook_1.1-1.tar.gz \  
        Cairo_1.5-9.tar.gz \
        MatrixModels_0.4-1.tar.gz \ 
        quantreg_5.19.tar.gz \
        stringi_0.5-5.tar.gz \ 
        magrittr_1.5.tar.gz \
        RMTstat_0.3.tar.gz  \ 
        Lmoments_1.1-6.tar.gz \
        distillery_1.0-2.tar.gz \ 
        RcppEigen_0.3.2.5.1.tar.gz \
        minqa_1.2.4.tar.gz \ 
        nloptr_1.0.4.tar.gz \
        lme4_1.1-10.tar.gz \ 
        pbkrtest_0.4-2.tar.gz \
        car_2.1-0.tar.gz \ 
        extRemes_2.0-6.tar.gz \
        RcppArmadillo_0.6.100.0.0.tar.gz && \
    rm *.tar.gz
        
RUN R -e 'source("http://bioconductor.org/biocLite.R"); biocLite("edgeR"); biocLite("DESeq2"); biocLite("pcaMethods");' 
    
RUN curl -L https://github.com/hms-dbmi/scde/archive/1.99.0.tar.gz > scde-1.99.0.tar.gz && \
    R CMD INSTALL scde-1.99.0.tar.gz && \
    tar -xzf scde-1.99.0.tar.gz && \
    mkdir sample && \
    cp scde-1.99.0/data/* sample && \
    rm -r scde-1.99.0 && \
    rm scde-1.99.0.tar.gz

