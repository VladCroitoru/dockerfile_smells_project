FROM alpine:3.4

ENV GOLANG_VERSION 1.4.2
ENV GOLANG_SRC_URL https://github.com/gomini/go-mips32.git
ENV GOOS linux
ENV GOARCH mips32le
ENV GOROOT /usr/local/go-mips32

RUN set -ex \
	&& apk add --no-cache --virtual .build-deps \
        bash \
        git \
        file \
        ca-certificates \
        gcc \
        musl-dev \
        openssl \
        openssh \
	\
  && cd /usr/local/ \
	&& git clone "$GOLANG_SRC_URL" go-mips32 \
	&& cd /usr/local/go-mips32/src \
	&& ./make.bash \
	\
	&& apk del .build-deps

ENV GOPATH /go-mips32
ENV PATH $GOPATH/bin:/usr/local/go-mips32/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/pkg" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH/src
