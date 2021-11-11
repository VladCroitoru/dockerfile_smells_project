FROM yrahal/dev-machine:latest

MAINTAINER Youcef Rahal

USER root

RUN apt-get update --fix-missing

# Install extras to be able read media files
RUN apt-get install -y software-properties-common
RUN add-apt-repository multiverse
#RUN apt-get update # TODO uncomment when VS Code fixes it.
RUN apt-get install -y gstreamer1.0-libav

# Install uWebSockets-0.13.0 and dependencies
RUN apt-get install -y libuv1-dev libssl-dev
RUN wget https://github.com/uWebSockets/uWebSockets/archive/v0.13.0.tar.gz -O uws.tar.gz && \
    echo 'Unpacking...' && tar xfz uws.tar.gz && \
    cd uWebSockets-0.13.0 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    cd ../../ && \
    rm -r uWebSockets-0.13.0 && \
    rm uws.tar.gz && \
    ln -s /usr/lib64/libuWS.so /usr/lib/libuWS.so

# Install cppad and ipopt and dependencies
RUN apt-get install -y cppad gfortran
RUN wget https://www.coin-or.org/download/source/Ipopt/Ipopt-3.12.7.tgz && \
    echo 'Unpacking...' && tar xfz Ipopt-3.12.7.tgz && \
    rm Ipopt-3.12.7.tgz && \
    cd Ipopt-3.12.7 && \
    
    # BLAS
    cd ThirdParty/Blas && \
    ./get.Blas && \
    mkdir -p build && cd build && \
    ../configure --prefix=/usr/local --disable-shared --with-pic && \
    make install && \

    # Lapack
    cd ../../../ThirdParty/Lapack && \
    ./get.Lapack && \
    mkdir -p build && cd build && \
    ../configure --prefix=/usr/local --disable-shared --with-pic --with-blas="/usr/local/lib/libcoinblas.a -lgfortran" && \
    make install && \

    # ASL
    cd ../../../ThirdParty/ASL && \
    ./get.ASL && \

    # MUMPS
    cd ../../ThirdParty/Mumps && \
    ./get.Mumps && \

    # build everything
    cd ../../ && \
    ./configure --prefix=/usr/local coin_skip_warn_cxxflags=yes --with-blas="/usr/local/lib/libcoinblas.a -lgfortran" --with-lapack=/usr/local/lib/libcoinlapack.a && \
    make && \
    make test && \
    make -j1 install && \

    cd .. && \
    rm -r Ipopt-3.12.7

# Clean
RUN apt-get clean && \
    apt-get autoremove && \
    rm -r /var/lib/apt/lists/*

# Rename orion user/group to kitt
RUN usermod -l kitt -m -d /home/kitt orion
RUN groupmod -n kitt orion

# The next commands will be run as the new user
USER kitt

# The port the simulator will be listening on
EXPOSE 4567
