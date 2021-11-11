FROM golang:1.8-alpine

RUN apk add --no-cache bash ca-certificates curl git

RUN curl -sL https://github.com/Masterminds/glide/releases/download/v0.12.3/glide-v0.12.3-linux-amd64.tar.gz | tar -xz \
    && mv linux-amd64/glide /usr/local/bin && chmod +x /usr/local/bin/glide \
    && go get github.com/mattn/gom

VOLUME /src
WORKDIR /src

COPY build_environment.sh /
COPY build.sh /

RUN chmod +x /build_environment.sh /build.sh

ENTRYPOINT ["/build.sh"]
