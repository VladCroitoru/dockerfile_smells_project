FROM alpine
LABEL description="Builds API static binary"
MAINTAINER Nnwww <johndororo@gmail.com>

# update repositories (add edge main & community)
RUN echo "https://dl-3.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    echo "https://dl-3.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

# install libraries
RUN apk update && apk upgrade && \
    apk add alpine-sdk git linux-headers ca-certificates gmp-dev zlib-dev curl ghc upx shadow

# install stack & set system-ghc because stack fail to resolve compiler in alpine linux.
RUN curl -sSL https://get.haskellstack.org/ | sh && \
    stack config set system-ghc --global true
