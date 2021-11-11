FROM golang:1.7-alpine
MAINTAINER Sindre Myren <sindre@myrenett.no>

ARG UPX_VERSION=3.91

RUN apk upgrade --no-cache --available && \
	apk add --no-cache \
		ca-certificates \
		git \
		openssl

ADD https://github.com/lalyos/docker-upx/releases/download/v${UPX_VERSION}/upx /bin/upx
RUN chmod +x /bin/upx
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# build configuration.
ENV GO_GET 0
ENV CGO_ENABLED 0
ENV GO_FLAGS "-installsuffix cgo -tags netgo -ldflags '-w -s'"
ENV UPX_FLAGS -8

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
