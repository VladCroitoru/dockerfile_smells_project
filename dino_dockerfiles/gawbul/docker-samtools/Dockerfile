FROM gawbul/docker-ubuntu1604-base

RUN mkdir -p /opt/tools

WORKDIR /opt/tools

# install htslib
RUN \
  wget -c https://github.com/samtools/htslib/archive/1.3.2.tar.gz && \
  tar -zxvf 1.3.2.tar.gz && \
  mv htslib-1.3.2 htslib && \
  cd htslib && \
  autoreconf && \
  ./configure && \
  make && \
  make install

# install samtools
RUN \
  wget -c https://github.com/samtools/samtools/archive/1.3.1.tar.gz && \
  tar -zxvf 1.3.1.tar.gz && \
  cd samtools-1.3.1 && \
  make && \
  make install
