## -------------------------------------------------------------------------------------------------

FROM golang:1.12 as builder

RUN set -eux; \
    apt-get update -y && \
    apt-get install -y apt-utils upx zip unzip;

# Drop root privileges to build
RUN adduser --disabled-password --gecos "" -u 1000 golang && \
    mkdir -p $GOPATH/src/workspace && \
    chown -R golang:golang $GOPATH/src/workspace;

# Force go modules
ENV GO111MODULE=on

WORKDIR $GOPATH/src/workspace

USER golang

# Clone repository
RUN set -eux; \
    git clone --depth=1 https://github.com/googleCloudPlatform/govanityurls

WORKDIR $GOPATH/src/workspace/govanityurls

# Build final target
RUN set -eux; \
    go build -o bin/govanityurls -ldflags="-s -w"

# Compress binaries
RUN set -eux; \
    upx -9 bin/*

## -------------------------------------------------------------------------------------------------

FROM gcr.io/distroless/base:latest

COPY --from=builder /go/src/workspace/govanityurls/bin/govanityurls /

EXPOSE 8080
WORKDIR /config
VOLUME [ "/config" ]
ENTRYPOINT [ "/govanityurls" ]
