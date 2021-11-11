## Versions
FROM alpine:3 AS alpine
ENV BATS_VERSION 1.3.0

## Builder
FROM alpine AS builder
RUN mkdir /bats-src
WORKDIR /bats-src
RUN apk add --update --no-cache \
  bash \
  ca-certificates \
  curl \
  tar \
  && true
RUN curl -sSLf \
  -o bats-core.tgz \
  "https://github.com/bats-core/bats-core/archive/v${BATS_VERSION}.tar.gz"
RUN tar -z -x -f bats-core.tgz
RUN cd bats-core* && ./install.sh /usr/local
COPY entrypoint.bash /usr/local/bin/docker-entrypoint.bash
RUN chmod +x /usr/local/bin/docker-entrypoint.bash

## Release image
FROM alpine AS release
WORKDIR /src
VOLUME {"/src"}
RUN \
  apk add --update --no-cache \
  bash \
  ncurses \
  && true
COPY --from=builder /usr/local/ /usr/local/
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.bash"]
CMD ["--help"]
