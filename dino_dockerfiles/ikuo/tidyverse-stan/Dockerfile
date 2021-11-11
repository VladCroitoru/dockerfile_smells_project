FROM rocker/tidyverse:3.4.0
LABEL maintainer "Ikuo Matsumura <ikuo@initials.im>"

RUN apt update && \
  apt install -y \
    build-essential \
    libssl1.0-dev \
    clang++-3.8 \
    htop && \
  apt clean

COPY Makevars /root/.R/Makevars

RUN Rscript -e 'Sys.setenv(MAKEFLAGS = "-j4"); install.packages(c("Rcpp", "rstan"), type = "source")'
