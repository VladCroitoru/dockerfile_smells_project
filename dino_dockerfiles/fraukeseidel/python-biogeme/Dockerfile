FROM python:3.4

RUN \
  curl -O http://biogeme.epfl.ch/distrib/biogeme-2.4.tar.gz && \
  tar xvzf biogeme-2.4.tar.gz && \
  cd biogeme-2.4 && \
  ./configure --enable-bison --enable-python && \
  make && \
  make install && \
  cd .. && \
  rm -rf biogeme-2.4*
