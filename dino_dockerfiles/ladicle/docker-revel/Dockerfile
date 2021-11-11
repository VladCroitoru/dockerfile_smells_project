FROM golang:1.6.2-alpine

# Install dependency packages
RUN set -ex \
    && apk update \
    && apk add --no-cache ca-certificates git wget \
    && update-ca-certificates

# Install go libraries
RUN set -ex \
    && go get github.com/revel/cmd/revel \
    && wget -O glide.zip https://github.com/Masterminds/glide/releases/download/0.10.2/glide-0.10.2-linux-386.zip \
    && unzip glide.zip \
    && rm glide.zip \
    && mv linux-386/glide $GOPATH/bin \
    && rm -rf linux-386
