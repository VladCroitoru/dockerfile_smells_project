FROM ubuntu:16.04

RUN locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    CONDARC=/opt/conda/.condarc \
    BASH_ENV=/etc/profile \
    PATH=/opt/conda/bin:$PATH

RUN DEBIAN_FRONTEND=noninteractive apt-get update -y && \
    apt-get install -y software-properties-common && \
    apt-get install -y \
        automake \
        bzip2 \
        curl \
        g++ \
        gfortran \
        git \
        libboost-program-options-dev \
        libpq-dev \
        libtool \
        libxrender1 \
        make \
        wget

# miniconda
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.2.11-Linux-x86_64.sh -O /usr/local/src/miniconda.sh && \
    /bin/bash /usr/local/src/miniconda.sh -b -p /opt/conda && \
    rm /usr/local/src/miniconda.sh

# Python libraries
ARG python_version=3.5.2
ARG TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc1-cp35-cp35m-linux_x86_64.whl

RUN conda install -y python=${python_version} && \
    conda install pandas scikit-learn jupyter notebook matplotlib seaborn && \
    pip install theano && \
    pip install keras && \
    pip install ${TF_BINARY_URL}

# xgboost
RUN cd /usr/local/src && mkdir xgboost && cd xgboost && \
    git clone --recursive https://github.com/dmlc/xgboost && \
    cd xgboost && make -j4 && \
    cd python-package && python setup.py install

COPY run_jupyter.sh /

# Jupyter
EXPOSE 8888

CMD ["bash", "/run_jupyter.sh"]
