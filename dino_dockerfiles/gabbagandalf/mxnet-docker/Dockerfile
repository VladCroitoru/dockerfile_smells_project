FROM ubuntu:16.04

RUN apt-get update \
	&& apt-get install -y unzip wget build-essential \
		cmake git pkg-config libswscale-dev \
		libtbb2 libtbb-dev libjpeg-dev \
		libpng-dev libtiff-dev libjasper-dev

RUN cd \
	&& wget https://github.com/opencv/opencv/archive/3.1.0.zip \
	&& unzip 3.1.0.zip \
	&& cd opencv-3.1.0 \
	&& mkdir build \
	&& cd build \
	&& cmake -DWITH_IPP=OFF .. \
	&& make -j$(nproc) \
	&& make install \
	&& cd \
    && rm 3.1.0.zip \
    && rm -rf opencv-3.1.0

RUN apt-get install -y libatlas-base-dev && \
    git clone --recursive https://github.com/dmlc/mxnet/ && cd mxnet && \
    cp make/config.mk . && \
    make -j$(nproc) && \
    cp lib/* /usr/lib && \
    cd .. && rm -rf mxnet
