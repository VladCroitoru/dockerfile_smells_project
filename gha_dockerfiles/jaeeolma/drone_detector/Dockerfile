FROM nvidia/cuda:11.1.1-base-ubuntu20.04

RUN echo 'install software and tools'
RUN apt-get -y update
RUN apt-get -y install --no-install-recommends build-essential ca-certificates \
            git nano zip unzip curl graphviz
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# add non-root user
RUN useradd --create-home --shell /bin/bash containeruser
USER containeruser
WORKDIR /home/containeruser

# install miniconda and python
RUN curl -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /home/containeruser/conda && \
    rm ~/miniconda.sh && \
    /home/containeruser/conda/bin/conda clean -ya && \
    /home/containeruser/conda/bin/conda install -y python=3.7

ENV PATH /home/containeruser/conda/bin:$PATH
ENV CONDA_DEFAULT_ENV $conda_env

RUN git clone git@github.com:jaeeolma/drone_detector
RUN cd drone_detector

RUN conda env create -f environment.yml

RUN conda init bash