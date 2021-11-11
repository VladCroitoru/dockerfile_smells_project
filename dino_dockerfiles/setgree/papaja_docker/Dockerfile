FROM registry.codeocean.com/codeocean/r-base:3.6.0-ubuntu18.04

LABEL maintainer='Seth Green seth@codeocean.com'

ARG DEBIAN_FRONTEND=noninteractive
ENV RSTUDIO_VERSION=1.1.463

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      "dirmngr" \
      "software-properties-common" \
    && apt-key adv --keyserver "hkp://keyserver.ubuntu.com:80" --recv-keys \
      "0xAD2323F17326AE31401037733E05EBFF05441C52" \
    && add-apt-repository -y "deb http://deb.codeocean.com/rstudio-server-bionic/ ubuntu main" \
    && apt-get purge -y --autoremove software-properties-common \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
      "build-essential=12.4ubuntu1" \
      "libgit2-dev" \
      "libssl-dev=1.1.1-1ubuntu2.1~18.04.4" \
      "pandoc=1.19.2.4~dfsg-1build4" \
      "pkg-config" \
      "r-base=3.6.1-3bionic" \
      "rstudio-server=1.2.1335" \
      "dvipng" \
      "lmodern" \
      "pandoc" \
      "texlive-latex-extra" \
      "texlive-fonts-recommended" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN Rscript --vanilla -e" install.packages('devtools'); \
    devtools::install_github('crsh/papaja')"
    
ENTRYPOINT ["/bin/bash"]
