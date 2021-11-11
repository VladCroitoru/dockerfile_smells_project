FROM alpine:latest
MAINTAINER Wesley Castro <root670@gmail.com>

ARG BINUTILS_VERSION=2.32
ARG GCC_VERSION=8.3.0

ENV PATH   $PATH:/usr/local/psxsdk/bin

WORKDIR /build

# Install build dependencies
RUN apk update && apk upgrade && apk add --no-cache \
  bash \
  git \
  cdrkit \
  gcc \
  g++ \
  gmp-dev \
  make \
  mpc1-dev \
  mpfr-dev \
  musl-dev \
  patch \
  wget \
  zlib-dev

# Compile binutils
RUN wget http://ftpmirror.gnu.org/binutils/binutils-${BINUTILS_VERSION}.tar.xz && \
  tar -xf binutils-${BINUTILS_VERSION}.tar.xz && \
  rm binutils-${BINUTILS_VERSION}.tar.xz && \
  cd binutils-${BINUTILS_VERSION} && \
  mkdir build && \
  cd build && \
  ../configure --disable-nls --prefix='/usr/local/psxsdk' --target=mipsel-unknown-elf --with-float=soft && \
  make && \
  make install && \
  cd ../.. && \
  rm -rf binutils-${BINUTILS_VERSION}

# Compile GCC
RUN wget http://ftpmirror.gnu.org/gcc/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.xz && \
  tar -xf gcc-${GCC_VERSION}.tar.xz && \
  rm gcc-${GCC_VERSION}.tar.xz && \
  cd gcc-${GCC_VERSION} && \
  mkdir build && \
  cd build && \
  ../configure --disable-nls --disable-libada --disable-libssp --disable-libquadmath --disable-libstdc++-v3 --target=mipsel-unknown-elf --prefix='/usr/local/psxsdk' --with-float=soft --enable-languages=c && \
  make && \
  make install-strip && \
  cd ../.. && \
  rm -rf gcc-${GCC_VERSION}

RUN pwd
# Compile PSXSDK
RUN git clone --depth 1 https://github.com/root670/psxsdk.git && \
  cd psxsdk && \
  sed -i.tmp "s/MAKE_COMMAND = gmake/MAKE_COMMAND = make/g" Makefile.cfg && \
  sed -i.tmp "s/ENABLE_CXX = yes/ENABLE_CXX = no/g" Makefile.cfg && \
  sed -i.tmp "s/EXAMPLES_VMODE = VMODE_PAL/EXAMPLES_VMODE = VMODE_NTSC/g" Makefile.cfg && \
  make && \
  make install && \
  cd .. && \
  rm -rf psxsdk

# Remove dependencies no longer needed
RUN cd / && \
  rm -rf /build/* && \
  apk del \
  gcc \
  g++ \
  musl-dev
