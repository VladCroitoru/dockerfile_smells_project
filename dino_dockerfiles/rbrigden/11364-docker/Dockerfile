FROM ubuntu:14.04

# Credits to Sai Soundararaj <saip@outlook.com> for
# the original template of this image.
MAINTAINER Ryan Brigden <rbrigden@cmu.edu>

ARG THEANO_VERSION=rel-0.8.2
ARG TENSORFLOW_VERSION=0.8.0
ARG TENSORFLOW_ARCH=cpu
ARG KERAS_VERSION=1.0.3

# Install some dependencies
RUN apt-get update && apt-get install -y \
		bc \
		build-essential \
		cmake \
		curl \
		g++ \
		gfortran \
		git \
		libffi-dev \
		libhdf5-dev \
		liblcms2-dev \
		libopenblas-dev \
		liblapack-dev \
		pkg-config \
		python-dev \
		software-properties-common \
		unzip \
		wget \
		zlib1g-dev \
		&& \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/* && \
# Link BLAS library to use OpenBLAS using the alternatives mechanism (https://www.scipy.org/scipylib/building/linux.html#debian-ubuntu)
	update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3

# Install pip
RUN curl -O --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py && \
	python get-pip.py && \
	rm get-pip.py

# Install useful Python packages using apt-get to avoid version incompatibilities with Tensorflow binary
# especially numpy, scipy, skimage and sklearn (see https://github.com/tensorflow/tensorflow/issues/2034)
RUN apt-get update && apt-get install -y \
		python-numpy \
		python-scipy \
		python-matplotlib \
		python-pandas \
		python-sklearn \
		&& \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*

# Install other useful Python packages using pip
RUN pip --no-cache-dir install \
		Cython \
    scikit-neuralnetwork

# Install TensorFlow
RUN pip --no-cache-dir install \
	https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_ARCH}/tensorflow-${TENSORFLOW_VERSION}-cp27-none-linux_x86_64.whl

# Install Theano and set up Theano config (.theanorc) OpenBLAS
RUN pip --no-cache-dir install git+git://github.com/Theano/Theano.git@${THEANO_VERSION} && \
	\
	echo "[global]\ndevice=cpu\nfloatX=float32\nmode=FAST_RUN \
		\n[lib]\ncnmem=0.95 \
		\n[nvcc]\nfastmath=True \
		\n[blas]\nldflag = -L/usr/lib/openblas-base -lopenblas \
		\n[DebugMode]\ncheck_finite=1" \
	> /root/.theanorc

# Install Keras
RUN pip --no-cache-dir install git+git://github.com/fchollet/keras.git@${KERAS_VERSION}


WORKDIR "/root"
CMD ["/bin/bash"]
