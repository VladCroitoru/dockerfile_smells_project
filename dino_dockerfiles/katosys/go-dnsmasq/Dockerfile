#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM alpine:3.4
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

ENV VERSION="1.0.7" \
    REPO="https://github.com/janeczku/go-dnsmasq" \
    DNSMASQ_LISTEN="0.0.0.0"

#------------------------------------------------------------------------------
# Install:
#------------------------------------------------------------------------------

ADD ${REPO}/releases/download/${VERSION}/go-dnsmasq-min_linux-amd64 /go-dnsmasq
RUN chmod +x /go-dnsmasq

#------------------------------------------------------------------------------
# Expose ports and entrypoint:
#------------------------------------------------------------------------------

EXPOSE 53 53/udp
ENTRYPOINT ["/go-dnsmasq"]
