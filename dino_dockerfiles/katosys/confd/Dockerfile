#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM frolvlad/alpine-glibc:alpine-3.6
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

ENV CONFD_VERSION="0.13.0" \
    CONFD_URL="https://github.com/kelseyhightower/confd/releases/download"

#------------------------------------------------------------------------------
# Install:
#------------------------------------------------------------------------------

RUN apk add --update -t deps openssl; apk add --update bash && cd /tmp \
    && wget ${CONFD_URL}/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 -O /bin/confd \
    && chmod +x /bin/confd; apk del --purge deps \
    && rm -rf /tmp/* /var/cache/apk/*

#------------------------------------------------------------------------------
# Entrypoint:
#------------------------------------------------------------------------------

ENTRYPOINT ["/bin/confd"]
