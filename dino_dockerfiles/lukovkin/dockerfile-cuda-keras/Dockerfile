# Start with cuDNN base image
FROM kaixhin/cudnn:7.0

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libglib2.0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git \
    mercurial \
    nano \
    vim \
  && rm -rf /var/lib/apt/lists/*
  
# Set CUDA_ROOT
ENV CUDA_ROOT /usr/local/cuda/bin

RUN curl -qsSLkO \
    https://repo.continuum.io/miniconda/Miniconda-latest-Linux-`uname -p`.sh \
  && bash Miniconda-latest-Linux-`uname -p`.sh -b \
  && rm Miniconda-latest-Linux-`uname -p`.sh

ENV PATH=/root/miniconda2/bin:$PATH

RUN conda create --name keras python=3

RUN source activate keras \
  && conda install -y \
    mkl \
    h5py \
    pandas \
    scikit-learn \
    networkx \
    pyyaml \
    pymongo \
    smart_open \
    matplotlib \
    sqlalchemy \
    psycopg2 \
    quandl
    
RUN source activate keras \
  && pip install --no-deps git+git://github.com/Theano/Theano.git \
  && pip install git+git://github.com/pykalman/pykalman.git \
  && pip install git+git://github.com/fchollet/keras.git --no-deps \
  && pip install git+https://github.com/quantopian/zipline

# Set up .theanorc for CUDA
RUN echo "[global]\ndevice=gpu\nfloatX=float32\nopenmp = True\n[lib]\ncnmem=1\n[nvcc]\nfastmath=True" > /root/.theanorc

ENV THEANO_FLAGS="mode=FAST_RUN,device=gpu,floatX=float32"
ENV OMP_NUM_THREADS=8
ENV PYTHONPATH=/notebook/nnt-backend-py/

RUN source activate keras \
  && git config --global http.sslVerify false \
  && pip install --no-deps git+https://github.com/lukovkin/hyperopt.git \
  && pip install git+https://github.com/lukovkin/holidays.py.git \
  && pip install bdateutil
