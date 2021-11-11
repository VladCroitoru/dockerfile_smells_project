#
# create a cling-jupyter notebook service
# 
# for more information, see these sources:
# https://blog.jupyter.org/interactive-workflows-for-c-with-jupyter-fe9b54227d92
# https://docs.anaconda.com/anaconda/user-guide/tasks/integration/docker
# https://github.com/QuantStack/xeus-cling
#
# This file partially replicates the continuumio/miniconda3 Dockerfile
# in order to have the latest version if debian included without waiting
# for the miniconda3 docker image to update.
# 

# start of continuumio/miniconda3

FROM debian:latest

RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes
# end of continuumio/miniconda3

# install boost
RUN apt-get update                  && \
    apt-get install -y curl gcc g++ && \
    mkdir /boost                    && \
    cd /boost                       && \
    curl -L https://dl.bintray.com/boostorg/release/1.66.0/source/boost_1_66_0.tar.gz --output boost_1_66_0.tar.gz && \
    tar -xzf boost_1_66_0.tar.gz    && \
    cd /boost/boost_1_66_0          && \
    ./bootstrap.sh                  && \
    ./b2 install -d0 --without-wave --without-python && \
    cd /                            && \
    rm -rf boost                    && \
    apt-get -qq -y remove curl      && \
    apt-get -qq -y autoremove       && \
    apt-get autoclean               && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log

RUN conda install cling -c QuantStack -c conda-forge -y      && \
    conda install xeus-cling -c QuantStack -c conda-forge -y && \
    conda install notebook -c conda-forge -y                 && \
    conda clean --all --yes

# set up user and environment
ENV     PATH /opt/conda/bin:$PATH
RUN     useradd -ms /bin/bash notebooker
COPY    start-notebook.sh /usr/local/bin
USER    notebooker
WORKDIR /home/notebooker
CMD     start-notebook.sh
