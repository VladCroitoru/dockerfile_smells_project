FROM alpine:latest
MAINTAINER kost - https://github.com/kost

RUN apk --update add udev chromium ttf-dejavu ttf-ubuntu-font-family ttf-liberation && rm -f /var/cache/apk/* && \
 mkdir -p /work && adduser -D -s /bin/sh user user && chown -R user /work && \
 echo "Success"

USER user

WORKDIR /work

ENTRYPOINT ["chromium-browser"]
