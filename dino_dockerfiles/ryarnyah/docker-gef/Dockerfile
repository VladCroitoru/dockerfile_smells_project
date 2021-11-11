FROM debian:jessie
MAINTAINER Ryar Nyah <ryarnyah@gmail.com>

# Install GEF
RUN useradd -ms /bin/bash gef && \
  dpkg --add-architecture i386 && \
  apt-get update && \
  apt-get install python-pip gdb gdbserver gdb-multiarch git make gcc g++ wget cmake pkg-config libc6:i386 libstdc++6:i386 libglib2.0-dev binutils -y && \
  pip install ropgadget ropper capstone keystone-engine && \
  mkdir /src && \
  cd /src && \
  cd /src && git clone https://github.com/unicorn-engine/unicorn.git && cd unicorn/bindings/python/ && make install && \
  cd /src && git clone https://github.com/keystone-engine/keystone.git && cd keystone/bindings/python && make install && \
  wget -q -O /src/gdbinit-gef.py https://github.com/hugsy/gef/raw/master/gef.py && chmod o+r /src/gdbinit-gef.py && \
  apt-get remove -y --purge git make gcc g++ wget cmake pkg-config && apt-get autoremove -y --purge && apt-get -y autoclean

USER gef
RUN echo source /src/gdbinit-gef.py > ~/.gdbinit
