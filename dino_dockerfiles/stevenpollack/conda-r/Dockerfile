## Emacs, make this -*- mode: sh; -*-

########################################################
##                                                    ##
## If creating your own image, edit the two entries   ##
## below, and the PACKAGES file                       ##
##                                                    ##
########################################################

## Choose your base image, e.g., rocker/drd:latest or rwercker/base:latest
FROM ubuntu:15.10

## Edit maintainer information as appropritate
MAINTAINER "Kirill Müller" krlmlr+github@mailbox.org

RUN apt-get update && apt-get install -y \
    libpq-dev \
    pkg-config \
    wget

RUN wget -O miniconda3.sh http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod +x miniconda3.sh \
    && ./miniconda3.sh -b \
    && rm ./miniconda3.sh

ENV PATH /root/miniconda3/bin:$PATH

RUN conda install -y --channel r \
    gcc \
    r-devtools

# update gmp to 6.0.0a
RUN conda install -y -c https://conda.anaconda.org/ostrokach gmp 
# link /usr/lib/.../libgmp.so to anaconda's version:
Run ln -fs /root/miniconda3/lib/libgmp.so.10 /usr/lib/x86_64-linux-gnu/libgmp.so.10

RUN touch tmp.R && \
    echo \ 
"options(unzip = 'internal', \
        repos = c(CRAN = 'http://cran.rstudio.com')); \
httr::set_config( httr::config( ssl_verifypeer = 0L ) ); \
devtools::install_github(c('RcppCore/Rcpp', \
                           'rstats-db/DBI', \
                           'rstats-db/RPostgres'));" > tmp.R && \
    R --no-save -f tmp.R && \
    rm tmp.R

COPY test_Rpostgres.R test_Rpostgres.R

CMD ["/bin/bash"]
