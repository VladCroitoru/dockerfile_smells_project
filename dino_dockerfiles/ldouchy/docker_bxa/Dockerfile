# BXA container 
# https://johannesbuchner.github.io/BXA

FROM ldouchy/docker_heasoft:latest

MAINTAINER ldouchy

LABEL description="BXA https://johannesbuchner.github.io/BXA"

ENV	LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/MultiNest/lib \
	MULTINEST=$MULTINEST:/opt/MultiNest \
	PYTHONPATH=$PYTHONPATH:/opt/custom/complex_pymultinest/LF_modules/configuration:/opt/custom/complex_pymultinest/LF_modules/models:/opt/BXA	 

WORKDIR /opt

RUN 	apt-get update && \
	apt-get install -y \
	build-essential\
	cmake \
	git \
	ipython \
	libatlas3-base libatlas-dev \
	libblas3 libblas-dev \
	libgl1-mesa-dev \
	liblapack3 liblapack-dev \
	python-matplotlib \
	python-numpy \
	python-progressbar \
	python-scipy \
	python-pyfits \
	feh \
	&& rm -rf /var/lib/apt/lists/*

# PyMultiNest install from sources
RUN wget https://raw.githubusercontent.com/ldouchy/docker_PyMultiNest/master/installMultiNest.sh && /bin/bash /opt/installMultiNest.sh

# BXA install from sources
RUN git clone https://github.com/JohannesBuchner/BXA.git && cd /opt/BXA && python setup.py install

# Simple test
WORKDIR /opt/example

COPY reputsimple_pymultinest1d_multimodal_pyinapublicgit.tar.gz /opt/example/
RUN tar -xzvf reputsimple_pymultinest1d_multimodal_pyinapublicgit.tar.gz && rm reputsimple_pymultinest1d_multimodal_pyinapublicgit.tar.gz

CMD python example_simplest.py && feh simplest-marg.png
