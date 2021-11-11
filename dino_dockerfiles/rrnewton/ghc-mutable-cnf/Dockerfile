FROM fpco/stack-build:lts-5

MAINTAINER Vikraman <git@vikraman.org>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install llvm-3.6

WORKDIR /root

RUN git clone --quiet --recursive git://git.haskell.org/ghc.git

WORKDIR /root/ghc

# ENV SUBMOD_SHA 8c17982648434fae28dedb102ab4624a7323476b
# [2016.05.07] Updating this to the latest arcpatch-D1264:
ENV SUBMOD_SHA af3effe4c591aa4d8ba984a29555d0635143051a

ENV GHC_PREFIX /opt/ghc

# Squish this into one giant command to try to keep the intermediate 
# build data out of the AUFS file system.
RUN git remote add fork https://github.com/iu-parfunc/ghc.git && \
    git fetch fork && \
    git checkout ${SUBMOD_SHA} && \
    git reset --hard && git clean -dfx && \
    git submodule update --init --recursive && \
    mkdir -p ${GHC_PREFIX} && \
    sed -e 's/#BuildFlavour = quick/BuildFlavour = quick/' \
        -e 's/#V=0/V=0/' mk/build.mk.sample > mk/build.mk && \
    ./boot && ./configure --quiet --prefix ${GHC_PREFIX} && \
    make -j2 && make install && \
    rm -rf /root/ghc

ENV PATH ${GHC_PREFIX}/bin:${PATH}
WORKDIR /root
