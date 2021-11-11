FROM ubuntu:trusty

# libvips version to use
ENV LIBVIPS_VERSION 8.7.2

# Imaginary version to use
ENV IMAGINARY_VERSION 1.0.15

# Go version to use
ENV GOLANG_VERSION 1.11.2
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN \

  # Install dependencies
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    automake build-essential curl \
    gobject-introspection gtk-doc-tools libglib2.0-dev libjpeg-turbo8-dev libpng12-dev \
    libwebp-dev libtiff5-dev libgif-dev libexif-dev libxml2-dev libpoppler-glib-dev \
    swig libmagickwand-dev libpango1.0-dev libmatio-dev libopenslide-dev libcfitsio3-dev \
    libgsf-1-dev fftw3-dev liborc-0.4-dev librsvg2-dev \
    gcc git libc6-dev make && \

  # Build libvips
  cd /tmp && \
  curl -OL https://github.com/libvips/libvips/releases/download/v${LIBVIPS_VERSION}/vips-${LIBVIPS_VERSION}.tar.gz && \
  tar zvxf vips-${LIBVIPS_VERSION}.tar.gz && \
  cd /tmp/vips-${LIBVIPS_VERSION} && \
  ./configure --enable-debug=no --without-python $1 && \
  make && \
  make install && \
  ldconfig  && \

  # Build Go, gcc (cgo)
  curl -L -o golang.tar.gz https://golang.org/dl/go${GOLANG_VERSION}.linux-amd64.tar.gz && \
  tar -C /usr/local -xzf golang.tar.gz && \
  rm -f golang.tar.gz && \
  mkdir -p "${GOPATH}/src" "${GOPATH}/bin" && \
  chmod -R 777 "${GOPATH}" && \

  # Get, pin and install the specific package
  go get -u golang.org/x/net/context && \
  go get -d -u github.com/h2non/imaginary && \
  cd ${GOPATH}/src/github.com/h2non/imaginary && \
  git checkout v${IMAGINARY_VERSION} && \
  go install && \

  # Cleanup
  rm -rf ${GOPATH}/src/ && \
  rm -rf /usr/local/go && \
  apt-get remove -y curl automake build-essential \
    gtk-doc-tools libglib2.0-dev libjpeg-turbo8-dev libpng12-dev \
    libwebp-dev libtiff5-dev libgif-dev libexif-dev libxml2-dev libpoppler-glib-dev \
    swig libmagickwand-dev libpango1.0-dev libmatio-dev libopenslide-dev libcfitsio3-dev \
    libgsf-1-dev fftw3-dev liborc-0.4-dev librsvg2-dev \
    gcc git libc6-dev make && \
  apt-get autoclean && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Server port to listen
ENV PORT 9000

# Expose the server TCP port
EXPOSE 9000

# Run the outyet command by default when the container starts.
ENTRYPOINT ["/go/bin/imaginary"]
