FROM gliderlabs/alpine:latest
MAINTAINER Romain BOURDY <romain@bourdy.eu>

RUN  apk add --verbose --update libffi-dev python-dev git g++ make perl coreutils ; \
  rm -rf /var/cache/apk/* ; \
  cd / ;\
  git clone https://github.com/micropython/micropython.git ; \
  git clone https://github.com/micropython/micropython-lib.git ; \
  cd /micropython/unix &&  make axtls &&  make && make instakk ; \
  cd  /micropython-lib &&  make install && cd / && rm -rf micropython-lib micropython

ENTRYPOINT ["/usr/local/bin/micropython"]
