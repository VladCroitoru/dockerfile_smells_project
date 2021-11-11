# docker-debian-cuda - Debian 9 with CUDA Toolkit

FROM gw000/keras:2.1.4-gpu
MAINTAINER gw0 [http://gw.tnode.com/] <gw.2017@ena.one>

# install py2-tf-cpu/gpu (Python 2, TensorFlow, CPU/GPU)
# (already installed in upstream image)

# install py2-th-cpu (Python 2, Theano, CPU/GPU)
ARG THEANO_VERSION=1.0.3
ENV THEANO_FLAGS='device=cpu,floatX=float32'
RUN pip --no-cache-dir install git+https://github.com/Theano/Theano.git@rel-${THEANO_VERSION}

# install py3-tf-cpu/gpu (Python 3, TensorFlow, CPU/GPU)
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \

    # install python 3
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-virtualenv \
    python3-wheel \
    pkg-config \
    # requirements for numpy
    libopenblas-base \
    python3-numpy \
    python3-scipy \
    # requirements for keras
    python3-h5py \
    python3-yaml \
    python3-pydot \
    libopenblas-base \
    # requirements
    python3-matplotlib \
    python3-pandas \
    python3-sklearn \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
 
# manually update numpy
RUN pip3 --no-cache-dir install -U numpy==1.15.4

ARG TENSORFLOW_VERSION=1.12.0
ARG TENSORFLOW_DEVICE=cpu
ARG TENSORFLOW_APPEND=
RUN pip3 --no-cache-dir install https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_DEVICE}/tensorflow${TENSORFLOW_APPEND}-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl

ARG KERAS_VERSION=2.2.4
ENV KERAS_BACKEND=tensorflow
RUN pip3 --no-cache-dir install git+https://github.com/fchollet/keras.git@${KERAS_VERSION}

# install py3-th-cpu/gpu (Python 3, Theano, CPU/GPU)
ARG THEANO_VERSION=1.0.3
ENV THEANO_FLAGS='device=cpu,floatX=float32'
RUN pip3 --no-cache-dir install git+https://github.com/Theano/Theano.git@rel-${THEANO_VERSION}

# install additional debian packages
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \
    # system tools
    less \
    procps \
    vim-tiny \
    # build dependencies
    build-essential \
    libffi-dev \
    # visualization (Python 2 and 3)
    python-matplotlib \
    python-pillow \
    python3-matplotlib \
    python3-pillow \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# install additional python packages
RUN pip --no-cache-dir install \
    # jupyter notebook and ipython (Python 2)
    ipython \
    ipykernel \
    jupyter \
    jupyter_kernel_gateway \
    jupyter-tensorboard \
    # data analysis (Python 2)
    pandas \
    scikit-learn \
    tflearn \
    statsmodels \
    tensorlayer \
    # nlp (Python 2)
    nltk \
    gensim \
    jieba \
    spacy \
    thulac \
    # webapi
    flask \
 && python -m ipykernel.kernelspec \
 && pip3 --no-cache-dir install \
    # jupyter notebook and ipython (Python 3)
    ipython \
    ipykernel \
    # data analysis (Python 3)
    pandas \
    scikit-learn \
    tflearn \
    statsmodels \
    tensorlayer \
    # nlp (Python 2)
    nltk \
    gensim \
    jieba \
    spacy \
    thulac \
    # webapi
    flask \
 && python3 -m ipykernel.kernelspec

# configure console
RUN echo 'alias ll="ls --color=auto -lA"' >> /root/.bashrc \
 && echo '"\e[5~": history-search-backward' >> /root/.inputrc \
 && echo '"\e[6~": history-search-forward' >> /root/.inputrc
 
ENV SHELL=/bin/bash
# default password: keras
ENV PASSWD='sha1:98b767162d34:8da1bc3c75a0f29145769edc977375a373407824'

# quick test and dump package lists

RUN jupyter notebook --version \

 && jupyter nbextension list 2>&1 \
 && python -c "import numpy; print(numpy.__version__)" \
 && python -c "import tensorflow; print(tensorflow.__version__)" \
 && python -c "import theano; print(theano.__version__)" \
 && MPLBACKEND=Agg python -c "import matplotlib.pyplot" \
 && python3 -c "import numpy; print(numpy.__version__)" \
 && python3 -c "import tensorflow; print(tensorflow.__version__)" \
 && python3 -c "import theano; print(theano.__version__)" \
 && MPLBACKEND=Agg python3 -c "import matplotlib.pyplot" \
 && rm -rf /tmp/* \
 && dpkg-query -l > /dpkg-query-l.txt \
 && pip2 freeze > /pip2-freeze.txt \
 && pip3 freeze > /pip3-freeze.txt

# dump package lists


# for jupyter
EXPOSE 8888
# for tensorboard
EXPOSE 6006
# for jupyter_kernel_gateway
EXPOSE 9001
# for jupyter_kernel_gateway
EXPOSE 5000

WORKDIR /srv/

CMD /bin/bash -c 'jupyter notebook \
    --NotebookApp.open_browser=False \
    --NotebookApp.allow_root=True \
    --NotebookApp.ip="$IP" \
    ${PASSWD+--NotebookApp.password=\"$PASSWD\"} \
    ${TOKEN+--NotebookApp.token=\"$TOKEN\"} \
    --NotebookApp.allow_password_change=False \
    --JupyterWebsocketPersonality.list_kernels=True \
    "$@"'
