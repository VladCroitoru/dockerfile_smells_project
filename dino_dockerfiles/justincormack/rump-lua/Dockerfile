# Build Lua with Docker

FROM justincormack/frankenlibc

MAINTAINER Justin Cormack

COPY . /usr/src/lua51

WORKDIR /usr/src/lua51

ENV CC=rumprun-cc

RUN curl http://www.lua.org/ftp/lua-5.1.5.tar.gz | tar xzf - && \
  cd lua-5.1.5 && \
  sed -i 's/CC= gcc//' src/Makefile && \
  make bsd && \
  make install && \
  make clean
