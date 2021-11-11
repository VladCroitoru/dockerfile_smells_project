
#
# ubuntu 18.04 dressed up for scientific computing
#
FROM ubuntu:18.04
#
ENV DEBIAN_FRONTEND=noninteractive
#
RUN apt update; apt -yq upgrade; \
	apt install -yq \
 		autoconf  \
         	ca-certificates  \
		cmake \
		cython \
		cython3 \
		g++ \
		gawk \
                gfortran-7  \
		git \
		gsl-bin \
		libgsl-dev \
		gnuplot \
 		libblacs-mpi-dev  \
 		libblacs-openmpi1  \
         	libfftw3-3  \
 		libfftw3-bin  \
  		libfftw3-dev  \
  		libfftw3-doc  \
         	libfftw3-double3   \
                libgfortran-7-dev  \
		libgomp1 \
		libmatheval1 \
		libmatheval-dev \
         	libopenblas-base  \
         	libopenblas-dev  \
 		libopenmpi-dev  \
		libxext-dev \
 		make  \
 		net-tools  \
 		openmpi-bin   \
 		openmpi-common \
 		openmpi-doc   \
 		openssh-server  \
		patch \
		python \
                python-backports-shutil-get-terminal-size \
		python-dev \
		python-matplotlib \
		python3-matplotlib \
		python-numpy \
                python3-numpy \
                python3-numpydoc \
		python-os-client-config \
		python-os-service-types \
		python-pip \
		python3-pip \
		python-scipy \
                python3-scipy \
		python-setuptools \
                python3-setuptools \
		python-subprocess32 \
                python3-whichcraft \
 		sudo  \
		vim \
 		wget  \
		xxd \
		xxdiff \
                zlib1g \
		zlib1g-dev \
		--no-install-recommends \
	&& apt autoremove   -y \
	&& rm -rf /var/apt/lists/* \
	&& ssh-keygen -A
#
RUN \
	ln -s /usr/bin/gfortran-7 /usr/bin/f95  \
	&& ln -s /usr/bin/gfortran-7 /usr/bin/gfortran \
	&& ln -s /usr/bin/gfortran-7 /usr/bin/f90

#
CMD /bin/bash




