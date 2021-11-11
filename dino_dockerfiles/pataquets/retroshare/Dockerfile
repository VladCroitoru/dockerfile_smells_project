FROM gcc

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      libglib2.0-dev libupnp-dev qt4-dev-tools \
      libqt4-dev libssl-dev libxss-dev libgnome-keyring-dev libbz2-dev \
      libqt4-opengl-dev libsqlcipher-dev \
      libspeex-dev libspeexdsp-dev libxslt1-dev libcurl4-openssl-dev \
      libopencv-dev tcl8.5 libmicrohttpd-dev \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

COPY . /usr/src/retroshare
WORKDIR /usr/src/retroshare

RUN qmake PREFIX=/usr LIB_DIR=/usr/lib64 "CONFIG-=debug" "CONFIG+=release"
RUN make
RUN make install
