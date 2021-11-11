FROM ubuntu:20.04 AS dep-base
LABEL maintainer="wan@qoherent.ai"

ARG DEBIAN_FRONTEND

ENV DEBIAN_FRONTEND=${DEBIAN_FRONTEND:-noninteractive}

RUN apt-get -qy update && apt-get -qy upgrade

# common depedencies
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    software-properties-common \
    git \
    cmake \
    g++ \
    ccache \
    build-essential \
    swig \
    curl \
    doxygen \
    nano \
    && echo "Installed common build dependencies" \
    && rm -rf /var/lib/apt/lists/*

FROM dep-base AS dep-libiiopkg
# install libiio as packages
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    libiio-dev  \
    libiio-utils  \
    libad9361-dev \
    python3-libiio \
    && echo "Installed Libiio packages" \
    && rm -rf /var/lib/apt/lists/*

FROM dep-base AS dep-uhdpkg
# install uhd as packages
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    libuhd-dev \
    uhd-host  \
    python3-uhd \
    && echo "Installed UHD Packages" \
    && rm -rf /var/lib/apt/lists/*

FROM dep-base AS dep-soapypkg
# install soapy as packages
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    libsoapysdr-dev \
    uhd-soapysdr \
    soapysdr-tools  \
    soapysdr-module-uhd \
    soapysdr-module-osmosdr \
    python3-soapysdr \
    && echo "Installed Soapy packages" \
    && rm -rf /var/lib/apt/lists/*

FROM dep-base AS dep-libiio
# libiio dependencies
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    libxml2 \
    libxml2-dev \
    bison \
    flex \
    libaio-dev \
    libboost-all-dev \
    libusb-1.0-0-dev \
    libavahi-common-dev \
    libavahi-client-dev \
    && echo "Installed Libiio build dependencies" \
    && rm -rf /var/lib/apt/lists/*

#FROM dep-base AS dep-uhd
## uhd dependencies

FROM dep-libiio AS dep-oscilloscope
# iio-oscilloscope dependencies
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    libglib2.0-dev  \
    libgtk2.0-dev  \
    libgtkdatabox-dev  \
    libmatio-dev  \
    libfftw3-dev  \
    libcurl4-openssl-dev  \
    libjansson-dev  \
    libserialport-dev \
    && echo "Installed IIO Oscilloscope build dependencies" \
    && rm -rf /var/lib/apt/lists/*

FROM dep-oscilloscope AS dep-gnuradio
# GNU Radio 3.8 dependences
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    gir1.2-gtk-3.0 \
    libasound2 \
    libboost-all-dev \
    libgmp-dev \
    libfftw3-dev \
    libsdl1.2-dev  \
    libgsl-dev  \
    libqwt-qt5-dev  \
    libqt5opengl5-dev  \
    liblog4cpp5-dev  \
    libzmq3-dev  \
    libcodec2-dev  \
    libgsm1-dev \
    python3-pyqt5 \
    python3-numpy \
    python3-mako  \
    python3-sphinx  \
    python3-lxml  \
    python3-yaml  \
    python3-click  \
    python3-click-plugins \
    python3-zmq  \
    python3-scipy  \
    python3-gi  \
    python3-gi-cairo  \
    && echo "Installed GNU Radio 3.8 build dependencies" \
    && rm -rf /var/lib/apt/lists/*

# GNU Radio 3.9 dependences
RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    pybind11-dev  \
    python3-matplotlib  \
    libsndfile1-dev \
    && echo "Installed GNU Radio 3.9-specific build dependencies" \
    && rm -rf /var/lib/apt/lists/*

FROM dep-gnuradio AS build-base
ARG PREFIX
ARG MAKEWIDTH

ENV PREFIX=${PREFIX:-/opt}
ENV MAKEWIDTH=${MAKEWIDTH:-4}
RUN echo "\n\
export PATH=$PREFIX/bin:\$PATH\n\
export LD_LOAD_LIBRARY=$PREFIX/lib:\$LD_LOAD_LIBRARY\n\
export LD_LIBRARY_PATH=$PREFIX/lib:\$LD_LIBRARY_PATH\n\
export PYTHONPATH=$PREFIX/lib/python3.8/site-packages:\$PYTHONPATH\n\
export PYTHONPATH=$PREFIX/lib/python3/dist-packages:\$PYTHONPATH\n\
export PKG_CONFIG_PATH=$PREFIX/lib/pkgconfig:\$PKG_CONFIG_PATH\n" >> ~/.bashrc

FROM build-base AS build-libiio

ARG LIBIIO_VER=master

WORKDIR /src

RUN mkdir -p build &&\
    git clone https://github.com/analogdevicesinc/libiio.git && \
    cd libiio && \
    git checkout $LIBIIO_VER &&\
    cd /src/build && \
    cmake -DCMAKE_INSTALL_PREFIX=$PREFIX ../libiio/ && \
    make -j $MAKEWIDTH && \
    make install \
    && echo "Installed libiio:$LIBIIO_VER source build"

FROM build-base AS build-libad9361-iio

ARG LIBAD9361_VER=master

COPY --from=build-libiio /$PREFIX /$PREFIX

WORKDIR /src

RUN mkdir -p build &&\
    git clone https://github.com/analogdevicesinc/libad9361-iio.git && \
    cd libad9361-iio && \
    git checkout $LIBAD9361_VER &&\
    cd /src/build && \
    cmake -DCMAKE_INSTALL_PREFIX=$PREFIX ../libad9361-iio/ && \
    make -j $MAKEWIDTH && \
    make install \
    && echo "Installed libad9361-iio:$LIBAD9361_VER source build"

FROM build-base AS build-oscilloscope

ARG IIO_OSCILLOSCOPE_VER=master

COPY --from=build-libiio /$PREFIX /$PREFIX
COPY --from=build-libad9361-iio /$PREFIX /$PREFIX

WORKDIR /src

RUN mkdir -p build &&\
    git clone https://github.com/analogdevicesinc/iio-oscilloscope.git && \
    cd iio-oscilloscope && \
    git checkout $IIO_OSCILLOSCOPE_VER &&\
    cd /src/build && \
    cmake -DCMAKE_INSTALL_PREFIX=$PREFIX ../iio-oscilloscope/ && \
    make -j $MAKEWIDTH && \
    make install \
    && echo "Installed iio-oscilloscope:$IIO_OSCILLOSCOPE_VER source build"

FROM build-base AS build-volk

ARG VOLK_VER=main

WORKDIR /src

RUN mkdir -p build &&\
    git clone --recursive https://github.com/gnuradio/volk.git && \
    cd volk && \
    git checkout $VOLK_VER &&\
    cd /src/build && \
    cmake -DCMAKE_INSTALL_PREFIX=$PREFIX ../volk/ && \
    make -j $MAKEWIDTH && \
    make install && \
    ldconfig \
    && echo "Installed volk:$VOLK_VER source build"

FROM build-base AS build-gnuradio

ARG GNURADIO_VER=master

COPY --from=build-libiio /$PREFIX /$PREFIX
COPY --from=build-libad9361-iio /$PREFIX /$PREFIX
COPY --from=build-volk /$PREFIX /$PREFIX

WORKDIR /src

RUN mkdir -p build &&\
    git clone https://github.com/gnuradio/gnuradio.git && \
    cd gnuradio && \
    git checkout $GNURADIO_VER &&\
    cd /src/build && \
    cmake -DCMAKE_INSTALL_PREFIX=$PREFIX ../gnuradio/ && \
    make -j $MAKEWIDTH && \
    make install &&\
    ldconfig \
    && echo "Installed gnuradio:$GNURADIO_VER source build"


FROM build-base AS final

COPY --from=build-libiio /$PREFIX /$PREFIX
COPY --from=build-libad9361-iio /$PREFIX /$PREFIX
COPY --from=build-volk /$PREFIX /$PREFIX
COPY --from=build-gnuradio /$PREFIX /$PREFIX
