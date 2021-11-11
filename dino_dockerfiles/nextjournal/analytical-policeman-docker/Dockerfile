FROM alpine:3.5

RUN apk add --no-cache bash gawk autoconf sed grep bc coreutils curl gcc g++ git coreutils make gfortran expat-dev R\
                       openjdk8 R-dev libressl-dev curl-dev libxml2-dev jpeg-dev ca-certificates gsl gsl-dev &&\
  R -q -e "install.packages('Rcpp', repo='https://cran.rstudio.com')" &&\
  curl -L -O https://cran.r-project.org/src/contrib/httpuv_1.3.3.tar.gz &&\
  tar xvf httpuv_1.3.3.tar.gz &&\
  sed -i -e 's/__USE_MISC/_GNU_SOURCE/g' httpuv/src/libuv/src/fs-poll.c &&\
  tar -cf httpuv_1.3.3.tar.gz httpuv &&\
  R CMD INSTALL httpuv_1.3.3.tar.gz &&\
  curl -L -O ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.24.tar.gz &&\
  tar xvf udunits-2.2.24.tar.gz &&\
  cd udunits-2.2.24 && ./configure && make && make install && cd .. &&\
  git clone https://github.com/ropensci/git2r.git &&\
  R CMD INSTALL --configure-args="--with-libssl-include=/usr/lib/" git2r &&\
  R -q -e "install.packages(c('devtools'), repo='https://cran.rstudio.com/')" &&\
  R -q -e "install.packages(c('base64enc'), repo='https://cran.rstudio.com/')" &&\
  R -q -e "install.packages(c('jsonlite'), repo='https://cran.rstudio.com/')" &&\
  R -q -e "install.packages(c('plotly'), repo='https://cran.rstudio.com/')" &&\
  rm -rf git2r /tmp/*

RUN echo "options(repos=structure(c(CRAN=\"https://cran.rstudio.com\")))" > ~/.Rprofile
ADD dependencies.R dependencies.R
RUN Rscript dependencies.R
