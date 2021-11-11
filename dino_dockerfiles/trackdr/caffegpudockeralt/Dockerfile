# Start with CUDA base image
FROM trackdr/cudadocker
MAINTAINER me

# Install git, bc and dependencies
RUN apt-get update && apt-get install -y \
  git \
  bc \
  libatlas-base-dev \
  libatlas-dev \
  libboost-all-dev \
  libprotobuf-dev \
  libgoogle-glog-dev \
  libgflags-dev \
  protobuf-compiler \
  libhdf5-dev \
  libleveldb-dev \
  liblmdb-dev \
  libsnappy-dev \
  python-pip \
  python-dev \
  python-numpy \
  python-scipy \
  python-skimage \
  python-protobuf \
  python-yaml \
  libopencv-dev

# Copy cudnn libraries into docker file
#COPY cudnn/cudnn-6.5-linux-x64-v2/libcudnn.so /usr/local/cuda/lib64/libcudnn.so
#COPY cudnn/cudnn-6.5-linux-x64-v2/libcudnn.so.6.5 /usr/local/cuda/lib64/libcudnn.so.6.5
#COPY cudnn/cudnn-6.5-linux-x64-v2/libcudnn.so.6.5.48 /usr/local/cuda/lib64/libcudnn.so.6.5.48
#COPY cudnn/cudnn-6.5-linux-x64-v2/cudnn.h /usr/local/cuda/include/cudnn.h
#COPY cuda_7.0.28_linux.run /cuda_7.0.28_linux.run

#WORKDIR /
#RUN ./cuda_7.0.28_linux.run -extract=`pwd`
#RUN ./cuda-samples-linux-*.run -noprompt
#RUN cd /usr/local/cuda-7.0/samples/1_Utilities/deviceQuery && make

# Clone Caffe repo and move into it
RUN cd /opt && git clone https://github.com/BVLC/caffe.git && cd caffe
RUN cd /opt/caffe/python && for req in $(cat requirements.txt); do pip install $req; done
RUN cd /opt/caffe && cp Makefile.config.example Makefile.config
RUN cd /opt/caffe && sed -i '/^# WITH_PYTHON_LAYER := 1/s/^# //' Makefile.config
#RUN cd /opt/caffe && sed -i '/^# USE_CUDNN := 1/s/^# //' Makefile.config
RUN cd /opt/caffe && make all
RUN cd /opt/caffe && make pycaffe
RUN cd /opt/caffe && make test

ENV PYTHONPATH /opt/caffe/python:$PYTHONPATH
