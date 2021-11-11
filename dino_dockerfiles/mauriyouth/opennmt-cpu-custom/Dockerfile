FROM ubuntu:14.04

MAINTAINER Mohamed Ahmednah <mauriyouth@gmail.com>

RUN apt-get update && apt-get install -y \
  git \
  software-properties-common \
  ipython3 \
  libssl-dev \
  libzmq3-dev \
  python-zmq \
  python-pip \
  sudo \
  build-essential gcc g++ curl \
  cmake libreadline-dev git-core libqt4-dev libjpeg-dev \
  libpng-dev ncurses-dev imagemagick libzmq3-dev gfortran \
  unzip gnuplot gnuplot-x11 ipython

RUN git clone https://github.com/xianyi/OpenBLAS.git /tmp/OpenBLAS  || { echo "Error. Cannot clone OpenBLAS." >&2 ; exit 1 ; } \
    && cd /tmp/OpenBLAS || { echo "Error. Cannot create tempdir." >&2 ; exit 1 ; }

RUN cd /tmp/OpenBLAS && make NO_AFFINITY=1 USE_THREAD=1 USE_OPENMP=1

RUN cd /tmp/OpenBLAS && make install

RUN git clone https://github.com/torch/distro.git /root/torch --recursive && cd /root/torch && \
  ./install.sh

WORKDIR /root/torch

ENV LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
ENV LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
ENV PATH=/root/torch/install/bin:$PATH
ENV LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH

RUN luarocks install dkjson
# RUN luarocks install lua-zmq ZEROMQ_LIBDIR=/usr/lib/x86_64-linux-gnu/ ZEROMQ_INCDIR=/usr/include
RUN luarocks install sundown
RUN luarocks install cwrap
RUN luarocks install paths
RUN luarocks install torch
RUN luarocks install nn
RUN luarocks install dok
RUN luarocks install gnuplot
RUN luarocks install qtlua
RUN luarocks install qttorch
RUN luarocks install luafilesystem
RUN luarocks install penlight
RUN luarocks install sys
RUN luarocks install xlua
RUN luarocks install image
RUN luarocks install optim
RUN luarocks install lua-cjson
RUN luarocks install trepl
RUN luarocks install nnx
RUN luarocks install threads
RUN luarocks install graphicsmagick
RUN luarocks install argcheck
RUN luarocks install signal
RUN luarocks install bit32
RUN luarocks install restserver-xavante
