ARG version=xenial
FROM ubuntu:${version}

LABEL maintainer="frank.foerster@ime.fraunhofer.de" \
      description="Dockerfile providing the cummeRbund software" \
      version="$VERSION" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/greatfireball/docker_cummeRbund"

RUN apt update && apt -y install \
    wget \
    gzip \
    tar \
    build-essential \
    git \
    software-properties-common \
    python-software-properties \
    gnupg2 \
    apt-transport-https

# install GNU R
RUN gpg \
       --keyserver hkp://keyserver.ubuntu.com:80 \
       --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 &&\
    gpg -a --export E298A3A825C0D65DFD57CBB651716619E084DAB9 | apt-key add - &&\
    add-apt-repository \
       'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/' &&\
    apt update &&\
    apt install --yes \
       r-base \
       libcurl4-openssl-dev \
       libssl-dev \
       libxml2-dev \
       libmariadb-client-lgpl-dev

# install cummeRbund
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("cummeRbund",suppressUpdates=T, ask=F, suppressAutoUpdate=T);'

# install sqlite-3
RUN apt install --yes sqlite

VOLUME /data
WORKDIR /data