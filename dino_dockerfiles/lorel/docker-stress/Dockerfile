FROM alpine:3.3

MAINTAINER aurelien@derniercri.io

ENV PACKAGES make gcc musl-dev linux-headers

RUN apk add --update $PACKAGES && \
  cd /root && \
  wget http://people.seas.harvard.edu/~apw/stress/stress-1.0.4.tar.gz && \
  tar -xzf stress-1.0.4.tar.gz && \
  cd stress-1.0.4/ && \
  ./configure && \
  make install && \
  cd .. && \
  rm -rfv stress-1.0.4* && \
  apk del $PACKAGES

ENTRYPOINT ["/usr/local/bin/stress"]

CMD ["--help"]
