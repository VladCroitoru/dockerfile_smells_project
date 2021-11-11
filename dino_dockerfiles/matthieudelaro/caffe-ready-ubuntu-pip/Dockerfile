# Don't edit this file directly, since it was generated from a template,
# and you're changes will be *clobbered*.  Edit the template instead.

# inspired by tleyden5iwx/caffe-gpu-master

FROM nvidia/cuda:7.5-cudnn4-devel

ENV PYTHONPATH /opt/caffe/python

# Add caffe binaries to path
ENV PATH $PATH:/opt/caffe/.build_release/tools

# Get dependencies
RUN apt-get update -m && apt-get install -y \
  bc \
  cmake \
  curl \
  gcc-4.6 \
  g++-4.6 \
  gcc-4.6-multilib \
  g++-4.6-multilib \
  gfortran \
  git \
  libprotobuf-dev \
  libleveldb-dev \
  libsnappy-dev \
  libopencv-dev \
  libboost-all-dev \
  libhdf5-serial-dev \
  liblmdb-dev \
  libjpeg62 \
  libfreeimage-dev \
  libatlas-base-dev \
  pkgconf \
  protobuf-compiler \
  python-dev \
  python-pip \
  unzip \
  wget

# Use gcc 4.6
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.6 30 && \
  update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.6 30 && \
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.6 30 && \
  update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.6 30


# Allow it to find CUDA libs
RUN echo "/usr/local/cuda/lib64" > /etc/ld.so.conf.d/cuda.conf && \
  ldconfig


# Glog
RUN cd /opt && wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz && \
  tar zxvf glog-0.3.3.tar.gz && \
  cd /opt/glog-0.3.3 && \
  ./configure && \
  make -j8 && \
  make install

# Workaround for error loading libglog:
#   error while loading shared libraries: libglog.so.0: cannot open shared object file
# The system already has /usr/local/lib listed in /etc/ld.so.conf.d/libc.conf, so
# running `ldconfig` fixes the problem (which is simpler than using $LD_LIBRARY_PATH)
# TODO: looks like this needs to be run _every_ time a new docker instance is run,
#       so maybe LD_LIBRARY_PATh is a better approach (or add call to ldconfig in ~/.bashrc)
RUN ldconfig

# Gflags
RUN cd /opt && \
  wget https://github.com/schuhschuh/gflags/archive/master.zip && \
  unzip master.zip && \
  cd /opt/gflags-master && \
  mkdir build && \
  cd /opt/gflags-master/build && \
  export CXXFLAGS="-fPIC" && \
  cmake .. && \
  make VERBOSE=1 && \
  make -j8 && \
  make install

# install python dependencies for Caffe. They may change a little bit from a version to another,
# but it doesn't harm to have most of them already installed.
RUN pip install "Cython>=0.19.2" && pip install "numpy>=1.7.1" && pip install "scipy>=0.13.2" && pip install "scikit-image>=0.9.3" && pip install "matplotlib>=1.3.1" && pip install "ipython>=3.0.0" && pip install "h5py>=2.2.0" && pip install "leveldb>=0.191" && pip install "networkx>=1.8.1" && pip install "nose>=1.3.0" && pip install "pandas>=0.12.0" && pip install "python-dateutil>=1.4,<2" && pip install "protobuf>=2.5.0" && pip install "python-gflags>=2.0" && pip install "pyyaml>=3.10" && pip install "Pillow>=2.3.0" 

# # Clone the Caffe repo
# RUN cd /opt && git clone https://github.com/BVLC/caffe.git

# # Build Caffe core
# RUN cd /opt/caffe && \
#   cp Makefile.config.example Makefile.config && \
#    \ 
#   echo "CXX := /usr/bin/g++-4.6" >> Makefile.config && \
#   sed -i 's/CXX :=/CXX ?=/' Makefile && \
#   make all

# # Add ld-so.conf so it can find libcaffe.so
# # ADD caffe-ld-so.conf /etc/ld.so.conf.d/
# RUN echo "/opt/caffe/.build_release/lib/" >> /etc/ld.so.conf.d/caffe-ld-so.conf 

# # Run ldconfig again (not sure if needed)
# RUN ldconfig

# # Install python deps
# RUN cd /opt/caffe && \
#   cat python/requirements.txt | xargs -L 1 sudo pip install

# # Numpy include path hack - github.com/BVLC/caffe/wiki/Ubuntu-14.04-VirtualBox-VM
# RUN ln -s /usr/include/python2.7/ /usr/local/include/python2.7 && \
#   ln -s /usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy/ /usr/local/include/python2.7/numpy

# # Build Caffe python bindings
# RUN cd /opt/caffe && make pycaffe -j8
