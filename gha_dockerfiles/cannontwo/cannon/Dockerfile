FROM ubuntu:bionic AS base

ARG build_graphics=1

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test

RUN apt-get update && apt-get install -y build-essential \ 
        clang-tidy \
        libglfw3-dev \
        libfreetype6 \
        libfreetype6-dev \
        assimp-utils \
        libassimp-dev \
        libboost-all-dev \
        git \
        wget \
        gcovr \
        libompl-dev \
        clang \
        gcc-9 \
        g++-9 \
        libglvnd0 \
        libgl1 \
        libglx0 \
        libegl1 \
        libxext6 \
        libx11-6 \
        libglvnd-dev \
        libgl1-mesa-dev \
        libegl1-mesa-dev \
        pkg-config \
        fonts-open-sans \
        doxygen \
        libhdf5-dev \
        ninja-build \
        libgmp3-dev \ 
        libmpfr-dev

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9

# CMake (we need a newer version)
WORKDIR /
RUN wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-linux-x86_64.sh
RUN chmod +x ./cmake-3.21.1-linux-x86_64.sh
RUN ./cmake-3.21.1-linux-x86_64.sh --skip-license

# Eigen
WORKDIR /
RUN wget https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.gz
RUN tar xzvf eigen-3.4.0.tar.gz
WORKDIR eigen-3.4.0
RUN mkdir build
WORKDIR build
RUN cmake ..
RUN make && make install

# YAML-Cpp
WORKDIR /
RUN wget https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-0.6.0.tar.gz
RUN tar xzvf yaml-cpp-0.6.0.tar.gz
WORKDIR yaml-cpp-yaml-cpp-0.6.0/
RUN mkdir build
WORKDIR build
RUN cmake -DBUILD_SHARED_LIBS=ON -DYAML_CPP_BUILD_TESTS=OFF ..
RUN make && make install
WORKDIR /

# Catch2
RUN git clone https://github.com/catchorg/Catch2.git
WORKDIR /Catch2/
RUN git checkout v2.x
RUN mkdir build
WORKDIR build
RUN cmake -DCATCH_BUILD_TESTING=OFF ..
RUN make && make install
WORKDIR /

# Boost
RUN wget https://boostorg.jfrog.io/artifactory/main/release/1.74.0/source/boost_1_74_0.tar.gz
RUN tar xzvf boost_1_74_0.tar.gz
WORKDIR /boost_1_74_0/
RUN ./bootstrap.sh --prefix=/usr/ --with-libraries=test
RUN ./b2
RUN ./b2 install
WORKDIR /

# OMPL
#WORKDIR /
#RUN wget https://ompl.kavrakilab.org/install-ompl-ubuntu.sh
#RUN chmod u+x install-ompl-ubuntu.sh
#RUN ./install-ompl-ubuntu.sh
#WORKDIR /ompl-1.5.0/
#RUN cmake -DCMAKE_INSTALL_PREFIX=/usr/local/
#RUN make install

# CGAL 
# TODO Download CGAL 5.2, uninstall libcgal-dev, install CGAL 5.2
RUN git clone https://github.com/CGAL/cgal.git
WORKDIR cgal
RUN mkdir build
WORKDIR build
RUN cmake ..
RUN make install
WORKDIR /

COPY . /cannon
RUN mkdir -p /cannon/build
WORKDIR /cannon/build
RUN cmake .. -DCANNON_BUILD_GRAPHICS=OFF -DCANNON_BUILD_DOC=OFF -DCMAKE_BUILD_TYPE=Debug -G "Ninja" -DCMAKE_UNITY_BUILD=yes -DCMAKE_CXX_FLAGS_INIT=-DAPPROVAL_TESTS_DISABLE_FILE_MACRO_CHECK
RUN ninja


# Building with graphics capability
#ENV NVIDIA_VISIBLE_DEVICES all
#ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility
#COPY . /cannon
#RUN mkdir -p /cannon/build
#WORKDIR /cannon/build
#RUN cmake ..
#RUN make -j4

ENTRYPOINT ["ninja", "test"]
