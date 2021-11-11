FROM alpine:latest

RUN apk add --no-cache curl && curl -sSL https://github.com/gliderlabs/sigil/releases/download/v0.4.0/sigil_0.4.0_Linux_x86_64.tgz | tar -zxC /usr/local/bin

WORKDIR /tmp/sigil

ENTRYPOINT [ "/usr/local/bin/sigil" ]
