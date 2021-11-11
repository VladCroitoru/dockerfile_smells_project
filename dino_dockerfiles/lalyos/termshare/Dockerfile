FROM alpine:3.3

RUN apk add --no-cache curl \
    && curl -L https://github.com/lalyos/termshare/releases/download/v0.3.0/termshare_v0.3.0_Linux_x86_64.tgz \
      | tar -xz -C /usr/local/bin \
    && apk del curl

ENV PORT 9999
CMD termshare -d
