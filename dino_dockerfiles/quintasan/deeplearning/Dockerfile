FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
MAINTAINER Michał Zając <docker@quintasan.pl>

RUN apt-get update && apt-get install -y \
  gfortran \
  git \
  wget \
  liblapack-dev \
  libopenblas-dev \
  python3-dev \
  python3-pip \
  python3-nose \
  python3-numpy \
  python3-scipy \
  python3-six

ENV CUDA_ROOT /usr/local/cuda/bin

RUN pip3 install --upgrade ipython ipdb

RUN pip3 install --upgrade --no-deps git+git://github.com/Theano/Theano.git

RUN echo "[global]\ndevice=gpu\nfloatX=float32\n[lib]\ncnmem=0.5\n[nvcc]\nfastmath=True" > /root/.theanorc

RUN pip3 install tensorflow-gpu

RUN pip3 install --upgrade git+git://github.com/fchollet/keras.git

ENV PYTHONPATH="/src:$PYTHONPATH"

WORKDIR /workdir
COPY test.py /workdir/test.py

VOLUME /workdir

CMD python3 test.py
