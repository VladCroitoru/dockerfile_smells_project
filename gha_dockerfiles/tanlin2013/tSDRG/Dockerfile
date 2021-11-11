FROM intel/oneapi-basekit
FROM intel/oneapi-hpckit
MAINTAINER "TaoLin" <tanlin2013@gmail.com>

ARG WORKDIR=/home
WORKDIR $WORKDIR

COPY . $WORKDIR

RUN tar -xzvf uni10-2.0.0.tar.gz

# Installing Uni10 v2.0.0
RUN cd uni10-2.0.0 \
    && mkdir build \
    && cd build \
    && cmake -DBUILD_WITH_MKL=on -DBUILD_WITH_INTEL_COMPILERS=on .. \
    && make \
    && make install

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/uni10/lib/
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:/usr/local/uni10/include/
ENV CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/uni10/include/

ENTRYPOINT /bin/bash
