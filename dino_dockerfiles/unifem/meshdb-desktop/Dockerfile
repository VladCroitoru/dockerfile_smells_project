# Builds a Docker image with Ubuntu 17.10, Python 3, Jupyter Notebook,
# CGNS/pyCGNS and MOAB/pyMOAB with parallel suppport for multiphysics coupling
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

# Use fenics-desktop as base image
FROM unifem/fenics-desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        automake autogen autoconf libtool \
        libhdf5-100 \
        libhdf5-dev \
        libhdf5-openmpi-100 \
        libhdf5-openmpi-dev \
        hdf5-tools \
        libnetcdf13 libnetcdf-dev \
        libmetis5 libmetis-dev \
        \
        tk-dev \
        libglu1-mesa-dev \
        libxmu-dev && \
    apt-get clean && \
    \
    pip3 install -U \
        cython \
        nose && \
    \
    mkdir -p /usr/lib/hdf5-openmpi && \
    ln -s -f /usr/include/hdf5/openmpi /usr/lib/hdf5-openmpi/include && \
    ln -s -f /usr/lib/x86_64-linux-gnu/hdf5/openmpi /usr/lib/hdf5-openmpi/lib && \
    \
    mkdir -p /usr/lib/hdf5-serial && \
    ln -s -f /usr/include/hdf5/serial /usr/lib/hdf5-serial/include && \
    ln -s -f /usr/lib/x86_64-linux-gnu/hdf5/serial /usr/lib/hdf5-serial/lib && \
    \
    rm -rf /var/lib/apt/lists/* /tmp/*

# Install CGNS from source with parallel enabled
RUN cd /tmp && \
    git clone --depth=1 -b master https://github.com/CGNS/CGNS.git && \
    cd CGNS/src && \
    export CC="mpicc" && \
    export LIBS="-Wl,--no-as-needed -ldl -lz -lsz -lpthread" && \
    ./configure --enable-64bit --with-zlib --with-hdf5=/usr/lib/hdf5-openmpi \
        --enable-parallel --enable-cgnstools --enable-lfs --enable-shared && \
    sed -i 's/TKINCS =/TKINCS = -I\/usr\/include\/tcl/' cgnstools/make.defs && \
    make -j2 && make install && \
    rm -rf /tmp/CGNS

# Install pyCGNS from source
RUN cd /tmp && \
    git clone --depth=1 -b master https://github.com/unifem/pyCGNS.git && \
    cd pyCGNS && \
    python3 setup.py build \
        --includes=/usr/include/hdf5/openmpi:/usr/include/openmpi \
        --libraries=/usr/lib/x86_64-linux-gnu/hdf5/openmpi && \
    python3 setup.py install && \
    rm -rf /tmp/pyCGNS

# Install MOAB and pymoab from sources
RUN cd /tmp && \
    git clone --depth=1 https://bitbucket.org/fathomteam/moab.git && \
    cd moab && \
    autoreconf -fi && \
    ./configure \
        --prefix=/usr/local \
        --with-mpi \
        CC=mpicc \
        CXX=mpicxx \
        FC=mpif90 \
        F77=mpif77 \
        --enable-optimize \
        --enable-shared=yes \
        --with-blas=-lopenblas \
        --with-lapack=-lopenblas \
        --with-scotch=/usr/lib/x86_64-linux-gnu \
        --with-metis=/usr/lib/x86_64-linux-gnu \
        --with-eigen3=/usr/include/eigen3 \
        --with-x \
        --with-cgns \
        --with-hdf5=/usr/lib/hdf5-openmpi \
        --with-hdf5-ldflags="-L/usr/lib/hdf5-openmpi/lib" \
        --enable-ahf=yes \
        --enable-tools=yes && \
    make -j2 && make install && \
    \
    cd pymoab && \
    python3 setup.py install && \
    rm -rf /tmp/moab

ADD image/home $DOCKER_HOME

########################################################
# Customization for user
########################################################

USER $DOCKER_USER
WORKDIR $DOCKER_HOME
USER root
