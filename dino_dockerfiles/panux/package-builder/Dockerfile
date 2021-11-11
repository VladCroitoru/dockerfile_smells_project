FROM alpine:3.6

ADD . /build

WORKDIR /build

RUN apk add --no-cache git make bash wget curl go musl-dev gcc ca-certificates wget && update-ca-certificates

RUN make -j20 install

ENTRYPOINT ["/bin/buildpkg"]
