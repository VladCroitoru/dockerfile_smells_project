FROM node:latest

# GCC @ https://github.com/wanglilong007/debian-jessie-gcc/blob/master/Dockerfile
# LIBVIPS @ https://github.com/TailorBrands
# node:latest @ https://github.com/nodejs/docker-node
# apt-utls @ https://github.com/phusion/baseimage-docker/issues/319#issuecomment-245857919

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
  automake build-essential curl gobject-introspection \
  gtk-doc-tools libglib2.0-dev libturbojpeg1-dev libpng12-dev \
  libwebp-dev libtiff5-dev libgif-dev libexif-dev libxml2-dev \
  libpoppler-glib-dev swig libmagickwand-dev libpango1.0-dev \
  libmatio-dev libopenslide-dev libcfitsio3-dev libgsf-1-dev \
  fftw3-dev liborc-0.4-dev librsvg2-dev gobject-introspection \ 
  gcc wget make g++ openssl libssl-dev libpcre3 libpcre3-dev zlib1g zlib1g-dev \
  nano sudo
# install sudo & nano etc.

ENV LIBVIPS_VERSION_MAJOR 8

ENV LIBVIPS_VERSION_MINOR 5

ENV LIBVIPS_VERSION_PATCH 5
# We set this to 5 to match the sharp lib, but it's interchangeable anyways with later versions.

ENV LIBVIPS_VERSION $LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR.$LIBVIPS_VERSION_PATCH

RUN cd /tmp && \
  curl -L -O https://github.com/jcupitt/libvips/releases/download/v$LIBVIPS_VERSION/vips-$LIBVIPS_VERSION.tar.gz && \
  tar zxvf vips-$LIBVIPS_VERSION.tar.gz && \
  cd /tmp/vips-$LIBVIPS_VERSION && \
  ./configure --enable-debug=no --without-python $1 && \
  make && \
  make install && \
  ldconfig
# Build libvips

RUN chown -R node:node /usr/local/lib/node_modules && chown -R node:node /usr/local/bin
# We chown the folders so we can npm install --global flawlessly
# https://github.com/me-ventures/angular-cli-docker/blob/master/Dockerfile

RUN sudo -u node npm install sharp --global
# You can't switch to another user, but you can run as another user.
# https://unix.stackexchange.com/a/3572

RUN echo 'export NODE_PATH="'$(npm root -g)'"' >> ~/.bashrc
# Setting node path in env is now mandatory export NODE_PATH thru ~/.bashrc
# https://askubuntu.com/a/438170
# https://stackoverflow.com/questions/15636367/nodejs-require-a-global-module-package#comment31655957_15646750

RUN apt-get remove -y automake curl build-essential && \
  apt-get autoremove -y && \
  apt-get autoclean && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Clean-up.

CMD [ "/bin/bash" ]
