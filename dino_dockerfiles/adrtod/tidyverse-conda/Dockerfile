FROM rocker/tidyverse:latest
MAINTAINER Adrien Todeschini <adrien.todeschini@gmail.com>
RUN apt-get update --fix-missing && \
    apt-get install -y git ssh tar gzip ca-certificates wget bzip2
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda2-5.0.0.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh
ENV PATH /opt/conda/bin:$PATH
RUN conda install virtualenv
