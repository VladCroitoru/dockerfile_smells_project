FROM node:7

# Install required dependencies (Debian packages)
RUN \
  apt-get install \
  tar \
  g++ \
  gcc \
  make \
  git \
  python \
  curl

# setup installation env
RUN \
  mkdir -p /tmp \
  && cd /tmp

# sass install
RUN \
  cd /tmp \
  && git clone https://github.com/sass/sassc \
  && cd sassc \
  && git clone https://github.com/sass/libsass \
  && SASS_LIBSASS_PATH=/tmp/sassc/libsass make \
  && mv /tmp/sassc/bin/sassc /usr/bin/sass

# install (global) NPM packages/dependencies
RUN \
  npm install -g \
  node-gyp \
  node-sass

# install phantomjs
ENV PHANTOMJS_BIN "/usr/local/bin/phantomjs"
RUN \
  npm install -g phantomjs-prebuilt

# cleanup
RUN \
  rm -rf /tmp \
  && npm cache clean -f

# Create an empty writable /tmp folder (required by the kind of Karma)
RUN \
  mkdir /tmp \
  && chmod 777 /tmp
