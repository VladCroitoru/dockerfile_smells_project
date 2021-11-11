FROM nvidia/cuda:7.0-cudnn4-devel
ENV CAFFE_VERSION 0.14
ENV RR_CONTAINER hmlatapie/rr_caffe
LABEL com.nvidia.caffe.version="0.14"
ENV CAFFE_PKG_VERSION 0.14.2-1

#install basic environment
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y aptitude \
  && apt-get install -y ipython \
  && apt-get install -y python-pip \
  && apt-get install -y man \
  && apt-get install -y vim \
  && apt-get install -y wget \
  && apt-get install -y git 

#install nvidia's flavor of caffe from source
RUN apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        python-scipy

ENV CAFFE_ROOT=/root/caffe
ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYTHON_ROOT:$PATH
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/apollocaffe/build/lib
ENV PYTHONPATH=$PYTHONPATH:/root/apollocaffe/python

RUN cd /root \
	&& git clone https://github.com/BVLC/caffe.git \
	&& cd caffe \
	&& for req in $(cat python/requirements.txt) pydot; do pip install $req; done \
	&& mkdir build \
	&& cd build \
	&& cmake -DUSE_CUDNN=1 .. \
 	&& make -j"$(nproc)"

RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

#install apollo caffe
RUN cd /tmp \
   && git clone https://github.com/hmlatapie/rr_caffe \
  	&& cd /root  \
	&& git clone http://github.com/Russell91/apollocaffe.git \
	&& cd apollocaffe \
   && cp /tmp/rr_caffe/install_test/Makefile.config . \
	&& for req in $(cat python/requirements.txt); do pip install $req; done \
   && make -j"$(nproc)" 

#install mongo
RUN pip install pymongo

#install sacred
RUN cd /root && git clone https://github.com/IDSIA/sacred.git && cd sacred && python setup.py install

RUN apt-get install -y --no-install-recommends --force-yes \
            caffe-nv=$CAFFE_PKG_VERSION \
            caffe-nv-tools=$CAFFE_PKG_VERSION \
            python-caffe-nv=$CAFFE_PKG_VERSION && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get upgrade -y && apt-get install python-opencv \
	&& pip install drawnow \
	&& pip install sympy \
	&& pip install munkres \
	&& cpan YAML:Syck \
	&& apt-get install -y gfortran \
	&& pip install Flask \
	&& pip install --upgrade numpy \
	&& pip install --upgrade cv2 \
	&& pip install --upgrade sympy \
	&& pip install --upgrade scipy \
	&& pip install --upgrade munkres \
	&& pip install --upgrade Flask

VOLUME /root/rr
WORKDIR /root

CMD /bin/bash

