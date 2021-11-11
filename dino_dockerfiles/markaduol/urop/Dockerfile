# escape=\ (backslash)

FROM ubuntu:14.04

ENV LLVM_VERSION=3.4 \
    KLEE_BUILD_DIR=/klee/build \
    KLEE_UCLIBC_SOURCE_DIR=/klee-uclibc \
    HOME=/home/urop \
    DISPLAY=:0

# We use layered RUN instructions in order frequently commit the container state during a build.

# Install LLVM toolchain
RUN set -xe && \
  apt-get update && \
  apt-get -y install \
    clang-${LLVM_VERSION} \
    llvm-${LLVM_VERSION} \
    llvm-${LLVM_VERSION}-dev \
    llvm-${LLVM_VERSION}-runtime

# Install klee dependencies and other required and useful packages
RUN set -xe && \
  apt-get update && \
  apt-get install -y \
    build-essential \
    curl \
    libcap-dev \
    git \
    cmake \
    libncurses5-dev \
    python-minimal \
    python-pip \
    unzip \
    zlib1g-dev \
    flex \
    bison \
    python3-tk \
    python3-pip \
    pkg-config \
    libfreetype6-dev \
    vim

# Install minisat
RUN set -xe && \
  git clone https://github.com/stp/minisat.git && \
  mkdir -p minisat/build && \
  cd minisat/build && \
  cmake -DSTATIC_BINARIES=ON -DCMAKE_INSTALL_PREFIX=/usr/local ../ && \
  make && \
  sudo make install

# Install stp
RUN set -xe && \
  git clone https://github.com/stp/stp.git && \
  cd stp && \
  git checkout tags/2.1.2 && \
  mkdir build && \
  cd build && \
  cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DENABLE_PYTHON_INTERFACE:BOOL=OFF ../ && \
  make && \
  sudo make install && \
  cd ../ && \
  ulimit -s unlimited && \
  cd ../ 

# Create symbolic links
RUN set -xe && \
  ln -s /usr/bin/llvm-config-${LLVM_VERSION} /usr/bin/llvm-config

# Install klee and klee-uclibc
RUN set -xe && \
  git clone https://github.com/klee/klee-uclibc.git && \
  cd klee-uclibc && \
  ./configure --make-llvm-lib && \
  make -j2 && \
  cd .. && \
  git clone https://github.com/klee/klee.git && \
  cd klee && \
  mkdir build && \
  cd build && \
  cmake -DENABLE_SOLVER_STP=ON \
    -DLLVM_CONFIG_BINARY=/usr/bin/llvm-config-${LLVM_VERSION} \
    -DENABLE_UNIT_TESTS=OFF \ 
    -DENABLE_POSIX_RUNTIME=ON \
    -DENABLE_KLEE_UCLIBC=ON \
    -DKLEE_UCLIBC_PATH=${KLEE_UCLIBC_SOURCE_DIR} \
    -DENABLE_SYSTEM_TESTS=OFF ../ && \
  make

# Add relevant files
RUN set -xe && \
  mkdir -p ${HOME}/UROP

COPY / ${HOME}/UROP

# Add KLEE binary directory to path
RUN set -xe && \
  touch ${HOME}/.bashrc && \
  (echo 'export PATH=$PATH:'${KLEE_BUILD_DIR}'/bin' >> ${HOME}/.bashrc) && \
  export LLVM_COMPILER=clang

# Create symbolic links
USER root
RUN set -xe && \
  (for executable in ${KLEE_BUILD_DIR}/bin/* ; do ln -s ${executable} /usr/bin/`basename ${executable}`; done)

# Install wllvm
RUN set -xe && \
  pip install wllvm && \
  pip3 install GitPython && \
  pip3 install numpy && \
  pip3 install matplotlib

# Set workdir
WORKDIR ${HOME}
