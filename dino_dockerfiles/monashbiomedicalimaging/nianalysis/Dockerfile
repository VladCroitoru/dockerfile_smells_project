FROM ubuntu:bionic
LABEL MAINTAINER "Tom Close <tom.g.close@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y \
	automake \
	build-essential \
	cmake \
	curl \
	g++ \
	g++-4.8 \
	gcc-4.8 \
	gfortran-7 \
	git \
	libbz2-dev \
	libeigen3-dev \
	libexpat1-dev \
	libfftw3-dev \
	libgl1-mesa-dev \
	libqt4-opengl-dev \
	libreadline-dev \
	libtiff5-dev \
	libx11-dev \
	pigz \
	python \
	python-numpy \
	python3 \
	python3-pip \
	tcl \
	tcl-dev \
	unzip \
	vim \
	vtk7 \
	wget \
	xorg \
	zlib1g-dev


RUN mkdir /downloads
RUN mkdir /packages
RUN mkdir /modules

ENV MODULE_VER 4.2.3

ENV AFNI_VER = 19.0.26
ENV ANTS_VER 2.3.1
ENV DCM2NIIX_VER v1.0.20181125
ENV FIX_VER 1.068
ENV FREESURFER_VER 6.0.0
ENV FSL_VER 6.0.1
ENV HCP_WB_VER 1.3.2
ENV MRTRIX_VER 3.0_RC3
ENV R_VER 3.5.3


# Install environment modules
# ---------------------------
ENV MODULE_VER 4.2.3
WORKDIR /downloads
RUN wget http://downloads.sourceforge.net/project/modules/Modules/modules-$MODULE_VER/modules-$MODULE_VER.tar.gz
RUN tar xzf modules-$MODULE_VER.tar.gz
WORKDIR /downloads/modules-$MODULE_VER
RUN ./configure --with-module-path=/modules --prefix=/packages/modules
RUN make
RUN make install
RUN echo '/modules' > /packages/modules/init/.modulespath
RUN cp /downloads/modules-$MODULE_VER/compat/etc/global/profile.modules /etc/profile.d/modules.sh
RUN sed -i 's/Modules//g' /etc/profile.d/modules.sh

# Set modules environment variables
ENV BASH_ENV '/packages/modules/init/bash'
ENV ENV '/packages/modules/init/profile.sh'
ENV LOADEDMODULES ''
ENV MANPATH '/packages/modules/share/man'
ENV MODULEPATH '/modules'
ENV MODULEPATH_modshare '/modules:1'
ENV MODULESHOME '/packages/modules'
ENV MODULES_CMD '/packages/modules/libexec/modulecmd.tcl'
ENV PATH "/packages/modules/bin:$PATH"

# Install Dcm2niix
# ----------------

RUN mkdir /packages/dcm2niix
RUN git clone https://github.com/rordenlab/dcm2niix.git /packages/dcm2niix/src
WORKDIR /packages/dcm2niix/src
RUN git checkout $DCM2NIIX_VER
RUN mkdir /packages/dcm2niix/build
WORKDIR /packages/dcm2niix/build
RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/packages/dcm2niix/$DCM2NIIX_VER ../src
RUN make install
RUN rm -r /packages/dcm2niix/src /packages/dcm2niix/build
 
# Create dcm2niix modulefile
RUN mkdir -p /modules/dcm2niix
RUN printf  "#%%Module1.0\n\
	proc ModulesHelp { } {\n\
	    global dotversion\n\
	    puts stderr \"\tDcm2niix $DCM2NIIX_VER\"\n\
	}\n\
	module-whatis \"Dcm2niix $DCM2NIIX_VER\"\n\
	conflict dcm2niix\n\
	prepend-path PATH /packages/dcm2niix/$DCM2NIIX_VER/bin" >> /modules/dcm2niix/$DCM2NIIX_VER
RUN echo 


# Install MRtrix
# --------------

RUN mkdir /packages/mrtrix
RUN git clone https://github.com/MRtrix3/mrtrix3.git /packages/mrtrix/$MRTRIX_VER
WORKDIR /packages/mrtrix/$MRTRIX_VER
RUN git checkout $MRTRIX_VER
RUN ./configure
RUN ./build

# Create modulefile
RUN mkdir -p /modules/mrtrix
RUN printf "#%Module1.0\n\
    proc ModulesHelp { } {\n\
    global dotversion\n\
        puts stderr "\tMRtrix $MRTRIX_VER"\n\
    }\n\
    module-whatis "MRtrix $MRTRIX_VER"\n\
    conflict mrtrix\n\
    prepend-path PATH /environment/packages/mrtrix/$MRTRIX_VER/bin\n\
    prepend-path PATH /environment/packages/mrtrix/$MRTRIX_VER/scripts\n\
    prepend-path LD_LIBRARY_PATH /environment/packages/mrtrix/$MRTRIX_VER/lib" >> /modules/mrtrix/$MRTRIX_VER

# Install Banana
# ENV BUILT_AT 2019-04-02-16:30
# RUN pip3 install banana
