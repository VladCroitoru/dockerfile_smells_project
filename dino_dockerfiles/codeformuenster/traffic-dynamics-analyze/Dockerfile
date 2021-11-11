## this was from https://github.com/jzelner/docker-rstan/blob/master/rstan/Dockerfile
## the only changes are
## (1) installing brms also (line 28)
## (2) using rocker/tidyverse instead of rocker/hadleyverse as base image (as recommended)
## (3) install clang instead of clang-3.6 which isn't available anymore
## (4) don't install texlive

FROM codeformuenster/traffic-dynamics:v0.3.6

## Mostly pirated from jrnold/docker-stan

# Install clang to use as compiler
# clang seems to be more memory efficient with the templates than g++
# with g++ rstan cannot compile on docker hub due to memory issues
RUN apt-get update \ 
	&& apt-get install -y --no-install-recommends \
                   clang

# Global site-wide config
RUN mkdir -p $HOME/.R/ \
    && echo "\nCXX=clang++ -ftemplate-depth-256\n" >> $HOME/.R/Makevars \
    && echo "CC=clang\n" >> $HOME/.R/Makevars

# Install rstan
RUN install2.r --error \
    inline \
    RcppEigen \
    StanHeaders \
    rstan \
    brms \
    KernSmooth

# Config for rstudio user
RUN mkdir -p /home/rstudio/.R/ \
    && echo "\nCXX=clang++ -ftemplate-depth-256\n" >> /home/rstudio/.R/Makevars \
    && echo "CC=clang\n" >> /home/rstudio/.R/Makevars \
    && echo "CXXFLAGS=-O3\n" >> /home/rstudio/.R/Makevars \
    && echo "\nrstan::rstan_options(auto_write = TRUE)" >> /home/rstudio/.Rprofile \
    && echo "options(mc.cores = parallel::detectCores())" >> /home/rstudio/.Rprofile

RUN apt-get update \ 
	&& apt-get install -y --no-install-recommends \
                   curl apt-utils

COPY ./src /srv/shiny-server/src
COPY ./results /srv/shiny-server/results

## this runs not when building the image but only when starting it:
# file writing test:
CMD Rscript -e "source('/srv/shiny-server/src/02_Bayesian_regressions.R')"
