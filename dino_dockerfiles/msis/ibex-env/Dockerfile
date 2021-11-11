# Start off a GCC:4.8 image based on wheezy
FROM gcc:4.8

# Feel free to email me if you need support
MAINTAINER Mohamed Saad IBN SEDDIK <ms.ibnseddik@gmail.com>

## Installation of python 2.7.9
#### A little bit of cleaning inspired from the official python image that uses jessie
# remove several traces of debian python
RUN apt-get purge -y python.*

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

ENV PYTHON_VERSION 2.7.9

# gpg: key 18ADD4FF: public key "Benjamin Peterson <benjamin@python.org>" imported
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF

RUN set -x \
  && mkdir -p /usr/src/python \
  && curl -SL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz" -o python.tar.xz \
  && curl -SL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc" -o python.tar.xz.asc \
  && gpg --verify python.tar.xz.asc \
  && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
  && rm python.tar.xz* \
  && cd /usr/src/python \
  && ./configure --enable-shared --enable-unicode=ucs4 \
  && make -j$(nproc) \
  && make install \
  && ldconfig \
  && curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2 \
  && find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' + \
  && rm -rf /usr/src/python

# install "virtualenv", since the vast majority of users of this image will want it
RUN pip install virtualenv
## Installation of python done

# Install ibex dependecies
RUN apt-get update \
  && apt-get install -y coinor-libclp-dev bison flex

# Change WORKDIR
WORKDIR /usr/src/

# Install latest version of ibex
RUN git clone https://github.com/ibex-team/ibex-lib.git \
  && cd ibex-lib \
  && ./waf configure \
  && ./waf install -j$(nproc)

# Export new variables for use
ENV PKG_CONFIG_PATH /usr/local/share/pkgconfig/
ENV LD_LIBRARY_PATH /usr/local/lib

# Move to slam examples workdir
WORKDIR /usr/src/ibex-lib/examples/slam

# Copy updated makefile
COPY Makefile /usr/src/ibex-lib/examples/slam/makefile

# Compile slam examples
RUN make

# Run an example
RUN ./slam1