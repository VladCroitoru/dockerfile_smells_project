FROM debian:8.2
MAINTAINER Sébastien Gruchet <gruchet@gmail.com>

RUN apt-get update && apt-get install -y \
    git bc libatlas-base-dev libatlas-dev libboost-all-dev libopencv-dev \ 
    libprotobuf-dev libgoogle-glog-dev libgflags-dev protobuf-compiler \
    libhdf5-dev libleveldb-dev liblmdb-dev libsnappy-dev python python-pip \
    python-numpy python-scipy python-pandas python-matplotlib cython python-six \ 
    python-protobuf python-networkx python-h5py python-skimage-lib gcc g++ make \
    ipython ca-certificates --no-install-recommends

RUN cd /usr/share && \
    git clone https://github.com/calou/caffe.git && \
    cd caffe && \
    cp Makefile.config.example Makefile.config && \
    sed -i 's/# CPU_ONLY/CPU_ONLY/g' Makefile.config && \
    echo 'INCLUDE_DIRS += /usr/include/hdf5/serial' >> Makefile.config && \
    echo 'LIBRARY_DIRS += /usr/lib/x86_64-linux-gnu/hdf5/serial' >> Makefile.config && \
    make -j"$(nproc)" all pycaffe && \
    cd python && \
    pip install -r requirements.txt 
    
RUN rm -rf /var/lib/apt/lists/* && apt-get remove -y git  

ENV PYTHONPATH=/usr/share/caffe/python

VOLUME /data

ENTRYPOINT ["python"]
