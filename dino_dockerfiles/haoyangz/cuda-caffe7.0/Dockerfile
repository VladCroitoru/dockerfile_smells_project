# Start with CUDA base image
FROM kaixhin/cuda:7.0

# Install git, bc and dependencies
RUN apt-get update && apt-get install -y \
  git \
  bc \
  libatlas-base-dev \
  libatlas-dev \
  libboost-all-dev \
  libopencv-dev \
  libprotobuf-dev \
  libgoogle-glog-dev \
  libgflags-dev \
  protobuf-compiler \
  libhdf5-dev \
  libleveldb-dev \
  liblmdb-dev \
  libsnappy-dev \
  python-pip \
  python-numpy \
  gfortran
  
RUN pip install --upgrade pip 

# Clone Caffe repo and move into it
RUN mkdir /scripts
RUN cd /scripts && git clone https://github.com/BVLC/caffe.git && cd caffe && \
# Copy Makefile
  cp Makefile.config.example Makefile.config && \
# Make
  make -j"$(nproc)" all && \
  cd python && \
  for req in $(cat requirements.txt); do pip install $req; done && \
  cd .. && \
  make pycaffe
  
ENV PYTHONPATH /scripts/caffe/python:$PYTHONPATH
