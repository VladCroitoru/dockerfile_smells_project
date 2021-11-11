# Builds a Docker image for PETSc and SLEPC
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

FROM x11vnc/desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

ENV OPENMPI_VERSION=2.1.1
ENV PETSC_VERSION=3.7.7
ENV SLEPC_VERSION=3.7.4


# Install system packages and compile OpenMPI2 for InfiniBand support
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        gcc \
        gfortran \
        bison \
        flex \
        git \
        bash-completion \
        bsdtar \
        rsync \
        wget \
        gdb \
        ccache \
        \
        libopenblas-base \
        libopenblas-dev \
        \
        openmpi-bin libopenmpi2 libopenmpi-dev \
        libscalapack-openmpi2.0 \
        libsuperlu-dev \
        libsuitesparse-dev \
        libhypre-dev \
        libptscotch-dev \
        libmumps-dev \
        \
        libpetsc${PETSC_VERSION}-dev \
        libslepc${SLEPC_VERSION}-dev && \
    apt-get clean && \
    apt-get autoremove && \
    \
    curl https://download.open-mpi.org/release/open-mpi/v2.1/openmpi-$OPENMPI_VERSION.tar.bz2 | tar xjvf - && \
    cd openmpi-$OPENMPI_VERSION && \
    ./configure --prefix=/opt/openmpi/${OPENMPI_VERSION} --enable-orterun-prefix-by-default --enable-mpirun-prefix-by-default --enable-static --enable-shared --with-verbs && \
    make -j2 && make install && \
    \
    cd /tmp && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PETSC_DIR=/usr/lib/petscdir/${PETSC_VERSION}/x86_64-linux-gnu-real
ENV SLEPC_DIR=/usr/lib/slepcdir/${SLEPC_VERSION}/x86_64-linux-gnu-real

# Config OpenMPI
ENV MPI_HOME=/opt/openmpi/${OPENMPI_VERSION}
ENV OMP_STACKSIZE=16M
ENV MPI_BUFFER_SIZE=20000000
ENV HWLOC_HIDE_ERRORS=1

########################################################
# Customization for user
########################################################
RUN echo "export OMP_NUM_THREADS=\$(nproc)" >> $DOCKER_HOME/.profile && \
    echo "export PATH=\$MPI_HOME/bin:\$PATH" && \
    chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME

WORKDIR $DOCKER_HOME
