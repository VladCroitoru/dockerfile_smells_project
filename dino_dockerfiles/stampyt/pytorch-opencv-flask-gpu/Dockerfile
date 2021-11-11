FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

RUN apt-get update && apt-get install -y \
		build-essential \
		cmake \
		curl \
		git


RUN apt-get update && apt-get install -y \
		libffi-dev \
		libfreetype6-dev \
		libhdf5-dev \
		libjpeg-dev \
		liblcms2-dev \
		libopenblas-dev \
		liblapack-dev \
		libopenjpeg5 \
		libpng12-dev

RUN apt-get update && apt-get install -y \
		software-properties-common

RUN add-apt-repository ppa:jonathonf/python-3.6 -y && apt update -y && apt install python3.6 -y
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1

ENV PYTHON_VERSION 3.6.5

RUN apt-get update && apt-get install -y \
		pkg-config \
		unzip \
		vim \
		wget \
		zlib1g-dev \
		libjpeg-dev \
		libpng-dev \
		libtiff5-dev \
		libjasper-dev \
		libopenexr-dev \
		libgdal-dev \
		libdc1394-22-dev \
		libavcodec-dev \
		libavformat-dev \
		libswscale-dev
RUN apt-get update && apt-get install -y \
		libtheora-dev \
		libvorbis-dev \
		libxvidcore-dev \
		libx264-dev \
		yasm \
		libopencore-amrnb-dev \
		libopencore-amrwb-dev \
		libv4l-dev \
		libxine2-dev \
		libtbb-dev \
		libeigen3-dev

RUN apt-get update && apt-get install -y \
        python3-distutils\
	python3-requests\
	default-jdk &&\
     rm -rf /var/lib/apt/lists/*

# Install pip
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --upgrade pip

# Install useful Python packages using apt-get to avoid version incompatibilities with Tensorflow binary
# especially numpy, scipy, skimage and sklearn (see https://github.com/tensorflow/tensorflow/issues/2034)
RUN apt-get update && apt-get install -y \
		python3-skimage \
		python3-scipy \
		&& \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*


# Install pytorch
RUN python3 -m pip install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp36-cp36m-linux_x86_64.whl
RUN python3 -m pip install torchvision

# Install opencv
RUN python3 -m pip install opencv-python


# Install Flask
RUN python3 -m pip install Flask