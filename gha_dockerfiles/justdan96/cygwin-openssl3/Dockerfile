# syntax=docker/dockerfile:1
FROM fedora:33 AS builder
MAINTAINER Dan Bryant (daniel.bryant@linux.com)

ENV TZ=Europe/London

# install basic dependencies for Linux build
RUN dnf update -y
RUN dnf install -y nano

# install Linux tools required to build Windows packages
RUN dnf install -y cmake gcc make ninja-build zip
RUN dnf upgrade -y

# enable cygwin COPR
RUN dnf install -y dnf-plugins-core
RUN dnf copr enable -y yselkowitz/cygwin
RUN dnf update -y
RUN dnf install -y cygwin-binutils cygwin-filesystem-base cygwin64-gcc cygwin-gcc-common cygwin64-w32api-headers \
	cygwin64-w32api-runtime cygwin64-zlib cygwin64-zlib-static cygwin64-pkg-config cygwin64-gcc-c++
RUN dnf install -y findutils xz
RUN dnf install -y cygwin64-libiconv-static 
RUN dnf download -y --source cygwin-libiconv
RUN rpm -ivh cygwin-libiconv*.src.rpm
RUN rm -f cygwin-libiconv*.src.rpm
RUN dnf install -y perl
RUN dnf install -y byacc flex
RUN dnf install -y git file zip patch

# we put the utilities here
RUN mkdir /opt/openssl3

# clone openssl v3
RUN cd /usr/local/src && git clone --branch openssl-3.0.0 https://github.com/openssl/openssl.git
RUN cd /usr/local/src/openssl && ./Configure Cygwin-x86_64 --cross-compile-prefix=x86_64-pc-cygwin- no-asm no-pinshared --prefix=/opt/openssl3 --openssldir=/opt/openssl3
RUN cd /usr/local/src/openssl && make
RUN cd /usr/local/src/openssl && make install_sw

# clean up the output folder before we package it
RUN rm -f /opt/openssl3/bin/c_rehash
RUN rm -rf /opt/openssl3/include
RUN rm -rf /opt/openssl3/lib/pkgconfig

# make sure to package the cygwin DLLs as well
# we only need cygwin1.dll, cygcrypto-3.dll and cygssl-3.dll
RUN cp /usr/x86_64-pc-cygwin/sys-root/usr/bin/cygwin1.dll /opt/openssl3/bin

# package the ZIP files
RUN cd /opt && zip -r openssl3.zip openssl3

FROM scratch AS export
COPY --from=builder /opt/openssl3.zip .
