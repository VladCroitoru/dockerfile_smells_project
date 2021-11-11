FROM gawbul/docker-ubuntu1604-base

RUN mkdir -p /opt/tools

WORKDIR /opt/tools

# install R
RUN \
  export R_LIBS= && \
  wget -c https://cran.r-project.org/src/base/R-3/R-3.3.2.tar.gz && \
  tar -zxvf R-3.3.2.tar.gz && \
  cd R-3.3.2 && \
  ./configure --with-x=no && \
  make && \
  make install
