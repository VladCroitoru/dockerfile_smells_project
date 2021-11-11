#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM alpine:3.6
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

ENV GOPATH="/go" \
    VERSION="2.6.1"

#------------------------------------------------------------------------------
# Install:
#------------------------------------------------------------------------------

RUN apk add --no-cache -U -t deps go git make musl-dev \
    && apk add --no-cache -U bash libressl ca-certificates \
    && go get github.com/docker/distribution \
    && cd ${GOPATH}/src/github.com/docker/distribution \
    && git checkout tags/v${VERSION} -b build \
    && make PREFIX=/usr clean binaries && mkdir /var/lib/registry \
    && apk del --purge deps && rm -rf /go /tmp/* /var/cache/apk/* \
    && rm -f /usr/bin/registry-api-descriptor-template \
    && rm -f /usr/bin/digest

#------------------------------------------------------------------------------
# Populate root file system:
#------------------------------------------------------------------------------

ADD rootfs /

#------------------------------------------------------------------------------
# Expose ports and entrypoint:
#------------------------------------------------------------------------------

EXPOSE 5000
ENTRYPOINT ["/init"]
