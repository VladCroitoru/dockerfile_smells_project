FROM nimbix/base-ubuntu-nvidia:8.0-cudnn5-devel
MAINTAINER Nimbix, Inc. <support@nimbix.net>

WORKDIR /usr/local/src

RUN apt-get update && apt-get -y install gfortran fort77 build-essential curl libibverbs-dev libibverbs1 libibcm1 librdmacm1 librdmacm-dev rdmacm-utils libibmad-dev libibmad5 byacc libibumad-dev libibumad3 infiniband-diags libmlx5-1 libmlx5-dev perftest ibverbs-utils opensm flex alien && apt-get clean
RUN curl http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-2.2.tar.gz |tar xzf - && cd mvapich2-2.2 && ./configure --without-cma --enable-threads=multiple MV2_USE_CUDA=1 RSH_CMD=/usr/bin/ssh SSH_CMD=/usr/bin/ssh && make -j2 && make install && cd .. && rm -rf mvapich2-2.2

# install mvapich2-gdr (for CUDA 8.0)
WORKDIR /tmp
RUN curl -O http://mvapich.cse.ohio-state.edu/download/mvapich/gdr/2.2/mofed-3.2/mvapich2-gdr-cuda8.0-gnu-2.2-2.el7.centos.x86_64.rpm && alien -c *.rpm && dpkg --install *.deb && rm -f *.rpm *.deb


