# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.16
MAINTAINER Dominic Böttger

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nodejs ssh git build-essential python pkg-config
RUN apt-get install -y catdoc poppler-utils tesseract-ocr unzip
RUN mkdir /var/node

# Install dependencies
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
  automake build-essential curl \
  gobject-introspection gtk-doc-tools libglib2.0-dev libjpeg-turbo8-dev libpng12-dev libwebp-dev libtiff5-dev libexif-dev libxml2-dev swig libmagickwand-dev

# Build libvips
WORKDIR /tmp
ENV LIBVIPS_VERSION_MAJOR 7
ENV LIBVIPS_VERSION_MINOR 42
ENV LIBVIPS_VERSION_PATCH 3
ENV LIBVIPS_VERSION $LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR.$LIBVIPS_VERSION_PATCH
RUN \
  curl -O http://www.vips.ecs.soton.ac.uk/supported/$LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR/vips-$LIBVIPS_VERSION.tar.gz && \
  tar zvxf vips-$LIBVIPS_VERSION.tar.gz && \
  cd vips-$LIBVIPS_VERSION && \
  ./configure --enable-debug=no --enable-docs=no --without-python --without-orc --without-fftw --without-gsf $1 && \
  make && \
  make install && \
  ldconfig

# Clean up
WORKDIR /
RUN apt-get autoremove -y && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN npm install -g bower

WORKDIR /var/node

VOLUME ["/var/node"]
EXPOSE 3000
EXPOSE 3443
CMD ["node", "app.js"]
