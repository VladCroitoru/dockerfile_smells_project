FROM ubuntu:xenial
MAINTAINER David Portabella <david.portabella@gmail.com>

RUN apt-get -y update && apt-get install -y wget gcc-4.9 g++-4.9 m4 make

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 10

RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 10

# http://ftp.gnu.org/gnu/bison/bison-2.3.tar.gz
COPY ./bison-2.3.tar.gz /tmp/

RUN cd /tmp/ && \
  tar -xvzf bison-2.3.tar.gz && \
  cd bison-2.3 && \
  ./configure && \
  make && \
  make install && \
  cd .. && \
  rm -Rf bison-2.3 && \
  rm -Rf bison-2.3.tar.gz

# http://downloads.sourceforge.net/project/flex/flex/2.5.4.a/flex-2.5.4a.tar.gz
# http://pkgs.fedoraproject.org/repo/pkgs/flex/flex-2.5.4a.tar.gz/md5/bd8753d0b22e1f4ec87a553a73021adf/flex-2.5.4a.tar.gz
COPY ./flex-2.5.4a.tar.gz /tmp/

RUN cd /tmp/ && \
  tar -xvzf flex-2.5.4a.tar.gz && \
  cd flex-2.5.4 && \
  ./configure && \
  make && \
  make install && \
  cd .. && \
  rm -Rf flex-2.5.4 && \
  rm -Rf flex-2.5.4a.tar.gz

ENV PATH /usr/local/bin:$PATH

# https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/alchemy-2/alchemy-2.tar.gz
COPY ./alchemy-2.tar.gz /tmp/
RUN cd /tmp/ && \
  tar -xvzf alchemy-2.tar.gz && \
  cd alchemy-2 && \
  cd src && \
  make && \
  find /tmp/alchemy-2/ && \
  rm -Rf ../bin/obj && \
  cp ../bin/* /usr/local/bin/ && \
  cd ../.. && \
  rm -Rf alchemy-2 && \
  rm -Rf alchemy-2.tar.gz

RUN apt-get remove -y wget gcc-4.9 g++-4.9 m4 make

# test it is installed
RUN which learnstruct
RUN which learnwts
RUN which infer
RUN which liftedinfer
RUN which runliftedinfertests
