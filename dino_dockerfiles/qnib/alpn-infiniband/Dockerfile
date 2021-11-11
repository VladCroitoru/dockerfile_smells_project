FROM qnib/alpn-terminal

ENV LIBIBCOMMON_VER=1.0.4 \
    LIBIBUMAD_VER=1.3.10.1 \
    LIBIBMAD_VER=1.1.1 \
    LDFLAGS=-L/usr/local/lib/ \
    CPPFLAGS=-I/usr/local/include
RUN apk update && apk upgrade && \
    apk add vim wget tar g++ make libgcrypt-dev perl file && \
    wget -qO- https://www.openfabrics.org/~halr/libibcommon-${LIBIBCOMMON_VER}.tar.gz |tar xfz - -C /opt/ && \
    cd /opt/libibcommon-${LIBIBCOMMON_VER} && \
    ./configure && make && make install && \
    wget -qO- https://www.openfabrics.org/~halr/libibumad-${LIBIBUMAD_VER}.tar.gz |tar xfz - -C /opt/ && \
    cd /opt/libibumad-${LIBIBUMAD_VER} && \
    ./configure && make && make install && \
    wget -qO- https://www.openfabrics.org/~halr/libibmad-${LIBIBMAD_VER}.tgz |tar xfz - -C /opt/ && \
    cd /opt/libibmad-${LIBIBMAD_VER} && \
    ./configure && make && make install && \
    apk del g++ make perl tar wget libgcrypt-dev && \
    rm -rf /var/cache/apk/*
