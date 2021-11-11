# calin/Dockerfile -- Stephen Fegan -- 2016-09-08
#
# Copyright 2016, Stephen Fegan <sfegan@llr.in2p3.fr>
# Laboratoire Leprince-Ringuet, CNRS/IN2P3, Ecole Polytechnique, Institut Polytechnique de Paris
#
# This file is part of "calin"
#
# "calin" is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License version 2 or later, as published by
# the Free Software Foundation.
#
# "calin" is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

FROM llrcta/calin-docker-base:ubuntu20.04_v1.37

MAINTAINER sfegan@llr.in2p3.fr

# Allow CPU architecture to be specified at build time, e.g.:
# docker build --build-arg arch=native .
# docker build --build-arg arch=broadwell .
ARG arch=generic

# Allow number of build threads to be specified
ARG threads=2

ADD / /build/calin/

# RUN apt-get update -y
#
# RUN apt-get install -y software-properties-common
#
# RUN add-apt-repository ppa:ubuntu-toolchain-r/test
#
# RUN apt install -y gcc-9 g++-9
#
# RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-9

RUN cd /build/calin &&                                             \
    mkdir mybuild &&                                               \
    cd mybuild &&                                                  \
    cmake -DCALIN_BUILD_ARCH=${arch}                               \
          -DCMAKE_BUILD_TYPE=Release                               \
          -DCMAKE_INSTALL_PREFIX=/usr                              \
          -DCALIN_PYTHON_SUB_DIR=lib/python3.8                     \
          .. &&                                                    \
    make -j${threads} &&                                           \
    make install &&                                                \
    cd / &&                                                        \
    rm -rf /build

CMD ["/usr/local/bin/jupyter-notebook"]
