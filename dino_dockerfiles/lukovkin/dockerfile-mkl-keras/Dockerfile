FROM ubuntu

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    mercurial \
    nano \
    vim \
  && rm -rf /var/lib/apt/lists/*

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
    quandl
RUN source activate keras \
  && pip install --no-deps git+git://github.com/Theano/Theano.git \
  && pip install git+git://github.com/pykalman/pykalman.git \
  && pip install git+git://github.com/fchollet/keras.git --no-deps

RUN echo $'[global]\nopenmp = True\n' > ~/.theanorc

ENV OMP_NUM_THREADS=12

RUN source activate keras \
  && git config --global http.sslVerify false \
  && git clone https://github.com/lukovkin/hyperopt.git \
  && cd hyperopt/ \
  && git checkout fmin-fix \
  && python setup.py install
