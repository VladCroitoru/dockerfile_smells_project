FROM nimbix/base-ubuntu-nvidia

# Pick up some TF dependencies (TODO: minimize)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        gfortran \
        libblas-dev \
        libfreetype6-dev \
        libhdf5-dev \
        liblapack-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python \
        python-dev \
        rsync \
        software-properties-common \
        unzip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py \
 && python get-pip.py \
 && rm get-pip.py

RUN sudo pip --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        Pillow \
        scipy \
        sklearn \
 && python -m ipykernel.kernelspec

RUN sudo pip --no-cache-dir install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.0-cp27-none-linux_x86_64.whl
RUN sudo pip install \
        h5py \
        hyperopt \
        keras \
        scikit-image \
        tflearn  

# Set up our notebook config.
COPY jupyter_notebook_config.py /home/nimbix/.jupyter/

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /home/nimbix/

# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888
