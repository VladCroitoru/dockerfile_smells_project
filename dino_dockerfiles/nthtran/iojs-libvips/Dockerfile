# iojs + libvips
# Adapted from https://github.com/marcbachmann/dockerfile-libvips
FROM iojs:1.6.1

# Install dependencies
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
  automake \
  gobject-introspection \
  gtk-doc-tools \
  libglib2.0-dev \
  libjpeg62-turbo-dev \
  libpng12-dev \
  libwebp-dev \
  libtiff5-dev \
  libexif-dev \
  libxml2-dev \
  swig \
  libmagickwand-dev

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
RUN apt-get remove -y automake && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*