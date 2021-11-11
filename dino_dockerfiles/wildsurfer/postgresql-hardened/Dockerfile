FROM postgres:12.1-alpine

MAINTAINER Ivan Kuznetsov <kuzma.wm@gmail.com>

RUN apk add --no-cache --virtual build-deps make build-base py-pip clang llvm && \
  pip install pgxnclient && \
  pgxn install safeupdate && \
  echo "shared_preload_libraries=safeupdate" >> /usr/local/share/postgresql/postgresql.conf.sample && \
  apk del build-deps