FROM ubuntu:20.04 as builder

ARG DEBIAN_FRONTEND=noninteractive
ENV PACKAGES "g++ make cmake libboost-all-dev"
ENV SOURCE "/tmp/source"
ENV BUILD "/tmp/build"

RUN apt-get update \
    && apt-get install -y ${PACKAGES}

COPY CMakeLists.txt freddi.ini ${SOURCE}/
COPY cpp ${SOURCE}/cpp

RUN mkdir -p ${BUILD} \
    && cd ${BUILD} \
    && cmake ${SOURCE} -DSTATIC_LINKING=TRUE \
    && make -j4 install VERBOSE=1



FROM ubuntu:20.04

LABEL maintainer="Konstantin Malanchev <malanchev@sai.msu.ru>"

COPY --from=builder /usr/local/bin/freddi /bin/freddi
COPY --from=builder /usr/local/bin/freddi-ns /bin/freddi-ns
COPY --from=builder /usr/local/etc/freddi.ini /etc/freddi.ini

VOLUME /data
WORKDIR /data
