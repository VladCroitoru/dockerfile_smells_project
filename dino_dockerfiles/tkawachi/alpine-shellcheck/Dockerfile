FROM mitchty/alpine-ghc:latest AS builder

MAINTAINER Takashi Kawachi <tkawachi@gmail.com>

RUN apk add --no-cache build-base git


RUN mkdir -p /usr/src/shellcheck
WORKDIR /usr/src/shellcheck

RUN git clone https://github.com/koalaman/shellcheck .
RUN git checkout v0.4.6

RUN cabal update && cabal install

ENV PATH="/root/.cabal/bin:$PATH"


# Get shellcheck binary
RUN mkdir -p /package/bin/
RUN cp $(which shellcheck) /package/bin/

# Get shared libraries
RUN mkdir -p /package/lib/
RUN ldd $(which shellcheck) | grep "=> /" | awk '{print $3}' | xargs -I '{}' cp -v '{}' /package/lib/

FROM alpine:latest

MAINTAINER Takashi Kawachi <tkawachi@gmail.com>

COPY --from=builder /package/bin/shellcheck /usr/local/bin/
COPY --from=builder /package/lib/           /usr/local/lib/

RUN ldconfig /usr/local/lib

WORKDIR /mnt
ENTRYPOINT ["shellcheck"]
