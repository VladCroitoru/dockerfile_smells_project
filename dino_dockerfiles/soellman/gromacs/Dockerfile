FROM debian:jessie
MAINTAINER Oliver Soell <oliver@soell.net>

# this makes it crazy big.
#RUN apt-get update -y &&\
#    apt-get install kmod &&\
#    mkdir /tmp/cuda &&\
#    cd /tmp/cuda &&\
#    curl -O http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_linux.run &&\
#    chmod +x cuda_*_linux.run &&\
#    ./cuda_*_linux.run -extract=$(pwd) &&\
#    ./NVIDIA-Linux-x86_64-*.run -s --no-kernel-module &&\
#    ./cuda-linux64-rel-*.run -noprompt &&\
#    rm -rf /tmp/cuda

#ENV PATH=/usr/local/cuda/bin:$PATH \
#  LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

ENV GROMACS_VERSION 5.1.2

RUN apt-get update -y &&\
    apt-get install -y build-essential curl cmake libxml2-dev &&\
    curl -sL ftp://ftp.gromacs.org/pub/gromacs/gromacs-${GROMACS_VERSION}.tar.gz | tar zxfv - -C /var/tmp &&\
    
    for type in sse2 sse4.1 avx_128_fma avx_256 avx2_256 ; do \
      mkdir /var/tmp/build-${type} &&\
      cd /var/tmp/build-${type} &&\
      cmake /var/tmp/gromacs-${GROMACS_VERSION} -DCMAKE_INSTALL_PREFIX=/opt/gromacs/${type} \
        -DGMX_SIMD=${type} \
        -DGMX_USE_RDTSCP=OFF \
        -DGMX_BUILD_OWN_FFTW=ON &&\
      make -j4 &&\
      make install &&\
      rm -rf /var/tmp/build-${type} ;\
    done &&\
    
    rm -rf /var/tmp/gromacs-${GROMACS_VERSION} &&\
    apt-get remove -y build-essential curl cmake && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists

RUN ln -s /opt/gromacs/sse2 /opt/gromacs/default

VOLUME /opt/gromacs

