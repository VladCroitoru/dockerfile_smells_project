FROM resin/armv7hf-debian-qemu

RUN [ "cross-build-start" ]

MAINTAINER Péter Szilágyi <peterke@gmail.com>

RUN \
  apt-get update && apt-get install ca-certificates golang git musl-dev -y && \
	mkdir /work && export GOPATH=/work               && \
	\
	go get github.com/karalabe/cloudflare-dyndns      && \
	cp /work/bin/cloudflare-dyndns /cloudflare-dyndns && \
	\
  apt-get remove golang git musl-dev -y && \
  rm -rf /work && rm -rf /var/cache/apt/*

RUN [ "cross-build-end" ]

ENTRYPOINT ["/cloudflare-dyndns"]
