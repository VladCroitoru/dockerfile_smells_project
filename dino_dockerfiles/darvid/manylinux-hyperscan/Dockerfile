ARG boost_version=1.57.0
ARG build_type=RelWithDebugInfo
ARG hyperscan_version=v5.4.0
ARG pcre_version=8.44
ARG ragel_version=6.10

FROM quay.io/pypa/manylinux_2_24_x86_64 AS base
RUN apt-get update && apt-get install -y gcc wget

FROM base AS base_ragel
ARG ragel_version
WORKDIR /tmp
RUN apt-get update && apt-get install -y gcc git wget
RUN wget -qO- https://www.colm.net/files/ragel/ragel-${ragel_version}.tar.gz | tar -vxz
WORKDIR /tmp/ragel-${ragel_version}
RUN ./configure --prefix=/usr && make && make install

FROM base_ragel as base_hyperscan
ARG boost_version
ARG hyperscan_version
WORKDIR /tmp
RUN git clone -b ${hyperscan_version} https://github.com/01org/hyperscan.git
RUN wget -qO- http://downloads.sourceforge.net/project/boost/boost/${boost_version}/boost_$(echo "${boost_version}" | tr . _).tar.bz2 | tar xj
RUN mv boost*/boost hyperscan/include

FROM base_hyperscan as build_pcre
ARG pcre_version
ENV CFLAGS=-fPIC
WORKDIR /tmp/hyperscan
RUN wget -qO- https://ftp.pcre.org/pub/pcre/pcre-${pcre_version}.tar.gz | tar xvz
WORKDIR /tmp/hyperscan/pcre-${pcre_version}
RUN ./configure --prefix=/opt/pcre --enable-unicode-properties --enable-utf
RUN make && make install
RUN cp -r .libs /opt/pcre/
WORKDIR /tmp/hyperscan

FROM build_pcre AS build_hyperscan
ARG build_type
ARG pcre_version
RUN mkdir -p build
WORKDIR /tmp/hyperscan/build
ENV CFLAGS="-fPIC"
ENV CXXFLAGS="$CFLAGS -D_GLIBCXX_USE_CXX11_ABI=1"
RUN cmake \
  -DCMAKE_INSTALL_PREFIX=/opt/hyperscan \
  -DFAT_RUNTIME=ON \
  -DBUILD_STATIC_AND_SHARED=ON \
  -DCMAKE_BUILD_TYPE=${build_type} \
  -DPCRE_SOURCE=../pcre-${pcre_version} \
  -DCMAKE_C_FLAGS="${CFLAGS}" \
  -DCMAKE_CXX_FLAGS="${CXXFLAGS}" \
  ../
RUN make -j$(nproc) && make install

FROM quay.io/pypa/manylinux_2_24_x86_64
ARG pcre_version
ENV LD_LIBRARY_PATH=/opt/hyperscan/lib:${LD_LIBRARY_PATH}
ENV PKG_CONFIG_PATH=/opt/hyperscan/lib/pkgconfig
ENV PKG_CONFIG_PATH=/opt/pcre/lib/pkgconfig:${PKG_CONFIG_PATH}
ENV C_INCLUDE_PATH=/opt/hyperscan/include/hs
LABEL maintainer="David Gidwani <david.gidwani@gmail.com>"
WORKDIR /opt
COPY --from=build_hyperscan /opt/pcre/ pcre
COPY --from=build_hyperscan /opt/hyperscan/ hyperscan
