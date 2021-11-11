FROM alpine:3.4

RUN apk --no-cache add rsnapshot

COPY freeupdate.sh /freeupdate.sh

ENTRYPOINT ["/bin/sh", "/freeupdate.sh"]
