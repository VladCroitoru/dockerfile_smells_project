FROM r-base:4.0.5
LABEL maintainer="Nacho Garcia <iggl@fhi.no>"
ENV PATH="/home/docker/miniconda3/envs/pangolin/bin:/home/docker/Scripts:/home/docker/miniconda3/bin:${PATH}"
ARG PATH="/home/docker/miniconda3/envs/pangolin/bin:/home/docker/Scripts:/home/docker/miniconda3/bin:${PATH}"
RUN apt-get update -qq \
    && apt-get -y --no-install-recommends install \
    liblzma-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libgc-dev \
    libssl-dev \
    gcc-9 \
    libpoppler-cpp-dev \
    nano \
    procps \
    wget \
    git-all \
    bc \
    rsync\
    nodejs \
    npm \
    && npm install --global @nextstrain/nextclade@0.14.4


RUN userdel docker && useradd -ms /bin/bash docker
ARG USER=docker
ARG GROUP=docker
ARG UID
ARG GID

ENV USER=$USER
ENV GROUP=$GROUP
ENV UID=$UID
ENV GID=$GID
ENV HOME="/home/${USER}"

RUN cd /home/docker \
    && wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /home/docker/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh \
    && conda config --add channels defaults \
    && conda config --add channels bioconda \
    && conda config --add channels conda-forge \
    && conda install ivar \
    && conda install -c bioconda samtools\
    && conda install -c bioconda seqkit \
    && conda update -n base -c defaults conda \
    && conda install -c bioconda bedtools \
    && conda install -c bioconda nextalign \
    && git clone https://github.com/cov-lineages/pangolin \
    && cd pangolin \
    && conda env create -f environment.yml \
    && pip install . \
    && pip install seaborn \
    && pip install matplotlib\
    && ln -s /home/docker/miniconda3/lib/libcrypto.so.1.1 /home/docker/miniconda3/lib/libcrypto.so.1.0.0

USER root
RUN Rscript -e "install.packages(c('doSNOW', \
'progress','foreach','parallel', 'pdftools', 'doParallel', \
'BiocManager', 'ggplot2', 'seqinr', 'xgboost', 'reshape2', 'httr','phangorn','ggpubr' ,'ape','readxl', 'geomnet','rvest', 'tidyverse','writexl','nnet', 'stringr', 'devtools', 'pacman','phylotools','optparse'))"
RUN Rscript -e "devtools::install_github('sctyner/geomnet')"
RUN rm -rf /var/lib/apt/lists/* \
    && rm /usr/bin/gcc /usr/bin/gcc-ar /usr/bin/gcc-nm /usr/bin/gcc-ranlib \
    && ln /usr/bin/gcc-nm-9 /usr/bin/gcc-nm \
    && ln /usr/bin/gcc-ar-9 /usr/bin/gcc-ar \
    && ln /usr/bin/gcc-9 /usr/bin/gcc \
    && ln /usr/bin/gcc-ranlib-9 /usr/bin/gcc-ranlib 
RUN Rscript -e "BiocManager::install(c('msa','GenomicAlignments','ggtree'))"
RUN mkdir -p /home/docker/Scripts /home/docker/Data /home/docker/CommonFiles /home/docker/Fastq /home/docker/Binaries
COPY CommonFiles/ /home/docker/CommonFiles/
COPY Scripts/ /home/docker/Scripts/
COPY Binaries/ /home/docker/Binaries/
RUN chmod +x /home/docker/Binaries/* \
    && chmod +x /home/docker/Scripts/* \
    && chmod -R +rwx /home/docker/CommonFiles/* \
    && mv /home/docker/Binaries/* /usr/bin/
USER docker
WORKDIR /home/docker/Fastq
