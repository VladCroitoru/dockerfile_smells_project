FROM ubuntu:16.04
MAINTAINER nyuge <aiben.mail1@gmail.com>

#
# environments settings
#
ARG DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH" \
    LANG=C.UTF-8 \
    PYTHON_MAJOR=3.5 \
    PYTHON_VERSION=3.5.5 \
    PYTHON_PIP_VERSION=9.0.1 \
    RDKIT_RELEASE_VERSION=2017_09_3

#
# install libraries with apt 
#
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        bzip2 \
        ca-certificates \
        cmake \
        curl \
        gfortran \
        gzip \
	libboost-dev \
	libboost-system-dev \
	libboost-thread-dev \
	libboost-serialization-dev \
	libboost-python-dev \
	libboost-regex-dev \
        libcairo2-dev \
        libeigen3-dev \
        liblapack-dev \
        libopenblas-dev \
        libsuitesparse-dev \
        libsqlite3-dev \
        libssl-dev \
        make \
        openssh-client \
        python-dev \
        sqlite3 \
        unzip \
        vim \
        wget \
        zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#
# build python
#
RUN set -ex \
    && curl -fSL "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" -o python.tar.xz \
    && mkdir -p /usr/src/python \
    && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
    && rm python.tar.xz \
    && cd /usr/src/python \
    && ./configure --enable-shared --enable-unicode=ucs4 \
    && make -j$(nproc) \
    && make install \
    && make clean \
    && ldconfig \
    && pip3 install --no-cache-dir --upgrade --ignore-installed pip==$PYTHON_PIP_VERSION \
    && find /usr/local \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && rm -rf /usr/src/python ~/.cache

#
# link symbols
#
RUN cd /usr/local/bin \
    && ln -s "easy_install-${PYTHON_MAJOR}" easy_install \
    && ln -s idle3 idle \
    && ln -s pydoc3 pydoc \
    && ln -s python3 python \
    && ln -s python3-config python-config

#
# install requirements of python libraries for rdkit
#
RUN pip3 install --no-cache-dir \
    numpy \
    pandas \
    cffi \
    pillow
RUN pip3 install --no-cache-dir \
    cairocffi

#
# environments settings for rdkit
#
ENV RDBASE=/usr/local/lib/python${PYTHON_MAJOR}/site-packages/rdkit \
    LD_LIBRARY_PATH=/usr/local/lib/python${PYTHON_MAJOR}/site-packages/rdkit/lib:/usr/include/boost \
    PYTHONPATH=$PYTHONPATH:/usr/local/lib/python${PYTHON_MAJOR}/site-packages/rdkit

#
# build rdkit
#
RUN wget "https://github.com/rdkit/rdkit/archive/Release_$RDKIT_RELEASE_VERSION.tar.gz" -O rdkit.tar.gz \
    && mkdir -p $RDBASE $RDBASE/build \
    && tar -zxC $RDBASE --strip-components=1 -f rdkit.tar.gz \
    && rm rdkit.tar.gz \
    && cd $RDBASE/build \
    && cmake \
        -D CMAKE_INSTALL_PREFIX=/usr/local/lib/python${PYTHON_MAJOR} \
        -D PYTHON_INCLUDE_DIR=/usr/local/include/python${PYTHON_MAJOR}m \
        -D PYTHON_EXECUTABLE=/usr/local/bin/python \
        -D PYTHON_LIBRARY=/usr/local/lib/python${PYTHON_MAJOR}/config-${PYTHON_MAJOR}m/libpython${PYTHON_MAJOR}m.a \
	        -D RDK_BUILD_INCHI_SUPPORT=ON \
        -D RDK_BUILD_AVALON_SUPPORT=ON \
        -D RDK_BUILD_CAIRO_SUPPORT=ON \
        -D PYTHON_NUMPY_INCLUDE_PATH=/usr/local/lib/python${PYTHON_MAJOR}/site-packages/numpy/core/include/ \
        .. \
    && make -j$(nproc) \
    && make install \
    && make clean \
    && cp ../External/INCHI-API/python/*.py ../rdkit/Chem/
