FROM rocker/r-base:latest
MAINTAINER "Eric Novik" eric@stan.fit

#ENV STAN_BRANCH develop 
#ENV STAN_MATH_BRANCH develop

RUN apt-get update \ 
	&& apt-get install -y --no-install-recommends \
                   libcurl4-openssl-dev \
		   libssl-dev \
		   git-all

#ENV COMMIT_REF '1a81f57'

# Install clang to use as compiler
# clang seems to be more memory efficient with the templates than g++
# with g++ rstan cannot compile on docker hub due to memory issues
#RUN apt-get update \ 
#	&& apt-get install -y --no-install-recommends \
#                   clang

# Global site-wide config
#RUN mkdir -p $HOME/.R/ \
#    && echo "\nCXX=clang++ -ftemplate-depth-256\n" >> $HOME/.R/Makevars \
#    && echo "CC=clang\n" >> $HOME/.R/Makevars

RUN mkdir -p $HOME/.R
COPY rstan/R_Makefile $HOME/.R/Makefile

## install pre-reqs for rstan
RUN install2.r --error \
    inline \
    Rcpp \
    coda \
    BH \
    RcppEigen \
    RInside \
    RUnit \
    devtools \
    ggplot2 \
    gridExtra \
    matrixStats


## update Rcpp & Rcppcore to versions in github
## as done in https://github.com/stan-dev/rstan/blob/develop/.travis.yml
#RUN R -q -e "options(repos = getCRANmirrors()[1,'URL']); library(devtools); install_github('Rcpp', 'Rcppcore')"

## begin building rstan from source (github.com/stan-dev/rstan)
WORKDIR /tmp/build_rstan
RUN git clone --recursive https://github.com/stan-dev/rstan.git 

## build/install development version of StanHeaders
WORKDIR /tmp/build_rstan/rstan
#RUN git reset --hard $COMMIT_REF
#RUN git config -f .gitmodules submodule.stan.branch $STAN_BRANCH
#RUN git config -f .gitmodules submodule.StanHeaders/inst/include/mathlib.branch $STAN_MATH_BRANCH
#RUN git submodule update --remote
RUN R CMD build StanHeaders/
RUN R CMD INSTALL `find StanHeaders*.tar.gz`

## build/install development version of rstan
WORKDIR /tmp/build_rstan/rstan/rstan 
RUN R CMD build rstan --no-build-vignettes
RUN R CMD INSTALL `find rstan*.tar.gz`

## install dependencies for shinystan
# RUN install2.r --error \ 
#    DT \
#    dygraphs \
#    gtools \ 
#    shinyjs \ 
#    shinythemes \ 
#    threejs \ 
#    xts \
#    rsconnect

## build/install development version of shinystan
# WORKDIR /tmp/build_shinystan
# RUN git clone --recursive https://github.com/stan-dev/shinystan.git
# RUN R CMD build shinystan
# RUN R CMD INSTALL `find shinystan_*.tar.gz`

## install loo
WORKDIR /tmp/build_loo
RUN git clone --recursive https://github.com/stan-dev/loo.git
RUN R CMD build loo --no-build-vignettes
RUN R CMD INSTALL `find loo_*.tar.gz`

WORKDIR /home/rstudio

