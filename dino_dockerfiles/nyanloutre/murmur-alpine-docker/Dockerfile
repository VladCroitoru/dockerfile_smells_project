FROM alpine:edge
MAINTAINER Paul TREHIOU <paul.trehiou@gmail.com>

RUN apk add -U murmur=1.2.17-r0

# Forward apporpriate ports
EXPOSE 64738/tcp 64738/udp

# Run murmur
ENTRYPOINT ["/usr/bin/murmurd", "-fg", "-v"]
