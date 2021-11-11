FROM debian:jessie

RUN \
  useradd -r -s /bin/false varnishd

# Install Varnish source build dependencies.
RUN \
  apt-get update && apt-get install -y --no-install-recommends \
    automake \
    build-essential \
    ca-certificates \
    curl \
    libedit-dev \
    libjemalloc-dev \
    libncurses-dev \
    libpcre3-dev \
    libtool \
    pkg-config \
    python-docutils \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Varnish from source, so that Varnish modules can be compiled and installed.
ENV VARNISH_VERSION=4.1.2
ENV VARNISH_SHA256SUM=9728da944d28eb5be90e7ab6799c2c4c831ef4df5e5154537eb7f2e5d5e348c4
RUN \
  apt-get update && \
  mkdir -p /usr/local/src && \
  cd /usr/local/src && \
  curl -sfLO https://repo.varnish-cache.org/source/varnish-$VARNISH_VERSION.tar.gz && \
  echo "${VARNISH_SHA256SUM} varnish-$VARNISH_VERSION.tar.gz" | sha256sum -c - && \
  tar -xzf varnish-$VARNISH_VERSION.tar.gz && \
  cd varnish-$VARNISH_VERSION && \
  ./autogen.sh && \
  ./configure && \
  make install && \
  rm ../varnish-$VARNISH_VERSION.tar.gz

COPY start-varnishd.bash /start-varnishd.bash

ENV VARNISH_PORT 80
ENV VARNISH_STORAGE_BACKEND malloc,100m
ENV VARNISH_BACKEND_HOST 127.0.0.1
ENV VARNISH_BACKEND_PORT 8080

CMD ["/bin/bash", "/start-varnishd.bash"]
