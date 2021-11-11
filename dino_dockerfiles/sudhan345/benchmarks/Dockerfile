FROM debian:6.0.10
MAINTAINER Sudhanshu Shukla <sudhan345@gmail.com>

## Set non interactive frontend
ENV DEBIAN_FRONTEND noninteractive

## Install build packages
RUN apt-get update && apt-get install -y \
        make \
        autoconf \
        gcc-multilib \
        g++-multilib \
        pkg-config \
        gettext \
        ia32-libs-dev \
        libx11-dev \
        libxext-dev \
        libxt-dev \
        libxmu-dev \
        libxi-dev \
        git

## Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

## Backup original uname
RUN mv /bin/uname /bin/uname.orig
RUN ln -sf /bin/uname.orig /bin/uname

# Add sumulation user and benchmarks
RUN useradd -m sim
USER sim
RUN git clone https://github.com/sudhan345/benchmarks.git /home/sim/benchmarks

## Add uname parsec wrapper
USER root
ADD uname.parsec /bin/uname.parsec
RUN chmod +x /bin/uname.parsec
RUN ln -sf /bin/uname.parsec /bin/uname

## Prepare for building PARSEC and SPLASH2X benchmarks 
USER sim
ENV HOSTTYPE i386
WORKDIR /home/sim/benchmarks/parsec-3.0/

## Build PARSEC benchmarks 
RUN ./bin/parsecmgmt -a build -p parsec.blackscholes
RUN ./bin/parsecmgmt -a build -p parsec.bodytrack
RUN ./bin/parsecmgmt -a build -p parsec.canneal
RUN ./bin/parsecmgmt -a build -p parsec.dedup
RUN ./bin/parsecmgmt -a build -p parsec.facesim
RUN ./bin/parsecmgmt -a build -p parsec.ferret
RUN ./bin/parsecmgmt -a build -p parsec.fluidanimate
RUN ./bin/parsecmgmt -a build -p parsec.freqmine
RUN ./bin/parsecmgmt -a build -p parsec.raytrace
RUN ./bin/parsecmgmt -a build -p parsec.streamcluster
RUN ./bin/parsecmgmt -a build -p parsec.swaptions
RUN ./bin/parsecmgmt -a build -p parsec.vips
RUN ./bin/parsecmgmt -a build -p parsec.x264

## Build SPLASH2X benchmarks 
RUN ./bin/parsecmgmt -a build -p splash2x.barnes
RUN ./bin/parsecmgmt -a build -p splash2x.cholesky
RUN ./bin/parsecmgmt -a build -p splash2x.fft
RUN ./bin/parsecmgmt -a build -p splash2x.fmm
RUN ./bin/parsecmgmt -a build -p splash2x.lu_cb
RUN ./bin/parsecmgmt -a build -p splash2x.lu_ncb
RUN ./bin/parsecmgmt -a build -p splash2x.ocean_cp
RUN ./bin/parsecmgmt -a build -p splash2x.radiosity
RUN ./bin/parsecmgmt -a build -p splash2x.radix
RUN ./bin/parsecmgmt -a build -p splash2x.raytrace
RUN ./bin/parsecmgmt -a build -p splash2x.water_nsquared
RUN ./bin/parsecmgmt -a build -p splash2x.water_spatial

# Clean build directory
RUN ./bin/parsecmgmt -a fullclean -p all

# Print status of PARSEC and SPLASH2x applications
RUN ./bin/parsecmgmt -a status -p parsec
RUN ./bin/parsecmgmt -a status -p splash2x

## Change uname back to original
USER root
RUN ln -sf /bin/uname.orig /bin/uname

