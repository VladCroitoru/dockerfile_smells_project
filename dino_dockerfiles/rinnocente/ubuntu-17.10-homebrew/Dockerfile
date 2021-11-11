#
# ubuntu 17.10 dressed up for scientific computing
#
FROM ubuntu:17.10
#
LABEL 	maintainer="Roberto Innocente <inno@sissa.it>" \
	version="1.0"
#
ARG DEBIAN_FRONTEND=noninteractive
#
RUN apt update; apt -yq upgrade; \
	apt install -yq vim \
		git \
		cmake \
 		openssh-server  \
 		sudo  \
 		wget  \
         	ca-certificates  \
		g++ \
		gnuplot \
		xxdiff \
		gawk \
         	libopenblas-base  \
         	libopenblas-dev  \
 		openmpi-bin   \
         	libfftw3-3  \
 		libfftw3-bin  \
  		libfftw3-dev  \
         	libfftw3-double3   \
 		libblacs-openmpi1  \
 		libblacs-mpi-dev  \
		libmatheval1 \
		libmatheval-dev \
		libxext-dev \
 		net-tools  \
 		make  \
 		autoconf  \
 		libopenmpi-dev  \
                libgfortran-6-dev  \
                gfortran-6  \
		python \
                python3-numpy \
                python3-scipy \
                zlib1g zlib1g-dev \
		--no-install-recommends \
	&& apt autoremove   -y \
	&& rm -rf /var/apt/lists/* \
	&& ssh-keygen -A
#
RUN \
	ln -s /usr/bin/gfortran-6 /usr/bin/f95  \
	&& ln -s /usr/bin/gfortran-6 /usr/bin/gfortran \
	&& ln -s /usr/bin/gfortran-6 /usr/bin/f90
#
CMD /bin/bash

