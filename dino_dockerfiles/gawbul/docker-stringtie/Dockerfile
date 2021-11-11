FROM gawbul/docker-ubuntu1604-base

RUN mkdir -p /opt/tools

WORKDIR /opt/tools

# install stringtie
RUN \
  wget -c http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.3.3.tar.gz && \
  tar -zxvf stringtie-1.3.3.tar.gz && \
  cd stringtie-1.3.3 && \
  make && \
  cp stringtie /usr/local/bin
