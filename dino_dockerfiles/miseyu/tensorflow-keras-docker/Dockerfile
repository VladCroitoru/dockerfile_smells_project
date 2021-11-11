FROM debian:jessie

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y \
        python3 \
        curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python3-numpy \
        python3-pip \
        python3-scipy \
        git \
        libhdf5-dev \
        graphviz \
        vim \
        imagemagick \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN cp /usr/bin/python3 /usr/bin/python && cp /usr/bin/pip3 /usr/bin/pip

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

RUN pip --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        h5py \
        pydot-ng \
        graphviz \
        tweepy \
        && \
    python -m ipykernel.kernelspec

# Install TensorFlow CPU version.
ENV TENSORFLOW_VERSION 1.0.0
RUN pip --no-cache-dir install \
    https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp34-cp34m-linux_x86_64.whl

# Set up our notebook config.
# COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
# COPY run_jupyter.sh /

RUN pip install git+git://github.com/Theano/Theano.git
RUN pip install keras

WORKDIR "/root"

# Copy some examples
RUN git clone git://github.com/fchollet/keras.git

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

COPY keras.json /root/.keras/keras.json
COPY . /root

CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token=
