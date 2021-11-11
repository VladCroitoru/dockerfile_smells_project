#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM alpine:3.4
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

ENV GOPATH="/go" \
    VERSION="v0.6.0"

ENV PATH="${PATH}:${GOPATH}/bin"

#------------------------------------------------------------------------------
# Install Mesos DNS and KViator
#------------------------------------------------------------------------------

RUN apk --no-cache add --update -t deps git go \
    && apk --no-cache add --update bash \
    && go get -u github.com/tools/godep \
    && go get -u github.com/mesosphere/mesos-dns \
    && cd ${GOPATH}/src/github.com/mesosphere/mesos-dns \
    && git checkout tags/${VERSION} -b ${VERSION} \
    && go install github.com/mesosphere/mesos-dns \
    && mv ${GOPATH}/bin/mesos-dns /bin/ \
    && apk del --purge deps \
    && rm -rf ${GOPATH} /var/cache/apk/*

#------------------------------------------------------------------------------
# Populate root file system:
#------------------------------------------------------------------------------

ADD rootfs /

#------------------------------------------------------------------------------
# Expose ports and entrypoint:
#------------------------------------------------------------------------------

EXPOSE 53
ENTRYPOINT ["/init"]
