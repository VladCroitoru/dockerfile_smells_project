FROM alantrrs/cuda-docker

# Verify it has cuDNN
RUN ls -la /usr/local/cuda/include | grep cudnn

ENV PYTHONPATH=/home/caffe-fast-rcnn/python:$PYTHONPATH \
    PATH=/home/conda/bin:$PATH \
    LD_LIBRARY_PATH=/home/conda/lib:$LD_LIBRARY_PATH

# Get dependencies
RUN apt-get update && apt-get install -y \
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
    unzip && \
    apt-get clean

# Install Glog and Gflags 
RUN cd /home && \
    wget --quiet https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz && \
    tar zxvf glog-0.3.3.tar.gz && \
    cd glog-0.3.3 && \
    ./configure && \
    make -j$(nproc) && \
    make install -j$(nproc) && \
    cd .. && \
    rm -rf glog-0.3.3.tar.gz && \ 
    ldconfig && \
    \
    cd /home && \
    wget --quiet https://github.com/schuhschuh/gflags/archive/master.zip && \
    unzip master.zip && \
    cd gflags-master && \
    mkdir build && \
    cd build && \
    export CXXFLAGS="-fPIC" && \
    cmake .. && \
    make VERBOSE=1 && \
    make  -j$(nproc) && \
    make install -j$(nproc) && \
    cd ../.. && \
    rm master.zip

# Install python dependencies
WORKDIR /home
RUN wget https://repo.continuum.io/archive/Anaconda-2.2.0-Linux-x86_64.sh 
RUN bash Anaconda-2.2.0-Linux-x86_64.sh -b -p /home/conda && \
    rm Anaconda-2.2.0-Linux-x86_64.sh && \
    /home/conda/bin/conda install --yes conda==3.10.1 && \
    conda install --yes cython && \
    conda install --yes opencv && \
    conda install --yes --channel https://conda.binstar.org/auto easydict 

# To remove erro when loading libreadline from anaconda
RUN rm /home/conda/lib/libreadline* && \
    ldconfig 

# Install libpng (removes run-time error )
RUN wget http://iweb.dl.sourceforge.net/project/libpng/libpng15/older-releases/1.5.15/libpng-1.5.15.tar.gz
RUN tar -xvf libpng-1.5.15.tar.gz
WORKDIR /home/libpng-1.5.15
RUN ./configure && make -j8 && make install

# Setup caffe-fast-rcnn
ADD . /home/caffe-fast-rcnn
WORKDIR /home/

# Install Python requirements
WORKDIR /home/caffe-fast-rcnn/python 
RUN pip install -r requirements.txt

# Configure & Build caffe
WORKDIR /home/caffe-fast-rcnn
RUN cp Makefile.config.example Makefile.config
RUN echo "CXX := /usr/bin/g++-4.6" >> Makefile.config && \
    echo "USE_CUDNN := 1" >> Makefile.config && \
    echo "ANACONDA_HOME := /home/conda" >> Makefile.config && \
    echo 'PYTHON_INCLUDE := $(ANACONDA_HOME)/include $(ANACONDA_HOME)/include/python2.7 $(ANACONDA_HOME)/lib/python2.7/site-packages/numpy/core/include' >> Makefile.config && \
    echo 'PYTHON_LIB := $(ANACONDA_HOME)/lib' >> Makefile.config && \
    echo 'INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/local/cuda/include' >> Makefile.config && \
    echo 'LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib' >> Makefile.config && \
    echo 'WITH_PYTHON_LAYER := 1' >> Makefile.config && \
    sed -i 's/CXX :=/CXX ?=/' Makefile 

RUN cat Makefile.config
RUN make -j8  && make pycaffe


