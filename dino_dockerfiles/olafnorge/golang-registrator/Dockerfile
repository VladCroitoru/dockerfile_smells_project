FROM alpine:3.7 as builder
MAINTAINER Volker Machon <volker@machon.biz>

ARG BUSY_BOX_VERSION=1.26.2
COPY buildfs/ /

# build and install registrator
WORKDIR /go/src/github.com/olafnorge/golang-registrator
RUN apk add --no-cache --virtual .run-deps \
        ca-certificates \
    && apk add --no-cache --virtual .go-build-deps \
           build-base \
           git \
           go \
	&& export GOPATH=/go \
  	&& git config --global http.https://gopkg.in.followRedirects true \
	&& go get \
	&& go build -ldflags "-X main.Version=$(cat VERSION)" -o /tmp/release/registrator \
	&& apk add --no-cache --virtual .busybox-build-deps \
        gcc \
        make \
        musl-dev \
        ncurses-dev \
        openssl \
    && wget -O- "https://busybox.net/downloads/busybox-${BUSY_BOX_VERSION}.tar.bz2" | tar xj --strip-components=1 -C /usr/src/busybox \
    && cd /usr/src/busybox \
    && make \
    && mkdir -p /tmp/release \
    && cd /tmp/release \
    && mv /usr/src/busybox/busybox . \
    && for SYM_LINK in test [ [[ ps ash sh; do ln -s busybox ${SYM_LINK}; done

FROM alpine:3.7
COPY --from=builder /tmp/release/* /bin/
COPY rootfs/ /

WORKDIR /
USER registrator
ENTRYPOINT ["/bin/registrator"]
