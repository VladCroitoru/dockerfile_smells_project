FROM gawbul/docker-ubuntu1604-base

RUN mkdir -p /opt/tools

WORKDIR /opt/tools

# install hisat2
RUN \
  wget -c ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.0.5-source.zip && \
  unzip hisat2-2.0.5-source.zip && \
  cd hisat2-2.0.5 && \
  make && \
  cp hisat2* /usr/local/bin 
