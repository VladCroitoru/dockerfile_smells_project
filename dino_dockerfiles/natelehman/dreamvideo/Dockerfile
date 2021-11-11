FROM debian

RUN apt-get clean && apt-get update && apt-get install -y \
	bc \
	ca-certificates \
	curl \
	cython \
	g++ \
	git \
	ipython \
	libatlas-base-dev \
	libatlas-dev \
	libboost-all-dev \
	libgflags-dev \
	libgoogle-glog-dev \
	libhdf5-dev \
	libleveldb-dev \
	liblmdb-dev \
	libopencv-dev \
	libprotobuf-dev \
	libsnappy-dev \
	make \
	protobuf-compiler \
	python-dateutil \
	python-gflags \
	python-h5py \
	python-leveldb \
	python-matplotlib \
	python-networkx \
	python-nose \
	python-numpy \
	python-pandas \
	python-pil \
	python-protobuf \
	python-scipy \
	python-skimage-lib \
	python-yaml \
        libav-tools \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

RUN curl https://bootstrap.pypa.io/get-pip.py | python

RUN pip install scikit-image

RUN cd root && git clone --depth 1 --single-branch https://github.com/BVLC/caffe.git

RUN curl http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel > /root/caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel

RUN cd /root/caffe && \
	cp Makefile.config.example Makefile.config && \
        sed -i 's/# CPU_ONLY/CPU_ONLY/g' Makefile.config && \
	echo 'INCLUDE_DIRS += /usr/include/hdf5/serial' >> Makefile.config && \
	echo 'LIBRARY_DIRS += /usr/lib/x86_64-linux-gnu/hdf5/serial' >> Makefile.config && \
	make -j"$(nproc)" all pycaffe

ENV PYTHONPATH=/root/caffe/python
WORKDIR /ddd

COPY start.sh /ddd/
COPY deepdreams.py /ddd/
COPY frames2movie.sh /ddd/

RUN mkdir /images

VOLUME /images

ENTRYPOINT ["/ddd/start.sh"]
