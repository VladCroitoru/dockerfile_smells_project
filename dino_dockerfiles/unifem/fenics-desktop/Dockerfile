# Builds a Docker image for FEniCS for Python3
# based on spyder-desktop
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

# Use PETSc prebuilt in compdatasci/petsc-desktop
FROM compdatasci/spyder-desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install system packages
RUN add-apt-repository ppa:fenics-packages/fenics && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        git-lfs \
        libnss3 \
        imagemagick \
        \
        python3-petsc4py \
        python3-slepc4py \
        python3-pybind11 \
        pybind11-dev \
        libboost-filesystem-dev \
        libboost-iostreams-dev \
        libboost-math-dev \
        libboost-program-options-dev \
        libboost-system-dev \
        libboost-thread-dev \
        libboost-timer-dev \
        libeigen3-dev \
        libomp-dev \
        libpcre3-dev \
        libhdf5-openmpi-dev \
        libgmp-dev \
        libcln-dev \
        libmpfr-dev \
        libparmetis4.0 libmetis-dev libparmetis-dev \
        fenics && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

ADD image/home $DOCKER_HOME

########################################################
# Customization for user
########################################################

USER $DOCKER_USER
ENV GIT_EDITOR=vi EDITOR=vi
RUN echo 'export OMP_NUM_THREADS=$(nproc)' >> $DOCKER_HOME/.profile && \
    echo "PATH=$DOCKER_HOME/bin:$PATH" >> $DOCKER_HOME/.profile

WORKDIR $DOCKER_HOME
USER root
