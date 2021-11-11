FROM gcc

ADD . /usr/src/ostiary
WORKDIR /usr/src/ostiary

RUN \
  ./configure && \
  make all && \
  make install && \
  mv -vi \
    /usr/local/etc/ostiary.cfg \
    /usr/local/etc/ostiary.cfg.default
