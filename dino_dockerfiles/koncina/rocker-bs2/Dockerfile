FROM rocker/tidyverse

MAINTAINER Eric KONCINA <mail@koncina.eu>

LABEL version="0.1"
LABEL description="Docker image to build the biostat2 website"

ARG DEBIAN_FRONTEND=noninteractive
# To avoid being trapped in the pager during knitting...
# And use bash instead of 
RUN sed -i 's/usr\/bin\/pager/bin\/cat/g' /usr/local/lib/R/etc/Renviron && \
    sed -i 's/\/home\/rstudio:/\/home\/rstudio:\/bin\/bash/g' /etc/passwd

# ffmpeg imagemagick are required for gganimate
# libudunits2-dev is required fo ggforce

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y apt-utils && \
    apt-get install -y ssh curl gnupg gnupg2 && \
    apt-get install -y ffmpeg imagemagick && \
    apt-get install -y libudunits2-dev rsync && \
    apt-get install -y libbz2-dev liblzma-dev

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

RUN Rscript -e 'devtools::install_github("koncina/unilur")' && \
    Rscript -e 'devtools::install_github("koncina/iosp@dev")' && \
    Rscript -e 'devtools::install_github("koncina/bs2site")'

ADD packages.yml /tmp/packages.yml

RUN Rscript -e 'bs2site::pkg_missing(path = "/tmp/", scan = FALSE, install = TRUE)'

ENV BS2_DEPLOY=1

