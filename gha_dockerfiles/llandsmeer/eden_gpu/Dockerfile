FROM jupyter/scipy-notebook:dd2087c75645

# Test & verification environment for EDEN simulator, including Jupyter, NEURON, jNeuroML and associated infrastrucure.
MAINTAINER Sotirios Panagiotou <info@sotiriospanagiotou.com>


ARG NEURON_VERSION=7.7

# ------------> Install prerequisites for MPI, NEURON, jNeuroML

USER root
RUN chown -R $NB_USER $HOME

#Get a whole lot of GNU core development tools
#version control java development, maven
#Libraries required for building MPI from source
#Libraries required for building NEURON from source

RUN apt-get update
RUN apt-get -y install apt-transport-https ca-certificates
RUN apt-get -y install apt-transport-https curl
RUN apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git gcc g++ build-essential \
    libncurses-dev openmpi-bin openmpi-doc libopenmpi-dev \
    default-jre default-jdk maven emacs \
    libxml2-dev libxslt-dev python-dev sudo

RUN pip install --upgrade pip

# Upgrade to version 2.0
# RUN conda update -n base conda anaconda=2019.10

# RUN conda install -y matplotlib

# Make sure every Python file belongs to jovyan
RUN find /opt/conda ! -user $NB_USER -print0 | xargs -0 -I {} chown -h $NB_USER {}
# Remove dangling symlinks
RUN find -L /opt/conda -type l -delete
# Make sure every Python file is writable
RUN find /opt/conda ! -writable -print0 | xargs -0 -I {} chmod 744 {}

RUN chown -R $NB_USER $HOME
RUN rm -rf /var/lib/apt/lists/*
RUN echo "${NB_USER} ALL=NOPASSWD: ALL" >> /etc/sudoers

USER $NB_USER
ENV WORK_HOME /$HOME/work
WORKDIR $WORK_HOME


# ------------> Install MPI, NEURON, jNeuroML

#author russell jarvis rjjarvis@asu.edu
#NEURON Dockerfile

#Get a whole lot of GNU core development tools
#version control java development, maven
#Libraries required for building MPI from source
#Libraries required for building NEURON from source
#Also DO this part as root.
USER root
RUN apt-get update && apt-get install -y wget bzip2 ca-certificates default-jre default-jdk maven automake libtool  \
                       wget python3 libpython3-dev libncurses5-dev libreadline-dev libgsl0-dev cython3 \
                       python3-pip python3-numpy python3-scipy python3-matplotlib python3-mock \
                       ipython3 python3-docutils \
                       python3-mpi4py cmake ssh


#Do the rest of the build  as user:
#This will create a more familiar environment to continue developing in.
#with less of a need to chown and chmod everything done as root at dockerbuild completion

USER jovyan
# Use numpy 1.12.1 until quantities is compatible with 1.13.
# RUN conda install -y scipy numpy==1.12.1 matplotlib
RUN sudo chown -R jovyan /home/jovyan
ENV HOME /home/jovyan
ENV PATH /opt/conda/bin:/opt/conda/bin/conda:/opt/conda/bin/python:$PATH

#Test matplotlib
RUN python -c "import matplotlib"
#Install General MPI, such that mpi4py can later bind with it.

WORKDIR $HOME

ARG NEURON_VERSIONED=nrn-${NEURON_VERSION}

# could make stderr more quiet or sth, to suppress red text
RUN \
  wget http://www.neuron.yale.edu/ftp/neuron/versions/v${NEURON_VERSION}/${NEURON_VERSIONED}.tar.gz && \
  tar -xzf ${NEURON_VERSIONED}.tar.gz && \
  rm ${NEURON_VERSIONED}.tar.gz

WORKDIR $HOME/${NEURON_VERSIONED}
ENV PATH /usr/bin/python3/python:/opt/conda/bin:/opt/conda/bin/conda:/opt/conda/bin/python:$PATH
RUN ./configure --prefix=`pwd` --with-paranrn --without-iv --with-nrnpython=/opt/conda/bin/python3
RUN sudo make all && \
    make install
    
RUN make all
RUN make install

WORKDIR src/nrnpython
RUN python setup.py install
ENV NEURON_HOME $HOME/${NEURON_VERSIONED}/x86_64
ENV PATH $NEURON_HOME/bin:$PATH


# Install NeuroML tools
USER root
# required for libNeuroML
RUN apt-get install -y python-lxml python3-pip python-dev python3-setuptools

USER jovyan
RUN sudo chown -R jovyan /home/jovyan
WORKDIR $HOME

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade virtualenv


# Get the original source code
RUN git clone https://github.com/NeuralEnsemble/libNeuroML.git
RUN git clone https://github.com/NeuroML/pyNeuroML.git

# Build from source code

WORKDIR $HOME/libNeuroML
# 2020-05 version
RUN git checkout 632c1bce797d44308d5ec8246c0aac360c862f1a
RUN pip3 install . -r requirements.txt

WORKDIR $HOME/pyNeuroML
# 2020-05 version
RUN git checkout 9e070467498c57d4244d44f9996bb8e0eecc5dc3
RUN python3 -m pip install .


# Check if packages are imported OK
WORKDIR $WORK_HOME

RUN python3 -c "import neuroml"
RUN python3 -c "import neuroml; from pyneuroml import pynml"

# TODO some testing on NeuroML examples, to verify it's working properly (like with POisson sources and such)

#onward
WORKDIR $WORK_HOME

# ------------> Install more auxiliary tools

USER $NB_USER
# Get some auxiliar packages, for network generation on the test environment
RUN pip install netpyne==0.9.6


# ------------> Install EDEN

USER root
WORKDIR $HOME

# Get the necessary build tools
# perhaps use a ENV PACKAGES variable LATER
RUN apt-get update \
&& apt-get install -y \
build-essential gcc-7 \
flex=2.6* bison=2:3* \
xxd \
&& apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* 
# More options:
# m4 autoconf for automakeable projects
# ca-certificates for non-canon package repos
# curl cvs svn git for self-hosted reposd

# Get the necessary runtime tools
# including GCC with OpenMP
# perhaps use a ENV PACKAGES variable LATER
RUN apt-get update \
    && apt-get install -y \
	build-essential gcc-7 \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* 


ARG EDEN_CODE_REPO=/repo
ARG EDEN_INSTALL_DIR=/opt/eden
# Assume build context is project root

#TODO copy just what's required for the build (exclude testing scripts that are not required perhaps?)
COPY . ${EDEN_CODE_REPO}

WORKDIR ${EDEN_CODE_REPO}

# Add some basic Python integration
RUN pip install testing/python_package

RUN \
    mkdir -p ${EDEN_INSTALL_DIR}/bin && \
    mkdir -p ${EDEN_INSTALL_DIR}/obj && \
    CC=gcc OUT_DIR=${EDEN_INSTALL_DIR} BUILD=release make -j$(nproc) eden

RUN rm -r ${EDEN_CODE_REPO}

RUN ln -s ${EDEN_INSTALL_DIR}/bin/eden.release.gcc.cpu.x /usr/local/bin/eden

WORKDIR $HOME


# ------------> Ready to run

USER $NB_USER
WORKDIR $WORK_HOME

# to inspect
# CMD ["bash"]
# to start Jupyter (default option)
# CMD ["start-notebook.sh"]
