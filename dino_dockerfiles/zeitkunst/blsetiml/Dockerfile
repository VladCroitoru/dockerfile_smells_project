# Building based off of https://github.com/floydhub/dl-docker
FROM ubuntu:16.04

MAINTAINER Nicholas Knouf <nknouf@wellesley.edu>

RUN apt-get update && apt-get install -y \
		bc \
		build-essential \
		curl \
		g++ \
		gfortran \
		git \
		libssl-dev \
		python-tk \
		python-dev \
		python-numpy \
		unzip \
		vim \
		wget \
		&& \
		apt-get clean && \
		apt-get autoremove && \ 
        rm -rf /var/lib/apt/lists/* 

# Install pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
	python get-pip.py && \
	rm get-pip.py

# Add SNI support to Python
RUN pip --no-cache-dir install \
		pyopenssl \
		ndg-httpsclient \
		pyasn1

# Install useful Python packages using apt-get to avoid version incompatibilities with Tensorflow binary
# especially numpy, scipy, skimage and sklearn (see https://github.com/tensorflow/tensorflow/issues/2034)
RUN apt-get update && apt-get install -y \
		python-astropy \
		python-numpy \
		python-scipy \
		python-nose \
		python-h5py \
		python-skimage \
		python-matplotlib \
		python-pandas \
		python-sklearn \
		python-sympy \
		&& \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*

# Install other useful Python packages using pip
RUN pip --no-cache-dir install --upgrade ipython && \
	pip --no-cache-dir install \
		Cython \
		ipykernel \
		jupyter \
		path.py \
		Pillow \
		pygments \
		six \
		sphinx \
		wheel \
		zmq \
		&& \
	python -m ipykernel.kernelspec



# Set up notebook config
COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly: https://github.com/ipython/ipython/issues/7062
COPY run_jupyter.sh /work/

COPY filterbank.py /work/

## Expose Ports for TensorBoard (6006), Ipython (8888)
#EXPOSE 6006 8888
EXPOSE 8888

WORKDIR "/work"
CMD ["/bin/bash"]
