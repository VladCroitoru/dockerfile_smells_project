FROM nvidia/cuda:8.0-cudnn5-devel
MAINTAINER volodimir@gmail.com

#General Dependencies
RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y sudo \
  git \
  cmake \
  vim   \
  wget \
  unzip \
  dh-autoreconf \
  build-essential \
  pkg-config \
  graphviz \
  python-dev \
  python-flask \
  python-flaskext.wtf \
  python-gevent \
  python-h5py \
  python-numpy \
  python-pil \
  python-pip \
  python-protobuf \
  python-scipy \
  libprotobuf-dev \
  libleveldb-dev \
  libsnappy-dev \
  libopencv-dev \
  libhdf5-serial-dev \
  protobuf-compiler \
  libboost-all-dev \
  doxygen \
  luarocks \
  libgflags-dev \
  libgoogle-glog-dev \
  liblmdb-dev \
  libatlas-base-dev \
  software-properties-common \    
  libhdf5-dev 

RUN pip install --upgrade pip

RUN sudo apt-get install -y    \
  gfortran  \
  python-all-dev \
  python-matplotlib \
  python-opencv \
  python-skimage \
  python-sklearn


#CAFFE INSTALLATION
# example location - can be customized
ENV CAFFE_ROOT=/root/caffe
RUN git clone https://github.com/NVIDIA/caffe.git $CAFFE_ROOT
RUN cat $CAFFE_ROOT/python/requirements.txt | xargs -n1 sudo pip install
WORKDIR /root/caffe
RUN mkdir build
WORKDIR /root/caffe/build
RUN cmake ..
RUN make -j $(($(nproc) + 1))
ENV PYTHONPATH=/root/caffe/python

#TORCH INSTALLATION
# example location - can be customized
ENV TORCH_ROOT=/root/torch
RUN git clone https://github.com/torch/distro.git $TORCH_ROOT --recursive
WORKDIR /root/torch
RUN ./install-deps
RUN ./install.sh -b
RUN /bin/bash -c "source /root/.bashrc"
RUN sudo apt-get install --no-install-recommends  
RUN /root/torch/install/bin/luarocks install tds
RUN /root/torch/install/bin/luarocks install "https://raw.github.com/deepmind/torch-hdf5/master/hdf5-0-0.rockspec"
RUN /root/torch/install/bin/luarocks install "https://raw.github.com/Neopallium/lua-pb/master/lua-pb-scm-0.rockspec"
RUN /root/torch/install/bin/luarocks install lightningmdb 0.9.18.1-1 LMDB_INCDIR=/usr/include LMDB_LIBDIR=/usr/lib/x86_64-linux-gnu
# If you have installed NCCL
#RUN /root/torch/install/bin/luarocks install "https://raw.githubusercontent.com/ngimel/nccl.torch/master/nccl-scm-1.rockspec"

#DIGITS INSTALLATION
# example location - can be customized
ENV DIGITS_ROOT=/root/digits
RUN git clone https://github.com/NVIDIA/DIGITS.git $DIGITS_ROOT
RUN sudo pip install -r $DIGITS_ROOT/requirements.txt

WORKDIR /root/digits/tools/
COPY download_data .
RUN ./main.py mnist ~/mnist
WORKDIR /root/digits
ENTRYPOINT /root/digits/digits-devserver -d
#RUN echo $PATH
EXPOSE 5000
