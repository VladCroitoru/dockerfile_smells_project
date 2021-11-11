FROM alpine:3.3

MAINTAINER aurelien@derniercri.io

ENV PACKAGES make gcc musl-dev

RUN apk add --update $PACKAGES && \
  cd /root && \
  wget http://www.devin.com/lookbusy/download/lookbusy-1.4.tar.gz && \
  tar -xzf lookbusy-1.4.tar.gz && \
  cd lookbusy-1.4/ && \
  ./configure && \
  make install && \
  cd .. && \
  rm -rfv lookbusy-1.4* && \
  apk del $PACKAGES

ENTRYPOINT ["/usr/local/bin/lookbusy"]

CMD ["--help"]