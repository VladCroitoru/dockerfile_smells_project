FROM ubuntu:14.04
MAINTAINER Melissa Gymrek <mgymrek@mit.edu>

# Install Ubuntu packages
RUN apt-get -qqy update
RUN apt-get install -y -q git curl python-pip cython libxft-dev libblas-dev liblapack-dev libatlas-base-dev gfortran libhdf5-dev wget bedtools
RUN mkdir -p /home/workspace
RUN mkdir -p /home/workspace/cuda

# Install torch
RUN curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
RUN git clone https://github.com/torch/distro.git /home/workspace/torch --recursive
WORKDIR /home/workspace/torch
RUN ./install.sh
RUN bash -c "source ~/.bashrc"

# Install python dependencies
RUN pip install numpy matplotlib seaborn pandas h5py sklearn pysam

# Install basset
RUN git clone https://github.com/davek44/Basset.git /home/workspace/Basset
WORKDIR /home/workspace/Basset
ENV BASSETDIR /home/workspace/Basset
ENV PATH $BASSETDIR/src:/home/workspace/torch/install/bin/:$PATH
ENV PYTHONPATH $BASSETDIR/src:$PYTHONPATH
RUN ./install_dependencies.py

# Set up LUA_PATH
RUN echo 'export LUA_PATH="$BASSETDIR/src/?.lua;${LUA_PATH}"' >> ~/.bashrc
RUN bash -c "source ~/.bashrc"
