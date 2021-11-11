# Docker image for interface mapper using DataTransferKit
# for multiphysics coupling.
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

# Use meshdb-desktop as base image
FROM unifem/meshdb-desktop
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

ARG TRILINOS_VERSION=12-12-1
ARG DTK_VERSION=2.0

# Build DataTransferKit
# For options to control Trilinos, see
# https://trilinos.org/oldsite/TrilinosBuildQuickRef.html#configuring-makefile-generator
RUN cd /tmp && \
    git clone --depth 1 --branch trilinos-release-${TRILINOS_VERSION} \
        https://github.com/trilinos/Trilinos.git && \
    cd Trilinos && \
    git clone --depth 1 --branch dtk-${DTK_VERSION} \
        https://github.com/unifem/DataTransferKit.git && \
    mkdir build && cd build && \
    cmake \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr/local \
        -DCMAKE_BUILD_TYPE:STRING=RELEASE \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
        -DCMAKE_SHARED_LIBS:BOOL=ON \
        -DTPL_ENABLE_MPI:BOOL=ON \
        -DTPL_ENABLE_Boost:BOOL=ON \
        -DBoost_INCLUDE_DIRS:PATH=/usr/include/boost \
        -DTPL_ENABLE_Libmesh:BOOL=OFF \
        -DTPL_ENABLE_MOAB:BOOL=ON \
        -DMOAB_INCLUDE_DIRS=/usr/local/include \
        -DMOAB_LIBRARY_DIRS=/usr/local/lib \
        -DTPL_ENABLE_Netcdf:BOOL=ON \
        -DTPL_ENABLE_BinUtils:BOOL=OFF \
        -DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=OFF \
        -DTrilinos_ENABLE_ALL_PACKAGES=OFF \
        -DTrilinos_EXTRA_REPOSITORIES="DataTransferKit" \
        -DTrilinos_ENABLE_EXPLICIT_INSTANTIATION:BOOL=ON \
        -DTrilinos_ASSERT_MISSING_PACKAGES:BOOL=OFF \
        -DTrilinos_ENABLE_TESTS:BOOL=OFF \
        -DTrilinos_ENABLE_EXAMPLES:BOOL=OFF \
        -DTrilinos_ENABLE_CXX11:BOOL=ON \
        -DTrilinos_ENABLE_Tpetra:BOOL=ON \
        -DTpetra_INST_INT_UNSIGNED_LONG:BOOL=ON \
        -DTPL_ENABLE_BLAS:BOOL=ON \
        -DTPL_BLAS_LIBRARIES=/usr/lib/x86_64-linux-gnu/libopenblas.so \
        -DTPL_ENABLE_LAPACK:BOOL=ON \
        -DTPL_LAPACK_LIBRARIES=/usr/lib/x86_64-linux-gnu/libopenblas.so \
        -DTPL_ENABLE_Eigen:BOOL=ON \
        -DTPL_Eigen_INCLUDE_DIRS=/usr/include/eigen3 \
        -DTrilinos_ENABLE_DataTransferKit=ON \
        -DDataTransferKit_ENABLE_DBC=ON \
        -DDataTransferKit_ENABLE_TESTS=ON \
        -DDataTransferKit_ENABLE_EXAMPLES=OFF \
        -DDataTransferKit_ENABLE_ClangFormat=OFF \
        -DTPL_ENABLE_BoostLib:BOOL=OFF \
        -DBUILD_SHARED_LIBS:BOOL=ON \
        .. && \
    make -j2 && \
    make install && \
    \
    rm -rf /tmp/Trilinos

ADD image/bin /usr/local/bin
ADD image/home $DOCKER_HOME

WORKDIR $DOCKER_HOME
USER root
