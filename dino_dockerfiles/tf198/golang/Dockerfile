FROM webhippie/alpine:latest
MAINTAINER Thomas Boerger <thomas@webhippie.de>

WORKDIR /srv/app
CMD ["bash"]

ENV GOPATH /srv/app
ENV GO15VENDOREXPERIMENT 1

ENV PATH /srv/app/bin:/usr/local/go/bin:${PATH}

ENV GOLANG_VERSION 1.8.1
ENV GOLANG_TARBALL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz

ADD rootfs /

RUN apk update && \
  apk add \
    build-base \
    git \
    git-lfs \
    mercurial \
    bzr \
    go && \
  export \
    GOROOT_BOOTSTRAP="$(go env GOROOT)" && \
  curl -sLo - \
    ${GOLANG_TARBALL} | tar -xzf - -C /usr/local && \
  cd \
    /usr/local/go/src && \
  patch -p2 -i \
    /tmp/no-pic.patch && \
  bash \
    make.bash && \
  apk del \
    go && \
  rm -rf \
    /var/cache/apk/*

ARG VERSION
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.version=$VERSION
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url="https://github.com/dockhippie/golang.git"
LABEL org.label-schema.name="Golang"
LABEL org.label-schema.vendor="Thomas Boerger"
LABEL org.label-schema.schema-version="1.0"
