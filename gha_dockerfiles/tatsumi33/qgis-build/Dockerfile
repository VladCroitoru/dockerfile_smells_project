# Working container for QGIS/GDAL/PROJ.
# Building QGIS binary in a container from the source code of specific version,
# tag, or branch.
#
# Build container image:
#
# ```
# $ docker build -t qgis-build .
# ```
#
# Run QGIS in the container with X11/GUI.
#
# ```
# $ xhost local:
# $ docker run -it --rm --privileged \
#       -e DISPLAY=${DISPLAY} \
#       -e LD_LIBRARY_PATH=/usr/local/lib \
#       -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
#       -v "$HOME/gis-data-folder:/root/data:ro" \
#       qgis-build bash
# > qgis
# ```

FROM ubuntu:21.04

ARG PARALLEL=8

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y \
# && apt-get install --no-install-recommends -y \
 && apt-get install -y \
    git \
    ca-certificates \
    curl \
    autoconf \
    pkg-config \
    libtool \
    make \
    cmake \
    clang \
    sqlite3 \
    libsqlite3-dev \
    libtiff-dev \
    libcurl4-gnutls-dev \
    flex \
    bison \
    libzip-dev \
    protobuf-compiler \
    libexiv2-dev \
    libzstd-dev \
    qtbase5-dev \
    qt3d5-dev \
    libqt5serialport5-dev \
    libqt5svg5-dev \
    qttools5-dev \
    libqt5webkit5-dev \
    qtpositioning5-dev \
    libqca-qt5-2-dev \
    libgsl-dev \
    libpython3.9-dev \
    pyqt5-dev \
    pyqt5.qsci-dev \
    python3-pyqt5 \
    python3-pyqt5.qsci \
    python3-pyqt5.qtsql \
    python3-pyqt5.qtwebkit \
    python3-sip \
    python3-pip \
    python3-psycopg2 \
    python3-numpy \
    pyqt5-dev-tools \
    libspatialindex-dev \
    libqscintilla2-qt5-dev \
    libqwt-qt5-dev \
    qt5keychain-dev \
    libminizip-dev \
    libfreexl-dev \
    libxml2-dev \
    sip-dev \
    libpq-dev \
    fonts-noto-cjk \
 && apt-get clean

WORKDIR /root

# PROJ
#ARG PROJ_VER=8.1.1
#RUN curl -SL https://github.com/OSGeo/PROJ/archive/refs/tags/${PROJ_VER}.tar.gz | tar xz \
# && cd PROJ-${PROJ_VER} \
RUN git clone https://github.com/OSGeo/PROJ && cd PROJ \
 && mkdir build && cd build \
 && cmake .. \
      -D CMAKE_C_COMPILER=/usr/bin/clang \
      -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
 && make -j ${PARALLEL} && make install

# GEOS
#ARG GEOS_VER=3.8.2
#RUN curl -SL https://git.osgeo.org/gitea/geos/geos/archive/${GEOS_VER}.tar.gz | tar xz \
RUN git clone https://git.osgeo.org/gitea/geos/geos.git \
 && cd geos \
 && mkdir build && cd build \
 && cmake .. \
      -D CMAKE_C_COMPILER=/usr/bin/clang \
      -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
 && make -j ${PARALLEL} && make install

# GDAL
#ARG GDAL_VER=3.3.2
#RUN curl -SL https://github.com/OSGeo/gdal/archive/refs/tags/v${GDAL_VER}.tar.gz | tar xz \
# && cd gdal-${GDAL_VER}/gdal \
RUN git clone https://github.com/OSGeo/gdal && cd gdal/gdal \
 && ./autogen.sh \
 && CC=clang CXX=clang++ ./configure \
        --with-python=yes \
 && make -j ${PARALLEL} && make install \
 && cd swig/python && python3 setup.py build && python3 setup.py install

# RT Topology Library
ARG RTTOPO_VER=1.1.0
RUN curl -SL https://git.osgeo.org/gitea/rttopo/librttopo/archive/librttopo-${RTTOPO_VER}.tar.gz | tar xz \
 && cd librttopo \
 && CC=clang CXX=clang++ ./autogen.sh \
 && ./configure \
 && make -j ${PARALLEL} && make install

# SpatiaLite
ARG SPATIALITE_VER=5.0.1
#RUN curl -SL http://www.gaia-gis.it/gaia-sins/libspatialite-${SPATIALITE_VER}.tar.gz | tar xz \
RUN curl -SL http://ftp.iij.ad.jp/pub/linux/gentoo/distfiles/c7/libspatialite-${SPATIALITE_VER}.tar.gz | tar xz \
 && cd libspatialite-${SPATIALITE_VER} \
 && CC=clang CXX=clang++ ./configure \
 && make -j ${PARALLEL} && make install

# OWSLib
RUN git clone https://github.com/geopython/OWSLib.git \
 && cd OWSLib \
 && python3 setup.py build && python3 setup.py install

# QGIS
ARG QGIS_VER=3_20_3
RUN curl -SL https://github.com/qgis/QGIS/archive/refs/tags/final-${QGIS_VER}.tar.gz | tar xz \
 && cd QGIS-final-${QGIS_VER} \
 && mkdir build && cd build \
 && cmake .. \
      -D CMAKE_C_COMPILER=/usr/bin/clang \
      -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
      -D WITH_3D=true \
 && LD_LIBRARY_PATH=/usr/local/lib make -j ${PARALLEL} \
 && LD_LIBRARY_PATH=/usr/local/lib make install

# Python libraries
RUN pip install ninja2
