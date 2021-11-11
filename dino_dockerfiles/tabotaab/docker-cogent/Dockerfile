# Set the base image to Ubuntu
FROM ubuntu:14.04
MAINTAINER Sara Movahedi movahedisara@yahoo.com

# Update the repository sources list
RUN apt-get update
RUN apt-get install -y -q software-properties-common

# Install compiler and perl stuff
RUN apt-get install -y -q libboost-iostreams-dev libboost-system-dev libboost-filesystem-dev
RUN apt-get install -y -q zlibc gcc-multilib apt-utils zlib1g-dev python python-pip
RUN apt-get install -y -q libx11-dev libxpm-dev libxft-dev libxext-dev libncurses5-dev
RUN apt-get install -y -q cmake tcsh build-essential g++ git wget gzip perl unzip
RUN apt-get install -y -q vim samtools
RUN apt-get update
RUN apt-get -y upgrade

# GMAP
WORKDIR /
RUN wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2018-07-04.tar.gz
RUN tar zxvf gmap-gsnap-2018-07-04.tar.gz
RUN cd /gmap-2018-07-04 && ./configure && make && make install
RUN rm -f gmap-gsnap-2018-07-04.tar.gz

# MASH v1.0.2
WORKDIR /
RUN wget https://github.com/marbl/Mash/releases/download/v1.0.2/mash-Linux64-v1.0.2.tar.gz
RUN tar -xvzf mash-Linux64-v1.0.2.tar.gz 
RUN cp mash /usr/bin/
RUN rm -f mash-Linux64-v1.0.2.tar.gz


# Minimap2 v2.7-r654
WORKDIR /
RUN wget https://github.com/lh3/minimap2/releases/download/v2.7/minimap2-2.7_x64-linux.tar.bz2
RUN tar xvjf minimap2-2.7_x64-linux.tar.bz2
RUN cp /minimap2-2.7_x64-linux/minimap2 /usr/bin/
RUN chmod 755 /minimap2-2.7_x64-linux/minimap2.1
ENV PATH=$PATH:/minimap2-2.7_x64-linux
RUN rm -f minimap2-2.7_x64-linux.tar.bz2

###############################
## A little Docker magic here

# Force bash always
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# Default conda installation
ENV CONDA_ENV_PATH /anaconda3
ENV MY_CONDA_COGENTENV "anaCogent"
# This is how you will activate this conda environment
ENV CONDA_ACTIVATE "source $CONDA_ENV_PATH/bin/activate $MY_CONDA_COGENTENV"

###############################
# Anaconda
WORKDIR /
RUN wget https://repo.continuum.io/archive/Anaconda3-5.3.1-Linux-x86_64.sh
RUN bash Anaconda3-5.3.1-Linux-x86_64.sh -b -p $CONDA_ENV_PATH 
ENV PATH=$CONDA_ENV_PATH/bin:$PATH

RUN conda -V && conda update --quiet --yes conda && \
    conda create -y -n $MY_CONDA_COGENTENV python=2.7 anaconda 

# Python Prerequisites
RUN $CONDA_ACTIVATE && \
    apt-get -y install libgl1-mesa-glx && \
    conda install -y -n $MY_CONDA_COGENTENV numpy && \
    conda install -y -n $MY_CONDA_COGENTENV scipy && \
    conda install -y -n $MY_CONDA_COGENTENV scikit-image && \
    conda install -y -n $MY_CONDA_COGENTENV matplotlib && \
    conda install -y -n $MY_CONDA_COGENTENV biopython && \
    conda install -y -n $MY_CONDA_COGENTENV -c http://conda.anaconda.org/cgat bx-python && \
    conda install -y -n $MY_CONDA_COGENTENV -c conda-forge pulp && \
    conda clean -y -t 

RUN chmod -R 755 $CONDA_ENV_PATH/bin && chmod -R 755 $CONDA_ENV_PATH/envs/anaCogent/bin

ENV PATH=$PATH:$CONDA_ENV_PATH/envs/anaCogent/bin

###############################
# Cogent
WORKDIR /
RUN $CONDA_ACTIVATE && \
    git clone https://github.com/Magdoll/Cogent.git && \
    cd Cogent && \
    git submodule update --init --recursive && \
    cd  Complete-Striped-Smith-Waterman-Library/src && \
    make && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Cogent/Complete-Striped-Smith-Waterman-Library/src && \
    export PYTHONPATH=$PYTHONPATH:/Cogent/Complete-Striped-Smith-Waterman-Library/src && \
    cd ../../ && \
    python setup.py build && \
    python setup.py install && \
    chmod 755 /Cogent -R

###############################
# Cupcake
WORKDIR /
RUN $CONDA_ACTIVATE && \
    git clone https://github.com/Magdoll/cDNA_Cupcake.git && \
    cd cDNA_Cupcake && \
    git checkout -b tofu2 tofu2_v21 && \
    python setup.py build && \
    python setup.py install && \
    chmod 755 /cDNA_Cupcake -R

ENV PATH=$PATH:/cDNA_Cupcake/cupcake2/tofu2:/cDNA_Cupcake/cupcake2/ice2:/cDNA_Cupcake/sequence/:/cDNA_Cupcake/annotation/:/cDNA_Cupcake/post_isoseq_cluster/:/cDNA_Cupcake/SequelQC 

###############################
WORKDIR /
RUN $CONDA_ACTIVATE && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Cogent/Complete-Striped-Smith-Waterman-Library/src && \
    export PYTHONPATH=$PYTHONPATH:/Cogent/Complete-Striped-Smith-Waterman-Library/src 

