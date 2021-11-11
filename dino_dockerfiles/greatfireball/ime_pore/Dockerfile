FROM ubuntu:xenial

LABEL maintainer="frank.foerster@ime.fraunhofer.de"
LABEL description="Dockerfile providing the poRe quality assessment and sequence extraction software for MinION long reads"

RUN apt update && apt install --yes software-properties-common python-software-properties && add-apt-repository --yes ppa:marutter/rrutter

RUN apt update && apt install --yes r-base r-base-dev

RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("rhdf5")'

RUN Rscript  -e 'install.packages(c("shiny","svDialogs","data.table","bit64"), repos=c("https://cloud.r-project.org"))'

RUN apt install wget && wget -O /tmp/poRe_0.24.tar.gz 'https://sourceforge.net/projects/rpore/files/0.24/poRe_0.24.tar.gz/download' && R CMD INSTALL /tmp/poRe_0.24.tar.gz && rm /tmp/poRe_0.24.tar.gz

VOLUME /data

WORKDIR /data

# loading poRe on R startup
ENV R_DEFAULT_PACKAGES=poRe

CMD R
