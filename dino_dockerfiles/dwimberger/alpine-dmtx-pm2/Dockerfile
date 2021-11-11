FROM keymetrics/pm2-docker-alpine

MAINTAINER Dieter Wimberger "dieter@wimpi.net"

WORKDIR /

# Install deps
RUN apk add --no-cache build-base gcc binutils binutils-doc gcc-doc g++ make autoconf automake libtool git imagemagick imagemagick-dev lcms2 fontconfig freetype zlib

# Fix lib references
RUN ln -s /usr/lib/libfreetype.so.6 /usr/lib/libfreetype.so
RUN ln -s /usr/lib/liblcms2.so.2 /usr/lib/liblcms2.so
RUN ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so
RUN ln -s /lib/libz.so.1 /lib/libz.so

# Clone reps
RUN git clone git://libdmtx.git.sourceforge.net/gitroot/libdmtx/libdmtx
RUN git clone git://libdmtx.git.sourceforge.net/gitroot/libdmtx/dmtx-utils

# Build libdmtx
WORKDIR /libdmtx
RUN ./autogen.sh;./configure ; make; make install; make clean

# Build dmtx-utils
WORKDIR /dmtx-utils
RUN ./autogen.sh
RUN PKG_CONFIG_PATH=/usr/local/lib/pkgconfig CFLAGS="-I/libdmtx/" ./configure
RUN make; make install; make clean

# Remove build only stuff
RUN apk del --no-cache build-base gcc binutils binutils-doc gcc-doc g++ make autoconf automake libtool git imagemagick-dev
RUN rm -rf libdmtx
RUN rm -rf dmtx-utils

WORKDIR /dmtx


