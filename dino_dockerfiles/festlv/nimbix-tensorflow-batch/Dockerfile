FROM nimbix/base-ubuntu-nvidia

RUN apt-get update && \
    apt-get install -y --no-install-recommends gfortran python-dev python-pip libhdf5-dev libblas-dev liblapack-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN sudo pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp27-none-linux_x86_64.whl
RUN sudo pip install h5py hyperopt tflearn

COPY test-libs.py /test-libs.py
