FROM alpine:3.9

LABEL maintainer="James Kyburz james.kyburz@gmail.com"

MAINTAINER James Kyburz "james.kyburz@gmail.com"

RUN apk --no-cache add libgomp libltdl libpng libjpeg tiff libwebp-tools

RUN apk --no-cache add --virtual native-deps \
  tar wget libjpeg-turbo-dev libpng-dev libtool libxml2 jasper-libs giflib-dev tiff-dev \
  git g++ gcc libgcc libstdc++ linux-headers make python && \
  wget https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-0.6.1.tar.gz && \
  tar -xzvf libwebp-0.6.1.tar.gz && \
  cd libwebp-0.6.1 && \
  ./configure && \
  make && \
  make install && \
  cd .. && \
  wget https://downloads.sourceforge.net/graphicsmagick/graphicsmagick/1.3.26/GraphicsMagick-1.3.26.tar.gz && \
  tar xvzf GraphicsMagick-1.3.26.tar.gz && \
  cd GraphicsMagick-1.3.26 && \
  ./configure \
    --build=$CBUILD \
    --host=$CHOST \
    --prefix=/usr \
    --sysconfdir=/etc \
    --mandir=/usr/share/man \
    --infodir=/usr/share/info \
    --localstatedir=/var \
    --enable-shared \
    --disable-static \
    --with-modules \
    --with-threads \
    --with-webp=yes \
    --with-tiff=yes \
    --with-jpeg=yes \
    --with-jp2=yes \
    --with-gs-font-dir=/usr/share/fonts/Type1 \
    --with-quantum-depth=16 && \
  make && \
  make install && \
  cd .. && \
  rm -rf Graphics* && \
  rm -rf libweb* && \
  apk del native-deps
